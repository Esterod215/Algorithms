#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []
  for (k,v) in recipe.items():
    
    if k not in ingredients:
      
      return 0
    elif recipe[k] > ingredients[k]:
      
      return 0
    else:
      batches.append(int(ingredients[k]/recipe[k]))
      
  return int(min(batches))
      
  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 60, 'flour': 51 }
  print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))
  print(recipe_batches(recipe,ingredients))
  # print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))