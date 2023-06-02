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

def pickleing(list_of_ppl):
    with open("pickeled.pickle", "wb") as f:
        pickle.dump(list_of_ppl, f)

def unpickleing():
    with open("pickeled.pickle", "rb") as f:
        loaded_list = pickle.load(f)
        print(loaded_list)
        for i in range(len(loaded_list)):
            print(loaded_list[i].name, loaded_list[i].age, loaded_list[i].adress)

pickleing(person_list)
unpickleing()