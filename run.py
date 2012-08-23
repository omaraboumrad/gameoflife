import sys
from string import maketrans

from life import Life

(INTAB, OUTTAB) = ('10','# ')

def run(name):
    """ Runs the game on a seed provided by file [name] """
    seed = load(name)
    gen = Life().next_gen(seed)
    show(gen)

def load(name):
    """ Loads seed from file [name] """
    return [map(int,str(line.strip())) for line in open(name).readlines()]

def show(array):
    """ Makes array matrix into \n delimited string, translates based on tabs """
    transtab = maketrans(INTAB, OUTTAB)
    print '\n'.join(''.join(map(str,a)) for a in array).translate(transtab)

if __name__ == '__main__':
    run(sys.argv[1])
