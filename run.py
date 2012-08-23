import sys
import platform
from gui import GuiLifePanel

if __name__ == '__main__':
    seed = [map(int,line.strip()) for line in open(sys.argv[1]).readlines()]
    kind = { 'gui' : GuiLifePanel }

    if platform.system() is not 'Windows':
        from terminal import TerminalLifePanel
        kind['term'] = TerminalLifePanel
        
    panel = kind[sys.argv[2]](seed).main()

