class Persona:

    def __init__(self, first_name: str,last_name: str) -> bool :
        self.__eta = None

        if isinstance(first_name,str):
            self.__first_name = first_name
        else:
            self.__first_name = None
            self.__eta = None
            print(f'Il nome inserito non è una stringa!')
            
        if isinstance(last_name,str):
            self.__last_name = last_name
        else: 
            self.__first_name = None
            self.__eta = None
            print(f'Il nome inserito non è una stringa!')

        if isinstance(first_name, str) and (isinstance(last_name, str)):
            self.__eta = 0

    def setName(self, first_name:str):
        if isinstance(first_name,str):
            self.__first_name = first_name
        else: 
            print(f'Il nome inserito non è una stringa!')
            
    def setLastName(self, last_name: str ) -> str:
        if isinstance(last_name,str):
            self.__last_name = last_name
        else: 
            print(f'Il nome inserito non è una stringa!')

    def setAge(self, age: int) -> int:
        if isinstance(age,int):
            self.__eta = age
        else: 
            print(f'Il nome inserito non è una stringa!')



            


        




        
       
        
            




 