# A practical example: Database connection context manager
class DatabaseConnection:
 def __init__(self, connection_string):
    self.connection_string = connection_string
    self.connection = None
 
 def __enter__(self):
    # Code for connecting to the database
    print(f"Connecting to database: {self.connection_string}")
    self.connection = {"connected": True} # Mock connection
    return self
 
 def __exit__(self, exc_type, exc_val, exc_tb):
    # Code for closing the connection
    if self.connection:
       print("Closing database connection")
       self.connection = None
 
    if exc_type is not None:
       print(f"An error occurred: {exc_val}")
       # Log the error, perform cleanup, etc.
 
       # Return False to propagate exceptions
       return False

# Usage
with DatabaseConnection("postgresql://user:password@localhost/db") as conn:
   # Database operations
   print("Performing database operations")
   # If an exception occurs here, __exit__ will be called with the exception info
