def process_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            result = len(data.split())
            return result
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        # Could create the file or use a default
        return 0
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        # Could request elevated permissions
        return 0
    except Exception as e:
        print(f"Unexpected error: {e}")
        # Log the error for debugging
        raise  # Re-raise the exception for higher-level handling
    else:
        print(f"Successfully processed file: {filename}")
    finally:
        print("File processing attempt completed")

# Usage
word_count = process_file("sample.txt")