import sys

from life import LifePanel

if __name__ == '__main__':
    seed = [map(int,line.strip()) for line in open(sys.argv[1]).readlines()]
    panel = LifePanel(seed).main()

