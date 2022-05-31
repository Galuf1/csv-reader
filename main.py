import csv
from socket import create_server

animal_getter = input("type of animal ")
animal = animal_getter
file = f"data/{animal}.csv"
data = {} 
try:
    with open(file) as csvfile:
        csvreader =  csv.reader(csvfile,delimiter=",")
        for row in csvreader:
            key = row[0]
            value = f"{row[0]} is a{row[1]} year old{row[2]}."
            data[key]=value
    data.pop("name")
    pet_name = str(input("name of the pet "))


    print(data[pet_name])
except:
    print(f"Sorry, we don't have any {animal} here")





        

class animal:
    def __init__(self,type,name,age):
        self.name = name
        self.type = type
        self.age = age

    def __str__(self):
            return (f"{self.name} is a {self.age} year old {self.type}.")


# fido = animal("fido", 4, "husky")
# print(fido) 





    


            


      
#f"{name} is a {age} year old {breed}."