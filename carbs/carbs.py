
import os 
import pprint
from traceback import print_tb
import requests
from dotenv import load_dotenv

class Nutritions:
    
    def __init__(self):
        # the constructor that contains the main variables
        self.min_carb= None
        self.max_carb= None
        self.r = None
        self.url= None
        self.api_key =  os.getenv("API_KEY")
    
    def set_carb(self, min, max):
         # function that has min and max attributes that raises a warning if the min> max
        if min> max:
            
            raise ValueError("it can not be Minimum value > Maximum value")
        else : 
            
            self.min_carb = min
            self.max_carb= max
   

    def get_data(self):
         # The API requests link that takes the api_key, min_carb, and max_carb as parameters
        self.url = f'https://api.spoonacular.com/recipes/findByNutrients?apiKey={self.api_key}&minCarbs={self.min_carb}&maxCarbs={self.max_carb}'
        self.r = requests.get(self.url).json()
        return requests.get(self.url).json()
    

    def __str__(self):
        return "welcome from Nutritions class"    
    def __repr__(self) :
        return "Nutritions class"
        
    # Looping the each response attribute in each function and store it in a new variable  
    def get_calories(self):
        new_calories=[]
        for i in self.r:
            new_calories.append({"calories": i["calories"],"title": i["title"]})
        return new_calories
    def get_protein(self):
        new_protein=[]
        for i in self.r:
            new_protein.append({"protein": i["protein"],"title": i["title"]})
        return new_protein

    def get_fat(self):
        new_fat=[]
        for i in self.r:
            new_fat.append({"fat": i["fat"],"title": i["title"]})
        return new_fat

    def get_carbs(self):
        new_carbs=[]
        for i in self.r:
            new_carbs.append({"carbs": i["carbs"],"title": i["title"]})
        return new_carbs
load_dotenv()
nutritions=Nutritions()
if __name__ == "__main__":
    nutritions.set_carb(100,119)
    nutritions.get_data()
    print(nutritions.url)
    print("="*50)
   