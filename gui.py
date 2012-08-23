import time
import Tkinter
import signal

from life import Life

class GuiLifePanel(object):
    def __init__(self, seed):
        self.seed = seed
        self.current = None 
        self.game = Life()
        self.top = Tkinter.Tk()
        self.top.protocol('WM_DELETE_WINDOW', self.window_closing)
        signal.signal(2, self.signal_closing)
        self.canvas = Tkinter.Canvas(self.top, bg='white', height=500, width=500)
        self.main()
        self.canvas.pack()
        self.top.mainloop()

    def window_closing(self):
        self.top.quit()
        
    def signal_closing(self, signum, frame):
        self.top.quit()

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

