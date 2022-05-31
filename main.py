import csv
from socket import create_server

class animal:
    def __init__(self,name,age=None,breed=None):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
            return (f"{self.name} is a{self.age} year old{self.breed}.")

animal_getter = input("type of animal ")
animal_type = animal_getter
file = f"data/{animal_type}.csv"
data = {} 
try:
    with open(file) as csvfile:
        csvreader =  csv.reader(csvfile,delimiter=",")
        # populate dictionary data with name as key and other as a list of attributes
        for row in csvreader:
            key = row[0]
            age_data = row[1]
            breed_data = row[2]
            data[key]= [age_data,breed_data]
    # removes first row
    poppedKeys = data.pop("name")
    pet_name = str(input("name of the pet "))
    query = animal(pet_name,data[pet_name][0],data[pet_name][1])
    print(query)
    
except:
    print(f"Sorry, we don't have any {animal_type} here")





        










    


            


      
#f"{name} is a {age} year old {breed}."