def process_log_file(filename):
    # Open the file and read lines
    with open(filename, 'r') as file:
        # Get only lines with ERROR
        error_lines = (line for line in file if "ERROR" in line)
        
        # Extract timestamps from error lines
        timestamps = (line.split()[0] for line in error_lines)
        
        # Parse timestamps to datetime objects
        from datetime import datetime
        dates = (datetime.strptime(ts, "%Y-%m-%d") for ts in timestamps)
        
        # Count errors by month
        month_counts = {}
        for date in dates:
            month_key = (date.year, date.month)
            month_counts[month_key] = month_counts.get(month_key, 0) + 1
            
        return month_counts

# This processes a potentially huge log file using minimal memory
