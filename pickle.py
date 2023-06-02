import pickle

class Person:
    def __init__(self,name,age,adress) -> None:
        self.name = name
        self.age = age
        self.adress = adress




p1 = Person("arad",20,"tehran")
p2 = Person("foo",45,"avangard")
p3 = Person("joojoo",18,"shiraz")
person_list = [p1,p2,p3] 

def pickleing():
    with open("pickeled.pkl", "wb") as f:
        pickle.dump(person_list, f)

def unpickleing():
    with open("pickeled.pkl", "rb") as f:
        loaded_list = pickle.load(f)
        print(loaded_list)