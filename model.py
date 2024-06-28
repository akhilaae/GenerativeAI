import torch
from transformers import pipeline

recipe_gen=pipeline(model="flax-community/t5-recipe-generation")

results=recipe_gen(str)

print(results)