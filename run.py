import sys

from ui import TerminalLifePanel, GuiLifePanel

if __name__ == '__main__':
    seed = [map(int,line.strip()) for line in open(sys.argv[1]).readlines()]

    kind = { 'term' : TerminalLifePanel, 'gui' : GuiLifePanel }
    
    panel = kind[sys.argv[2]](seed).main()

