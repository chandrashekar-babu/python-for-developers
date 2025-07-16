#access_log = '''51.15.43.205 - - [01/Jan/2017:00:01:14 -0500] "GET /random-thoughts/godmen-leaders-and-superstars.html HTTP/1.0" 200 44545 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36" 0 0 "off:-:-" 365 855116 192.252.149.39 chandrashekar.info'''

import re

field_names = ("client_ipaddr", "timestamp", 
               "http_method", "request", 
               "response_code", "response_size",
               "referer_url", "user_agent")

regex = r"""
    (?P<{}>[\d\.]+)      # Extract IP address
    \s-\s-\s
    \[
    (?P<{}>.+?)          # Extract time-stamp 
    \]\s"
    (?P<{}>\w+)          # Extract HTTP method (GET / POST / HEAD)
    \s
    (?P<{}>.+?)          # Extract request/query string
    \sHTTP\/\d\.\d"\s
    (?P<{}>\d+)          # Extract response code
    \s
    (?P<{}>\d+)          # Extract response size
    \s"
    (?P<{}>.+?)          # Extract Referer URL
    "\s"
    (?P<{}>.+?)          # Extract User-Agent (web browser) information
    "\s\d\s\d
""".format(*field_names)

pattern = re.compile(regex, re.VERBOSE | re.MULTILINE | re.DOTALL)

#m = pattern.match(access_log)
#m.groupdict()

from csv import DictWriter
with open("www_logs/2017-01/www-01.log") as logfile, \
     open("access_log_1.csv", "w") as outfile:
    
    csvout = DictWriter(outfile, fieldnames=field_names)
    csvout.writeheader()
    for line in logfile:
        row = pattern.match(line)
        if row: csvout.writerow(row.groupdict())
    


