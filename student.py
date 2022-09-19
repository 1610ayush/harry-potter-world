# class is the blueprint of an object
class Student: 
    # __init__ function is called when a object is created and this function instantiate the attributes of the object
    # self keyword refers to the current object so it is used to set the attributes of current object
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # __str__ function is called when some function wants to call the object as string, in this case used to print.
    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("house: ")
        return cls(name, house)


    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing name")
    #     self._name = name


    # #Getter
    # @property
    # def house(self):
    #     return self._house
    
    # #Setter
    # @house.setter
    # def house(self, house):
    #     if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    #         raise ValueError("Invalid house")
    #     self._house = house

    
def main():
    student = Student.get()  #calling a class method to get the name and house and then instantiate the student object
    print(student)

# def get_student():
#     name = input("name: ")
#     house = input("house: ")
#     return Student(name, house)  #object - instantiation of class and at this point we are calling __init__ function


if __name__ == "__main__":
    main()
