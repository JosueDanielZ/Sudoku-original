class Cuerpo():
    def __init__(self):
        self.cuerpo_s = []

    def iniciar_cuerpo(self):
        self.cuerpo_s = [[0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]]
    
    def recorrer_sudoku(self):
        for filas in self.cuerpo_s:
            print(filas)

cuerpo_sudoku = Cuerpo()
cuerpo_sudoku.iniciar_cuerpo()
cuerpo_sudoku.recorrer_sudoku()


