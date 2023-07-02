from Doctor import Doctor
from Patient import Patient
#pra

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
        # if self.__username == username and self.__password == password:

        #     print("___Login Successful___")
        # else:
        #     raise Exception("Invalid username or password | Try again!")
        return self.__username == username and self.__password == password

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        D_first_name = input("Enter the name of the Doctor: ")
        D_sur_name = input("Enter the surname of the Doctor: ")
        D_speciality = input("Enter the speciality of Doctor: ")
        return D_sur_name, D_first_name, D_speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        try:
            op = input("Enter the Operation-Here: ")


            # register
            if op == '1':
                print("-----Register-----")

                # get the doctor details
                print('Enter the doctor\'s details:')
                #ToDo4
                D_first_name, D_sur_name, D_speciality = self.get_doctor_details()
                

                # check if the name is already registered
                name_exists = False
                for doctor in doctors:
                    if D_first_name == doctor.get_first_name() and D_sur_name == doctor.get_surname():
                        print('Name already exists.')
                        break
                        #ToDo5
                         # save time and end the loop
                if name_exists == False:
                    doctors.append(Doctor(D_first_name,D_sur_name, D_speciality))
                    print("*Doctor Registerd*")
                    self.view(doctors)

                #ToDo6
                # add the doctor ...
                                                            # ... to the list of doctors
                # print('Doctor registered.')

            # View
            elif op == '2':
                print("-----List of Doctors-----")
                print("ID   |     Full NAME     |   Speciality   ")
                self.view(doctors)
                #ToDo7
                

            # Update
            elif op == '3':
                while True:
                    print("-----Update Doctor`s Details-----")
                    print('ID |          Full name           |  Speciality')
                    self.view(doctors)
                    try:
                        index = int(input('Enter the ID of the doctor: ')) - 1
                        doctor_index=self.find_index(index,doctors)
                        if doctor_index!=False:
                    
                            break
                            
                        else:
                            print("Doctor not found")

                        
                            # doctor_index is the ID mines one (-1)
                            

                    except ValueError: # the entered id could not be changed into an int
                        print('The ID entered is incorrect')

                # menu
                print('Choose the field to be updated:')
                print(' 1 First name')
                print(' 2 Surname')
                print(' 3 Speciality')
                op = int(input('Input: ')) # make the user input lowercase

                #ToDo8
                if op == 1:
                    new_first_name = input("Enter new name:")
                    doctors[index].set_first_name(new_first_name)
                    print("New firstname set")
                    self.view([doctors[index]])
                                        
                                        
                elif op == 2:
                    new_surname = input("Enter new surname:")
                    doctors[index].set_surname(new_surname)
                    print("New surname set")
                    self.view([doctors[index]])
                                    

                elif op == 3:
                    new_speciality = input("enter new speciality:")
                    
                    doctors[index].set_speciality(new_speciality)
                    print("new speciality set")
                    self.view([doctors[index]])
                

            # Delete
            elif op == '4':
                print("-----Delete Doctor-----")
                print('ID |          Full Name           |  Speciality')
                self.view(doctors)
                try:
                        index = int(input('Enter the ID of the doctor to be deleted: ')) -1
                        doctor_index=self.find_index(index,doctors)
                        if(doctor_index!= False):
                            doctors.pop(index)
                            print("deleted!!!")
                            self.view(doctors)
                            
                            # if the id is not in the list of patients
                        else:
                            print('Invalid operation choosen. Check your spelling!')
                except:
                    print("invalid input")

                  
                #ToDo9
    
        except ValueError:
            print("Oops! Wrong operation- Please choose the valid Operation")
        





    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index].full_name())
                
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        try:      
            Patient_index = int(input('Please enter the patient ID: '))-1
                
            if Patient_index in range(len(patients)):
                discharge_patients.append(patients.pop(Patient_index))
                self.view_discharge(discharge_patients)
                with open("patient.txt", "w") as file:
                    for patient in patients:
                        file.write(f"{patient}")

                # with open("patient.txt", "r") as file:
                #     contents = file.readlines()
                #     print(contents)
                
                
               
                print("Patient discharged successfully.")
                        
                
            else:
                print("patients is not available...")
            
        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')

        

        #ToDo12
        

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        self.view(discharged_patients)
    def admin_details(self):
        print(f"username : {self.__username}")
        print(f"password : {self.__password}")
        print(f"address : {self.__address}")

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        try:
            op = int(input('Input: '))

            if op == 1:
                #ToDo14
                self.admin_details()
                new_username = input("Enter new username: ")

                confirm_username = input("Repeat same username: ")

                if (new_username == confirm_username):
                    self.__username = new_username
                    print("Username Upated")
                else:
                    print("username unmatched")
                

            elif op == 2:
                self.admin_details
                password = input('Enter the new password: ')
                confirm_password = input("Repeat same password: ")
                # validate the password
                if password == confirm_password:
                    self.__password == confirm_password
                    print("Password Updated!!")
                else:
                    print("Password did not match!! Try again!")
                    self.update_details()

            elif op == 3:
                #ToDo15
                self.admin_details()
                new_address = input("Enter new address: ")
                if new_address == new_address:
                    self.__address = new_address
                    print("Address updated")
                
            

            else:
                #ToDo16
                pass
        except ValueError:
            print("Invalid option!! Please try again!")



admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
patients = [Patient('Sara','Smith', 20, '07012345678','B1 234','fever'), Patient('Mike','Jones', 37,'07555551234','L2 2AB','cough'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC','fatigue')]

discharged_patients = []
