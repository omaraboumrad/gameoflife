import sys
import numpy

(ALIVE, DEAD) = ('#','_')

def run(name):
    seed = load(name)
    gen = next_gen(seed)
    show(gen)

def load(name):
    array = []
    for line in open(name):
        row = []
        for column in line.strip():
            row.append(int(column))
        array.append(row)
    return numpy.array(array)

def show(array):
    for line in array:
        replace_living = ''.join(map(str,line)).replace('1',ALIVE)
        replace_dead = ''.join(replace_living).replace('0',DEAD)
        print replace_dead

def next_gen(array):
    new_gen = []
    hack_array = array[1:-1,1:-1] # temp hack until edges are solved
    for j,row in enumerate(hack_array):
        new_gen_row = []
        for i,column in enumerate(row):
            successor = get_successor(array[j:j+3,i:i+3])
            new_gen_row.append(successor)
        new_gen.append(new_gen_row)
    return new_gen

def get_successor(m):
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

if __name__ == '__main__':
    run(sys.argv[1])
