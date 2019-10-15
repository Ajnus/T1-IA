import time
from math import exp
from random import seed, random, randint, shuffle, randrange
from copy import deepcopy
import tsplib95

'''
        regulação da temperatura
'''
def KirkpatrickCooling (startTemp, alpha):
        t = startTemp
        while True:
                yield t
                t = alpha * t

"""
        retorna uma probabilidade 0 < p <= 1
"""
def p(delta,temp):
        return exp(-delta/temp)

def CreateInitialSolution (problem):
        initialSolution = list(problem.get_nodes())
        shuffle(initialSolution)

        return initialSolution

def RouteDistance (route , dist):

        total = 0
        cardCities = len(route)

        for i in range(cardCities):
                j = (i + 1) % cardCities
                #print("esse é o I "+ str(i)+"\t"+"esse é o J " + str(j))
                city_i = route [i]
                city_j = route [j]

                total = total + dist.wfunc(city_i, city_j)

        return total

def Reallocate(cities):
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

def GetRandomNeighbour(solution):
        return Reallocate(solution)

def SimulatedAnnealing(startTemp,alpha,exaustionCrit, problem):
        current = CreateInitialSolution(problem)
        currentEval = RouteDistance(current, problem)
        best = current
        bestEval = currentEval
        
        '''
        temperatura diminui conforme o tempo é gasto
                
        '''
        cooling = KirkpatrickCooling(startTemp,alpha)

        #a cada temperatura, visita vizinhos ate trocar com algum
        for temp in cooling:

                #swaped permite a iteracao no conjunto dos vizinhos numa dada temperatura
                swaped = False

                comparisions = 1

                #visita vizinho
                while not swaped:
                        #pede novo vizinho qualquer
                        solution = GetRandomNeighbour(current)
                        solutionEval = RouteDistance(solution, problem)
                        #avaliação do vizinho com a solução atual
                        deltaEval = solutionEval - currentEval
                        if deltaEval<0:
                                current = solution
                                currentEval = solutionEval
                                if currentEval < bestEval:
                                        best = current
                                        bestEval = currentEval
                                swaped = True
                                continue
                        elif deltaEval>0:
                                if random() <= p(abs(deltaEval),temp):
                                        current = solution
                                        currentEval = solutionEval
                                        swaped = True
                                        print("ok")
                                        continue

                        comparisions+=1
                        if comparisions == exaustionCrit:
                                print("\nComparisions: " + str(comparisions))
                                return best,bestEval
                        
if __name__ =="__main__":
        seed(randrange(0, 10))
        problem = tsplib95.load_problem('si175.tsp')
        (best, bestEval) = SimulatedAnnealing(3170,0.95,28000,problem)
        print("Best Evaluation: ", bestEval,"\nRoute:", best)
        print("Elapsed time = %f s" % time.process_time())
