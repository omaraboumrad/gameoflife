import time
import curses
import signal

from life import Life

class TerminalLifePanel(object):
    def __init__(self, seed):
        self.seed = seed
        self.game = Life()
        self.screen = curses.initscr()
        self.running = True
        signal.signal(2, self.signal_closing)

    def signal_closing(self, signum, frame):
        self.running = False

    def main(self):
        self.screen.clear()
        
        self.draw_generation(self.seed)

        gen = self.game.next_gen(self.seed)

        while self.running:
            time.sleep(0.2)
            self.draw_generation(gen)
            gen = self.game.next_gen(gen) 


        self.screen.refresh()
        curses.endwin()

    def draw_generation(self, data):
        self.screen.clear()
        for j, row in enumerate(data):
            for i, col in enumerate(row):
                if col:
                    self.screen.addstr(j,i,'O')
                else:
                    self.screen.addstr(j,i,' ')
        self.screen.refresh()


