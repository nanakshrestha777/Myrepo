
#pra
class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
    
        self.__doctor = 'None'
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms
    

       

    
    def full_name(self) :
        """full name is first_name and surname"""
        #ToDo2
        return f"{self.__first_name} {self.__surname}"
        


    def get_doctor(self) :
        #ToDo3
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        print_sym = input("Please! Enter Your Symptoms-Here: ")
        print(print_sym)
        return
    def get_symptoms(self):
        return self.__symptoms
        

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
