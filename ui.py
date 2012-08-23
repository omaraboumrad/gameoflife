import time

from life import Life

# Terminal
import curses

class TerminalLifePanel(object):
    def __init__(self, seed):
        self.seed = seed
        self.game = Life()
        self.screen = curses.initscr()

    def main(self):
        self.screen.clear()
        
        self.draw_generation(self.seed)

        gen = self.game.next_gen(self.seed)

        while True:
            time.sleep(0.2)
            self.draw_generation(gen)
            gen = self.game.next_gen(gen) 


        self.screen.refresh()
        self.screen.getch()
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

# Gui
import Tkinter

class GuiLifePanel(object):
    def __init__(self, seed):
        self.seed = seed
        self.current = None 
        self.game = Life()
        self.top = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(self.top, bg='white', height=500, width=500)
        self.main()
        self.canvas.pack()
        self.top.mainloop()
        
    def main(self):
        self.canvas.delete(Tkinter.ALL)
        if not self.current:
            self.draw_generation(self.seed)
            self.current= self.game.next_gen(self.seed)
        else:
            self.draw_generation(self.current)
            self.current = self.game.next_gen(self.current)

        self.top.after(100, self.main)



    def draw_generation(self, data):
        rec_size = 20
        start_x = 10
        start_y = 10
        for j, row in enumerate(data):
            for i, col in enumerate(row):
                if col:
                    self.canvas.create_rectangle(
                        i*start_x, 
                        j*start_y, 
                        i*start_x+rec_size, 
                        j*start_y+rec_size, 
                        fill='black', width=0)   
                else:
                    self.canvas.create_rectangle(
                        i*start_x, 
                        j*start_y, 
                        i*start_x+rec_size, 
                        j*start_y+rec_size, 
                        fill='white', width=0)   









