import random
from player import Player
from game_map import GameMap
from ai import AStarAI

def main():
    width, height = 10, 10  # Size of the game map
    game_map = GameMap(width, height)
    player = Player(game_map)
    ai = AStarAI(game_map)

    while not game_map.is_goal_reached(player.position):
        game_map.print_map(player.position, ai.position)
        
        # Player's move
        move = input("Enter your move (WASD): ").upper()
        player.move(move)
        
        # AI's move
        ai.move_towards_goal()

        print()

    print("Congratulations! You've reached the goal!")

if __name__ == "__main__":
    main()
