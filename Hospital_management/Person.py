#pra
class Person:
    def __init__(self, first_name, surname):
        # Initialize the Person object with the provided first name and surname
        self.__first_name = first_name  # variable to store the first name
        self.__surname = surname  #  variable to store the surname
      
    def get_first_name(self):
        # Get the first name of the person
        return self.__first_name
    
    def set_first_name(self, new_first_name):
        # Set a new value for the first name
        self.__first_name = new_first_name  # This line has a mistake, it should be self.__first_name = new_first_name
    
    def get_surname(self):
        # Get the surname of the person
        return self.__surname
    
    def set_surname(self, new_surname):
        # Set a new value for the surname
        self.__surname = new_surname

        