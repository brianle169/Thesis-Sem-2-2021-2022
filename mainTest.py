import pprint
import sys
import terminatingCondition.termination
import fixedParameters.parameters
from rawDataTranslation.translateRaw import *
from createChromosome.chromosomeEncoding import *
from decodeChromosome.chromosomeDecoding import *
from geneticOperators.evaluateFitness import *
from geneticOperators.reproduction import selection
from opposition.oppositeSolution import *

#Get problem instance and information
path = "D:\School Materials\Thesis\Code\TextData\Monaldo\Fjsp\Job_Data\Hurink_Data\Text\\vdata\mt06.fjs"
problemInfo = getInfo(path)
data = translate(path)
instanceName = str(path.split("\\")[11])
print(f"FJSP problem instance: {instanceName}")
print(f"Problem size:\n- Job numbers: {problemInfo[0]}\n- Machine numbers: {problemInfo[1]}\n- Average machines per operation: {problemInfo[2]}")
pprint.pprint(data)

exampleMS1 = createMS(data)
exampleMS2 = createMS(data)
print(exampleMS1, exampleMS2)







# #Initialize population
# initializePop = initialPop(data)
# #Create opposites
# oppositePop = oppositePopulation (data, initializePop)

# #Evaluate fitness and omit the weaks:
# #Append two populations, sort descending in terms of fitness, pick the fittest 50.

# #Append two populations
# population = initializePop + oppositePop

# #Sort the population in terms of makespan, in ascending order, which means the fittest will appear first.
# sortedPop = sorted(population, key = lambda solution: fitness(data, solution))

# #Form the final "initial" population:
# initialPop = sortedPop[:parameters.popSize]
# initialFit = []
# for x,y in enumerate(initialPop):
#     initialFit.append(fitness(data,y))
# averageFitInitial = sum(initialFit) / len(initialFit)
# print(initialFit, averageFitInitial, min(initialFit), max(initialFit), "\n")

# selectedFit = []
# intermediatePool = selection(initialPop, data)
# for i,j in enumerate(intermediatePool):
#     selectedFit.append(fitness(data,j))
# averageFitSelected = sum(selectedFit)/len(selectedFit)
# print(selectedFit, averageFitSelected, min(selectedFit), max(selectedFit))

