import datetime
import unittest
import random

import genetic

class Fitness:
    NumbersInSequenceCount = None
    TotalGap = None

    def __init__(self, numbersInSequenceCount, totalGap):
        self.NumbersInSequenceCount = numbersInSequenceCount
        self.TotalGap = totalGap

    def __gt__(self, other):
        if self.NumbersInSequenceCount != other.NumbersInSequenceCount:
            return self.NumbersInSequenceCount > other.NumbersInSequenceCount
        return self.TotalGap < other.TotalGap

    def __str__(self):
        return "{0} Sequential, {1} Total Gap".format(
            self.NumbersInSequenceCount,
            self.TotalGap
        )

class SortedNumbersTests(unittest.TestCase):
    def test_sort_10_numbers(self):
        self.sort_numbers(10)
    def sort_numbers(self, totalNumbers):
        def fnGetFitness(genes):
            return get_fitness(genes)
        def fnDisplay(candidate):
            display(candidate, startTime)

        geneset = [i for i in range(100)]
        startTime = datetime.datetime.now()
        optimalFitness = Fitness(totalNumbers, 0)
        best = genetic.get_best(fnGetFitness, totalNumbers, optimalFitness, geneset, fnDisplay)
        #self.assertEqual(not optimalFitness > best.Fitness)
#
def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print(type(candidate.Genes))
    print("{0}\t{1}\t{2}".format(candidate.Genes, candidate.Fitness, str(timeDiff)))

def get_fitness(genes):
    fitness = 1
    gap = 0
    for i in range(1, len(genes)):
        if genes[i] > genes[i - 1]:
            fitness += 1
        else:
            gap += genes[i - 1] - genes[i]
    return Fitness(fitness, gap)


if __name__ == "__main__":
    unittest.main()
