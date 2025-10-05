class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.goal = (width - 1, height - 1)
        self.obstacles = self.generate_obstacles()

    def generate_obstacles(self):
        obstacles = set()
        for _ in range((self.width * self.height) // 5):  # 20% of the grid as obstacles
            obstacle = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if obstacle != (0, 0) and obstacle != self.goal:
                obstacles.add(obstacle)
        return obstacles

    def is_obstacle(self, position):
        return position in self.obstacles

    def is_within_bounds(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def is_goal_reached(self, position):
        return position == self.goal

    def print_map(self, player_position, ai_position):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == player_position:
                    print("P", end=" ")
                elif (x, y) == ai_position:
                    print("A", end=" ")
                elif (x, y) == self.goal:
                    print("G", end=" ")
                elif (x, y) in self.obstacles:
                    print("X", end=" ")
                else:
                    print(".", end=" ")
            print()
