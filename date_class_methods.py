class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def from_string(cls, date_string):
        """Alternative constructor 
           from string YYYY-MM-DD"""
        year, month, day = \
           map(int, date_string.split('-'))
        return cls(day, month, year)
    
    @classmethod
    def today(cls):
        """Factory method for current date"""
        import datetime
        now = datetime.datetime.now()
        return cls(now.day, now.month, now.year)
    
# Using class methods
date1 = Date.from_string("2025-07-15")
date2 = Date.today()
