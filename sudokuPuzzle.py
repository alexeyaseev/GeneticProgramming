import unittest
import datetime
import genetic
import random
import statistics


def get_fitness(_genes):
    size = _genes[-1]
    block_size = _genes[-2]
    genes = _genes[:-2]
    rows = []
    cols = []
    blocks = []
    for k in range(size):
        rows.append(genes[size*k:size*k+size])
        cols.append(genes[k::size])
    for k in range(size):
        blocks.append([])
        for i in range(block_size):
            blocks[-1].extend(rows[block_size*(k // block_size) + i]
                                  [block_size* (k % block_size):block_size* (k % block_size) + block_size])
    numDistinct_Rows = sum(len(set(row)) for row in rows)
    numDistinct_Cols = sum(len(set(col)) for col in cols)
    numDistinct_Blocks = sum(len(set(block)) for block in blocks)
    return Fitness(numDistinct_Rows, numDistinct_Cols, numDistinct_Blocks)


class Fitness:
    NumDistinct_Rows = None
    NumDistinct_Cols = None
    NumDistinct_Blocks = None
    def __init__(self, numDistinct_Rows, numDistinct_Cols, numDistinct_Blocks):
        self.NumDistinct_Rows = numDistinct_Rows
        self.NumDistinct_Cols = numDistinct_Cols
        self.NumDistinct_Blocks = numDistinct_Blocks
    def __gt__(self, other):
        return self.get_fitness() > other.get_fitness()
    def get_fitness(self):
        return 1*self.NumDistinct_Rows + 1*self.NumDistinct_Cols + 1*self.NumDistinct_Blocks
        #return min(self.NumDistinct_Rows,self.NumDistinct_Cols,self.NumDistinct_Blocs)
        #return self.NumDistinct_Rows + self.NumDistinct_Cols + self.NumDistinct_Blocks - statistics.stdev([self.NumDistinct_Rows,self.NumDistinct_Cols,self.NumDistinct_Blocks])
    def __str__(self):
        return "rows_num_distinct: {0} cols_num_distinct: {1} blocks_num_distinct: {2}".format(
            self.NumDistinct_Rows,
            self.NumDistinct_Cols,
            self.NumDistinct_Blocks)

def create(size, block_size):
    genes = [val+1 for digit in range(size) for val in [digit]*size]
    random.shuffle(genes)
    genes += [block_size, size]
    return genes

# def add(genes, items, maxWeight, maxVolume):
#     usedItems = {iq.Item for iq in genes}
#     item = random.choice(items)
#     while item in usedItems:
#         item = random.choice(items)
#     maxQuantity = max_quantity(item, maxWeight, maxVolume)
#     return ItemQuantity(item, maxQuantity) if maxQuantity > 0 else None
#

def mutate(genes):
    indexes = range(genes[-1]**2)
    indexA, indexB = random.sample(indexes, 2)
    genes[indexA], genes[indexB] = genes[indexB], genes[indexA]
    # indexA, indexB = random.sample(indexes, 2)
    # genes[indexA], genes[indexB] = genes[indexB], genes[indexA]
    # indexA, indexB = random.sample(indexes, 2)
    # genes[indexA], genes[indexB] = genes[indexB], genes[indexA]

def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    genes = candidate.Genes[:]
    size = genes[-1]
    for k in range(size):
         print(genes[k*size:k*size+size])
    print("{0}\t{1}".format(candidate.Fitness, str(timeDiff)))

class SudokuTests(unittest.TestCase):
    def test_9x9(self):
        size = 100
        block_size = 10
        num_blocks = (size // block_size)**2
        optimal = Fitness(size**2, size**2, num_blocks * (block_size**2))
        self.new_sudoku_game(size, block_size, optimal)

    def _test_4x4(self):
        size = 4
        block_size = 2
        num_blocks = (size // block_size)**2
        optimal = Fitness(size**2, size**2, num_blocks * (block_size**2))
        self.new_sudoku_game(size, block_size, optimal)

    def new_sudoku_game(self, size, block_size, optimalFitness):
        startTime = datetime.datetime.now()

        def fnDisplay(candidate):
            display(candidate, startTime)
        def fnGetFitness(genes):
            return get_fitness(genes)
        def fnCreate():
            return create(size, block_size)
        def fnMutate(genes):
            mutate(genes)
        #
        best = genetic.get_best(fnGetFitness, None, optimalFitness, None, fnDisplay, fnMutate, fnCreate)#, maxAge=2500)
        # self.assertTrue(not optimalFitness > best.Fitness)

# size = 4
# block_size = 2
# random.seed(0)
# genes = create(size, block_size)
# genes = []
# size = 9
# block_size = 3
# genes = [val+1 for digit in range(block_size**2) for val in [digit]*size]
# random.shuffle(genes)
# genes += [3,9]
# for k in range(size):
#     print(genes[k*size:k*size+size])
# print(get_fitness(genes))

# for _ in range(size**2):
#     genes.append(random.randint(1,block_size**2))
# print(genes)

unittest.main()
