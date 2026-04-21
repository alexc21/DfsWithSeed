import random


class Maze():
    def __init__(self) -> None:
        self.start = (1, 1)
        self.stack: list[tuple[int, int]] = [self.start]
        self.height = 40
        self.width = 40
        self.grid = []
        self.visited = set()
        self.valid = []

    def generate_grid(self):
        self.grid = [["@" for i in range(self.width)]
                     for i in range(self.height)]

    def generate_maze(self):
        self.grid[1][1] = "."
        while self.stack:
            self.visited.add(self.stack[-1])
            x, y = self.stack[-1]
            neighboor = [(x-2, y), (x + 2, y), (x, y - 2), (x, y + 2)]
            for n in neighboor:
                a, b = n
                if (0 <= a < self.width and
                    0 <= b < self.height and
                   (a, b) not in self.visited):
                    self.valid.append(n)
            if (self.valid):
                rv_coord = self.valid[random.randrange(0, len(self.valid))]
                r, v = rv_coord
                var1 = int((rv_coord[0] - x) / 2)
                var2 = int((rv_coord[1] - y) / 2)
                self.stack.append(rv_coord)
                self.visited.add(rv_coord)
                self.grid[y + var2][x + var1] = "."
                self.grid[v][r] = "."
            else:
                self.stack.pop()
            self.valid.clear()

    def display_grid(self):
        for cell in self.grid:
            print(" ".join(cell))


if __name__ == "__main__":
    maze = Maze()
    maze2 = Maze()
    random.seed(42)
    maze.generate_grid()
    maze.generate_maze()
    maze.display_grid()
    print()
    random.seed(42)
    maze2.generate_grid()
    maze2.generate_maze()
    maze2.display_grid()
