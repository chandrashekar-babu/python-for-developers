import re

field_names = ("client_ipaddr", "timestamp", 
               "http_method", "request", 
               "response_code", "response_size",
               "referer_url", "user_agent")

regex = r"""
    (?P<{}>[\d\.]+)
    \s-\s-\s
    \[(?P<{}>.+?)\]
    \s"
    (?P<{}>\w+)
    \s
    (?P<{}>.+?)
    \sHTTP\/\d\.\d"\s
    (?P<{}>\d+)
    \s
    (?P<{}>\d+)
    \s"
    (?P<{}>.+?)
    "\s"
    (?P<{}>.+?)
    "\s\d\s\d
""".format(*field_names)

pattern = re.compile(regex, re.VERBOSE | re.MULTILINE | re.DOTALL)
m = pattern.match(access_log)
m.groupdict()
from csv import DictWriter
with open("www_logs/2017-01/www-01.log") as logfile, \
     open("access_log_1.csv", "w") as outfile:
    
    csvout = DictWriter(outfile, fieldnames=field_names)
    csvout.writeheader()
    for line in logfile:
        row = pattern.match(line)
        if row: csvout.writerow(row.groupdict())
    


