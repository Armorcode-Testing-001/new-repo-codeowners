class Player:
    def __init__(self, game_map):
        self.position = (0, 0)
        self.game_map = game_map

    def move(self, direction):
        x, y = self.position
        if direction == 'W':  # Up
            new_pos = (x, y - 1)
        elif direction == 'S':  # Down
            new_pos = (x, y + 1)
        elif direction == 'A':  # Left
            new_pos = (x - 1, y)
        elif direction == 'D':  # Right
            new_pos = (x + 1, y)
        else:
            print("Invalid move!")
            return

        if self.game_map.is_within_bounds(new_pos) and not self.game_map.is_obstacle(new_pos):
            self.position = new_pos
        else:
            print("Move blocked!")
