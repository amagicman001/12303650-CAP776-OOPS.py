class Eggrecipe:
    def __init__(self,name):
        self.name = name          
        self.ingredients = []     
        self.steps =[]     

    def addingredient(self,ingredient):
        self.ingredients.append(ingredient)
    def addstep(self, step):
        self.steps.append(step)
    def displayrecipe(self):
        print(f"Recipe Name: {self.name}")
        print("\nIngredients:")
        for ingredient in self.ingredients:
            print(f"-> {ingredient}")
        print("\nSteps:")
        for i, step in enumerate(self.steps, 1):
            print(f"{i}. {step}")



recipe = Eggrecipe("Classic Scrambled Eggs")
recipe.addingredient("2 eggs")
recipe.addingredient("Salt to taste")
recipe.addingredient("1 tablespoon butter")
recipe.addingredient("Pepper to taste")
recipe.addstep("In a large bowl, pour together the eggs and salt.")
recipe.addstep("Beat the eggs in a bowl.")
recipe.addstep("Heat the butter in a pan over medium heat.")
recipe.addstep("Pour in the eggs and cook gently.")
recipe.addstep("Stir continuously until the eggs are just set.")
recipe.addstep("cook with salt and pepper and serve immediately.")

recipe.displayrecipe()
