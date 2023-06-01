
# "S" - start
# "E" - end
# "#" - wall
# "." - empty space
# "x" - visited space
# "*" - solution path
class Labyrinth:

    def __init__(self, filename):
        self._labyrinth = self.load_labyrinth(filename)
        self._solution = None
        self.wall = "#"
        self.empty_space = " "
        self.start = "S"
        self.end = "E"
        self.route = "*"

    def load_labyrinth(self, filename):
        labyrinth = []
        with open(filename, 'r') as file:
            for line in file:
                row = [char for char in line.strip()]
                labyrinth.append(row)
        return labyrinth

    def show(self, show_solution=False):
        labyrinth_str = ""
        if show_solution and self._solution is not None:
            labyrinth_with_solution = [row.copy() for row in self._labyrinth]
            for x, y in self._solution:
                labyrinth_with_solution[y][x] = self.route
            for row in labyrinth_with_solution:
                print(' '.join(row))
                labyrinth_str += ' '.join(row) + '\n'
        else:
            for row in self._labyrinth:
                labyrinth_str += ' '.join(row) + '\n'
                print(' '.join(row))
        return labyrinth_str

    def solve(self):
        start_x, start_y = self.find_start_position()
        end_x, end_y = self.find_end_position()
        visited = set()
        self._solution = self.shortest_path(
            start_x, start_y, end_x, end_y, visited)
        return self._solution

    def find_start_position(self):
        for y, row in enumerate(self._labyrinth):
            for x, char in enumerate(row):
                if char == self.start:
                    return x, y
        raise ValueError("Start position not found in the labyrinth.")

    def find_end_position(self):
        for y, row in enumerate(self._labyrinth):
            for x, char in enumerate(row):
                if char == self.end:
                    return x, y
        raise ValueError("End position not found in the labyrinth.")

    def shortest_path(self, x, y, end_x, end_y, visited):
        if x == end_x and y == end_y:
            return [(x, y)]

        if (x, y) in visited:
            return None

        visited.add((x, y))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if self.validate_postion(new_x, new_y):
                path = self.shortest_path(
                    new_x, new_y, end_x, end_y, visited)
                if path is not None:
                    path.append((x, y))
                    return path

        return None

    def validate_postion(self, x, y):
        if 0 <= x < len(self._labyrinth[0]) and 0 <= y < len(self._labyrinth):
            return self._labyrinth[y][x] != self.wall
        return False

    @property
    def solution(self):
        return self._solution.copy() if self._solution is not None else None


# data = Labyrinth("labyrinth.txt")
# data.show()
# data.solve()
# data.show(show_solution=True)
# print(data.solution)
