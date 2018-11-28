import datetime
import unittest
import random

import genetic

class Board:
    def __init__(self, genes, size):
        board = [['.'] * size for _ in range(size)]
        for index in range(0, len(genes), 2):
            r,c = genes[index + 0],genes[index + 1]
            board[r][c] = 'Q'
        self._board = board
    def print(self):
        # 0,0 prints in bottom left corner
        for i in reversed(range(0, len(self._board))):
            print(' '.join(self._board[i]))

class Fitness:
    NumberOfTakes = None

    def __init__(self, numberOfTakes):
        self.NumberOfTakes = numberOfTakes

    def __gt__(self, other):
        return self.NumberOfTakes < other.NumberOfTakes

    def __str__(self):
        return "{0} Number of takes".format(
            self.NumberOfTakes
        )

class QueenTests(unittest.TestCase):
    @staticmethod
    def test(size = 8):

        def fnGetFitness(genes):
            return get_fitness(genes)
        def fnDisplay(candidate):
            display(candidate, startTime)


        geneset = [i for i in range(size)]
        startTime = datetime.datetime.now()
        #genes = genetic._generate_parent(16, geneset, lambda x: 1).Genes
        #genes = [6,7,0,5,2,2,3,3,4,4,5,5,6,6,7,7]
        #a = Board(genes,8)
        #get_fitness(genes)
        #print(genes)
        #a.print()
        optimalFitness = Fitness(0)
        best = genetic.get_best(fnGetFitness, size * 2, optimalFitness, geneset, fnDisplay, None,None,10)
        #self.assertEqual(not optimalFitness > best.Fitness)

def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    board = Board(candidate.Genes, len(candidate.Genes)//2)

    #board.print()

    print(str(timeDiff))
    return
    print("{0}\t- {1}\t{2}".format(
        ' '.join(map(str, candidate.Genes)),
        candidate.Fitness,
        str(timeDiff)))


def get_fitness(genes):
    fitness = 0
    size = len(genes) // 2
    rows = [0] * size
    cols = [0] * size
    diags_1 = [0] * (2*size-1)
    diags_2 = [0] * (2*size-1)
    for index in range(0, len(genes), 2):
        r,c = genes[index + 0], genes[index + 1]
        rows[r] += 1
        cols[c] += 1
        diags_1[r+c] += 1
        diags_2[r-c] += 1
    fitness += sum(val*(val-1)//2 for val in rows)
    fitness += sum(val*(val-1)//2 for val in cols)
    fitness += sum(val*(val-1)//2 for val in diags_2)
    fitness += sum(val * (val - 1) // 2 for val in diags_1)
    #print(diags_1)
    #print(diags_2)
    return Fitness(fitness)


if __name__ == "__main__":
    #genetic.Benchmark.run(QueenTests.test)
    #unittest.main()
    QueenTests.test()
