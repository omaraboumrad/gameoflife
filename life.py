import numpy

class Life(object):
    def next_gen(self, array):
        """ Iterates over cells, gets successor, populates new generation """
        array = numpy.array(array)
        new_gen = []
        hack_array = array[1:-1,1:-1] # temp hack until edges are solved
        for j,row in enumerate(hack_array):
            new_gen_row = []
            for i,column in enumerate(row):
                successor = self.get_successor(array[j:j+3,i:i+3])
                new_gen_row.append(successor)
            new_gen.append(new_gen_row)
        return new_gen

    def get_successor(self, m):
        """ Retrieves the successor of m[1,1] """
        is_alive = m[1,1]
        living_cells = m.sum()-is_alive

        # Any dead cell with exactly three live neighbours becomes a live cell.
        if not is_alive and living_cells == 3:
            return 1
        
        # Any live cell with fewer than two live neighbours dies.
        if is_alive and living_cells < 2:
            return 0

        # Any live cell with two or three live neighbors, lives on.
        if is_alive and living_cells in (2,3):
            return 1

        # Any live cell with more than three live neighbours, dies.
        if is_alive and living_cells > 3:
            return 0

        return 0

