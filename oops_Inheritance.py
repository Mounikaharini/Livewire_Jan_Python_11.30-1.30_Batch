#single inheritance
class briyani:
    def ingredients(self):
        ing = ["oil","spices","rice","water","tomato","onion","ginger garlic paste",
               "Mint leaves","masala","curd","ghee"]
        print("🥘🍲   Ingredients   🥘🍲\n")
        for i in ing:
            print("==> ",i)
    def recipe(self):
        print("\n🧑‍🍳 Steps to Cook 🧑‍🍳\n")
        print("Step 1 : oil / ghee then roast the spices")
        print("Step 2 : ginger garlic paste , onion , tomato , masala")
        print("Step 3 : after 5mins add water and rice")
        print("Step 4 : after 20mins add lemon and ready to serve")

class chickenbriyani(briyani):
    def addedingredients(self):
        print("Addtional Ingredient : Chicken")

b = briyani()
b.ingredients()
b.recipe()

c=chickenbriyani()
c.ingredients()
c.addedingredients()
c.recipe()

#hierarchical inheritance
class vegbriyani(briyani):
    def addedingredients(self):
        print("Addtional Ingredient : Vegetables")

class mushroombriyani(briyani):
    def addedingredients(self):
        print("Addtional Ingredient : Mushroom")

m=mushroombriyani()
m.ingredients()
m.addedingredients()
m.recipe()

#multiple inheritance

class dress:
    def women(self):
        print("Tops and Tunics \nSaree \nBlouse \nShirts \n")
    def men(self):
        print("Shirt \nPants \nT-shirt \n")

class homeAppliances:
    def homedecors(self):
        print("Curtains \nMat \nKitchen Utilites \n")
    def electronics(self):
        print("Mobile \nTV \n")
    def furnitures(self):
        print("Chairs \nTables \n")
        
class accessories:
    def footware(self):
        print("Shoes \nFlats \nHeels \nSandals \nFlipflops \ncrocs \n")
    def jewellry(self):
        print("Chains \nBangles \nEarrings \nRings \nAnklets \n")
        
class meesho(dress,homeAppliances,accessories):
    def title(self):
        print(" Welcome to Meesho ")

m=meesho()
m.title()
m.women()
m.men()
m.homedecors()
m.electronics()
m.furnitures()
m.footware()
m.jewellry()




