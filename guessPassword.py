import datetime
import genetic
import random


class TestGuessPassword():
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"

    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_For_I_am_fearfully_and_wonderfully_made(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)

    def test_Random(self):
        length = 100
        target = ''.join(random.choice(self.geneset) for _ in range(length))
        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Random)

    def guess_password(self, target):
        startTime = datetime.datetime.now()
        def fnGetFitness(genes):
            return get_fitness(genes, target)
        def fnDisplay(candidate):
            display(candidate, startTime)
        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset,fnDisplay)
        assert ''.join(best.Genes) == target

def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(''.join(candidate.Genes), candidate.Fitness, str(timeDiff)))

def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)
