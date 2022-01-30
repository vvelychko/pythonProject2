class Human:
    def __init__(self, fullname, age, birthdate, phone, city, address):
        self.__name = fullname
        self.__age = age
        self.__birthdate = birthdate
        self.__phone = phone
        self.__city = city
        self.__address = address

    #def __str__(self):
     #   return f"Name: {self.__name}, age: {self.__age}"
    def get_full_info(self):
        full_info = f"{self.__name}, {self.__age}, {self.__birthdate}, {self.__phone}, {self.__city}, {self.__address}"
        return f"Name: {self.__name}, age: {self.__age}, birthdate: {self.__birthdate}, phone: {self.__phone}, city: {self.__city}, address: {self.__address}"

    def set_full_info(self, fullname, age, birthdate, phone, city, address):
        self.__name = fullname
        self.__age = age
        self.__birthdate = birthdate
        self.__phone = phone
        self.__city = city
        self.__address = address

  #  def __repr__(self):
   #     return f"Name: {self.__name}, age: {self.__age}, birthdate: {self.__birthdate}, phone: {self.__phone}, city: {self.__city}, address: {self.__address}"


human = Human('Mike', 15, "01.01.2000", "1234567", "NY", "Some address")
print(human.get_full_info())
human.set_full_info('Ed', 22, "02.02.1985", "7654321", "Chicago", "Elm Street 100")
print(human.get_full_info())