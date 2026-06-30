import random


class Maze():
    def __init__(self, width, height) -> None:
        self.cell_width = width
        self.cell_height = height
        self.start = (0, 0)
        self.stack: list[tuple[int, int]] = [self.start]
        self.height = self.cell_height * 2 + 1
        self.width = self.cell_width * 2 + 1
        self.grid = []
        self.visited = set()
        self.valid = []

    def generate_grid(self):
        self.grid = [["M" for i in range(self.width)]
                     for i in range(self.height)]
        self.grid[1][1] = "."

    def generate_maze(self):
        while self.stack:
            self.visited.add(self.stack[-1])
            cx, cy = self.stack[-1]
            neighboor = [(cx + 1, cy), (cx - 1, cy),
                         (cx, cy + 1), (cx, cy - 1)]
            for n in neighboor:
                a, b = n
                if (0 <= a < self.cell_width and
                    0 <= b < self.cell_height and
                   (a, b) not in self.visited and
                   self.grid[a][b] != 0):
                    self.valid.append(n)
            if self.valid:
                nx, ny = random.choice(self.valid)
                cx, cy = self.stack[-1]
                self.stack.append((nx, ny))
                self.visited.add((nx, ny))
                self.grid[ny * 2 + 1][nx * 2 + 1] = "."
                self.grid[cy * 2 + 1][cx * 2 + 1] = "."
                wall_x = cx + nx + 1
                wall_y = cy + ny + 1
                self.grid[wall_y][wall_x] = "."
            else:
                self.stack.pop()
            self.valid.clear()

    def display_grid(self):
        for cell in self.grid:
            print(" ".join(cell))




if __name__ == "__main__":
    maze = Maze(10, 10)
    # random.seed(42)
    maze.generate_grid()
    maze.generate_maze()
    maze.display_grid()
    