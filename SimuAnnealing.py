import sys
from random import random,seed,randint,shuffle, randrange
import time
from math import exp
from copy import deepcopy
import os
import tsplib95

"""
	funcao p() retorna uma probabilidade P 0<P<=1
"""
def p(delta,temp):
	#print("delta "+ str(temp))
	return exp(-delta/temp)

"""
	-A chance de aceitar um vizinho pior diminui a cada solucao que se aceita
	-exaustion_criteria eh o numero de vizinhos que o algoritmo tem que avaliar antes de parar
"""
def create_initial_solution (problem):

	initial_solution = list(problem.get_nodes())

	shuffle(initial_solution)

	return initial_solution

def route_distance (route , distancies): # calcula a distancia do percurso

	total = 0
	num_cities = len(route)

	for i in range(num_cities):
		j = ( i + 1 ) % num_cities

		#print("esse é o I "+ str(i)+"\t"+"esse é o J " + str(j))
		city_i = route [ i ]
		city_j = route [ j ]

		total = total + distancies.wfunc(city_i, city_j)

	return total

def reallocate(cities):
	l = len(cities)-1
	n1 = randint(0,l)
	n2 = randint(0,l)

	#print("n1 - n2 \t"+str(n1)+"\t"+str(n2))

	while n1==n2:
		n2 = randint(0,l)
	new = deepcopy(cities)
	new[n1] = cities[n2]
	new[n2] = cities[n1]
	return new

def getRandomNeighbour(solution):
	return reallocate(solution)

def simulated_annealing(temperature, problem):
	current = create_initial_solution(problem)
	current_eval = route_distance(current, problem)
	best = current
	best_eval = current_eval

	#a cada temperatura, visita-se vizinhos ate trocar com um deles
	while temperature > 1:

		#swaped permite a iteracao no conjunto dos vizinhos numa mesma temperatura
		swaped = False

		#visita a cada vizinho
		while not swaped:
			#pede novo vizinho aleatório
			solution = getRandomNeighbour(current)
			solution_eval = route_distance(solution, problem)
			#avaliação do vizinho com a solução atual
			delta_eval = solution_eval - current_eval
			if delta_eval<0:
				current = solution
				current_eval = solution_eval
				if current_eval < best_eval:
					best = current
					best_eval = current_eval
				swaped = True
				continue
			elif delta_eval>0:
				if random() < p(abs(delta_eval),temperature):
					current = solution
					current_eval = solution_eval
					swaped = True
					#print("Aceito")
					continue

		temperature-=1
		#print("cri " + str(exaustion_criteria))

	return best,best_eval

if __name__ =="__main__":
	seed(randrange(0, 50))
	problem = tsplib95.load_problem('brazil58.tsp')
	(best, best_eval) = simulated_annealing(10000,problem)
	print(best_eval,"\n", best)