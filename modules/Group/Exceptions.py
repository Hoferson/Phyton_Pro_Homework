class Group_limit_error(Exception):

    def __init__ (self, message, limit):
        self.message = message
        self.limit = limit

    def __str__ (self):
        return f'{self.message}{self.limit}'
    
class Member_doesnt_exist(Exception):

    def __init__ (self, message):
        self.message = message
    
    def __str__ (self):
        return f'{self.message}'