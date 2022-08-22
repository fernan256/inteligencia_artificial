import argparse
from puzzle_operations import Puzzle
import utils as Utils

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", '--cols',
                          help='cantidad de columnas')
    parser.add_argument("-r", '--rows',
                          help='cantidad de filas')
    parser.add_argument("-nmax", '--maxNumber',
                          help='entero indica cantidad de veces a desordenar')     
    parser.add_argument("-ra", '--random',
                          help='resolver de forma random', action='store_true')
    parser.add_argument("-ba", '--breadth',
                          help='resolver usando busqueda en anchura', action='store_true')
    parser.add_argument("-bd", '--bidireccional',
                          help='resolver usando busqueda bidireccional', action='store_true')           
    args = parser.parse_args()
    cols = args.cols
    rows = args.rows
    puzzle = Puzzle(int(cols),int(rows))
    randomMatrix = puzzle.mixMatrix()
    do_random_search = args.random
    do_breadth_search = args.breadth
    max_movements = args.maxNumber
    max_movemnets_to_send = 0     
    if do_random_search:
        randomSolution, numberOfMovements = puzzle.randomSolve(randomMatrix)
        print("------------- Resultado -------------")
        if max_movements:
            max_movemnets_to_send = int(max_movements)
        Utils.represent_board(randomMatrix, max_movemnets_to_send)
        Utils.represent_board(randomSolution, numberOfMovements)

    elif do_breadth_search:
        randomSolution, numberOfMovements = puzzle.busquedaEnAnchura(randomMatrix)
        print("------------- Resultado -------------")
        if max_movements:
            max_movemnets_to_send = int(max_movements)
        Utils.represent_board(randomMatrix, max_movemnets_to_send)
        Utils.represent_board(randomSolution, numberOfMovements)
