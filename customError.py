class NoScriptFound(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        # Now for your custom code...
        self.errors = errors
    def __str__(self):
        return "{0}: {1}".format(self.errors,self.message)

# Error raised if an user makes and invalid selection
class InvalidSelection(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        # Now for your custom code...
        self.errors = errors
    def __str__(self):
        return "{0}: {1}".format(self.errors,self.message)
