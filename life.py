class Life(object):
    def next_gen(self, array):
        new_gen = []
        for j,row in enumerate(array):
            new_gen_row = []
            for i,column in enumerate(row):
                successor = self.get_successor(array, j, i, len(array), len(row))
                new_gen_row.append(successor)
            new_gen.append(new_gen_row)
        return new_gen

    def get_successor(self, array, j, i, h, w):
        alive = array[j][i]
        lmi = lambda x: 0 if x < 0 else x
        lma = lambda x, m: m-1 if x == m else x
        living_cells = sum((
            sum(array[lmi(j-1)   ][lmi(i-1):lma(i+2, w)]),
            sum(array[j          ][lmi(i-1):lma(i+2, w)]),
            sum(array[lma(j+1, h)][lmi(i-1):lma(i+2, w)]))) - alive

        return 1 if (alive and living_cells in (2,3)) or \
                    (not alive and living_cells == 3) else 0


          
