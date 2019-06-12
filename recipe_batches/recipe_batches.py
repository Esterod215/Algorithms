#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  for (k,v), (k2,v2) in zip(recipe.items(),ingredients.items()):
    if v2 < v:
      return 0
    else:
      batches = 1
    
  
  return batches
  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print(recipe_batches(recipe,ingredients))
  # print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))