def read_large_file(file_path, chunk_size=1024):
    """Generator to read a large file in chunks."""
    with open(file_path, 'r') as file:
        while True:
            # Read a chunk of data
            data = file.read(chunk_size)
            
            # If no more data, stop iteration
            if not data:
                break
                
            # Yield the chunk
            yield data

def process_data(d):
    print("Processing: ", d)
    
# Usage for processing a large file without loading it all into memory
for chunk in read_large_file('large_log_file.txt'):
    process_data(chunk)
