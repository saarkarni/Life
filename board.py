class Board:

    def __init__(self, size):
        self.size = size
        self.board = {}
        self.alive_neighbors = {}

        for i in range(self.size):
            for j in range(self.size):
                self.board[(i, j)] = 0
                self.alive_neighbors[(i, j)] = 0

    def print(self, current_generation):
        print("Game State - Generation #" + str(current_generation) + ":\n")
        for i in range(self.size):
            for j in range(self.size):
                if self.board[(i, j)] == 0:
                    print("_", end=" ")
                else:
                    print("x", end=" ")
            print("\n")

    def get_cell_status(self, row, col):
        return self.board[(row, col)]

    def reset_num_of_neighbors(self):
        for i in range(self.size):
            for j in range(self.size):
                self.alive_neighbors[(i, j)] = 0

    def revive_cell(self, row, col):
        self.board[(row, col)] = 1

    def kill_cell(self, row, col):
        self.board[(row, col)] = 0

    def get_neighbors(self, row, col):

        neighbors = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
        neighbors_to_remove = []

        for neighbor in neighbors:
            if neighbor[0] < 0 or neighbor[0] > self.size-1 or neighbor[1] < 0 or neighbor[1] > self.size-1:
                neighbors_to_remove.append(neighbor)

        return [item for item in neighbors if item not in neighbors_to_remove]

    def calc_alive_neighbors(self, row, col):

        neighbors = self.get_neighbors(row, col)
        for neighbor in neighbors:
            self.alive_neighbors[(row, col)] += self.board[(neighbor[0], neighbor[1])]
