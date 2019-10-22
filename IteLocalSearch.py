import time
from random import random,seed,randint,shuffle, randrange
from math import exp
from copy import deepcopy
import tsplib95

def create_initial_solution (problem):

	initial_solution = list(problem.get_nodes())

	shuffle(initial_solution)

	return initial_solution

def route_distance (route , distancies): # calcula a distancia do percurso

	total = 0
	num_cities = len(route)

	for i in range(num_cities):
		j = ( i + 1 ) % num_cities

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

def perturbate(solution, nivel):
	# modificated = nivel + 1
	# i = 1
	# while i <= modificated: 
	# 	i+=1
	solution = reallocate(solution)
		#print("i -- " + str(i))

	return solution

def local_search(max_search, best, best_eval, cities, problem):

	i = 0
	while i <= max_search: 
		candidate = reallocate(cities)
		candidate_eval = route_distance(candidate, problem)
		if candidate_eval < best_eval: 
			#i = 0
			best = candidate
			best_eval = candidate_eval
		else: 
			i+=1

		#print("i --- " + str(i))

	return best, best_eval

def iterated_local_search(max_ite, max_search, problem):
	current = create_initial_solution(problem)
	current_eval = route_distance(current, problem)
	best = current
	best_eval = current_eval
	i = 0
	nivel = 1

	while i < max_ite:
		i+=1
		#print("i --- " + str(i))

		current = perturbate(current, nivel)
		(current, current_eval) = local_search(max_search, best, best_eval, current, problem)

		if current_eval < best_eval: 
			best = current
			best_eval = current_eval 
			nivel = 1
		else: 
			nivel += 1
		
	return best, best_eval

if __name__ =="__main__":
	seed(randrange(0, 50))
	problem = tsplib95.load_problem('hk48.tsp')
	(best, best_eval) = iterated_local_search(10000, 30,problem)
	print(best_eval,"\n", best)
	print("Elapsed time = %f s" % time.process_time())