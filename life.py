from board import Board


class Game:

    def __init__(self, size, alive_cells):
        self.size = size
        self.current_generation = 0
        self.board = Board(self.size)
        for cell in alive_cells:
            self.board.revive_cell(cell[0], cell[1])

    def play(self, num_of_generations):
        for i in range(num_of_generations):
            self.board.print(self.current_generation)
            self.calculate_next_generation()
            self.current_generation += 1

    def calculate_next_generation(self):

        self.board.reset_num_of_neighbors()

        for i in range(self.size):
            for j in range(self.size):
                self.board.calc_alive_neighbors(i, j)

        for i in range(self.size):
            for j in range(self.size):

                if self.board.get_cell_status(i, j) == 1 and self.board.alive_neighbors[(i, j)] < 2:
                    self.board.kill_cell(i, j)

                elif self.board.get_cell_status(i, j) == 1 and self.board.alive_neighbors[(i, j)] > 3:
                    self.board.kill_cell(i, j)

                elif self.board.get_cell_status(i, j) == 0 and self.board.alive_neighbors[(i, j)] == 3:
                    self.board.revive_cell(i, j)


game = Game(30, [(15,10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15), (15, 16), (15, 17), (15, 18), (15, 19)])
game.play(16)
