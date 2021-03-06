import species
from matplotlib import pyplot as plt
import numpy as np
import pickle
import game

'''
This script evolves a population of players, generation by generation
The final result is a player that plays the game very well, if not perfectly
Whole population is pickled and saved to disk (several 10's of MBs)
'''

imr = 0.08
amr = 0.00
size = 100


species.X = 150
species.Y = 300
species.R = 25
game.jump_speed = 20
game.WIDTH,game.HEIGHT = 800,600
game.speed = 6
game.barrier_prob = 10
game.barrier_width = 75
game.vision_rows = game.rows(10)

population = species.Population(imr,amr,size,io=(12,1),hidden_layers=[15,15],activations=['relu','relu','sigmoid'])

fitnesses = []
num_gens = 300
for i in range(num_gens):
    population.calculate_fitness()
    fitness = population.max_fitnesses[-1]
    fitnesses.append(fitness)
    print('Generation',population.gen,':',fitness)
    if i != num_gens-1: population.evolve()


plt.plot(fitnesses)
raise Exception
with open('population6.pkl','wb') as file:
    pickle.dump(population,file)

plt.show()
