# Simple Python program for a snake game with colorama
# install colorama 

import random
import os
import time
import msvcrt
from colorama import init, Fore

init(autoreset=True)

class SnakeGame:
    def __init__(self):
        self.board_size = [15, 25]
        self.snake_position = [[5, 5], [5, 4], [5, 3]]
        self.direction = 'd'
        self.apple_position = self.generate_apple_position()
        self.score = 0
        self.game_over = False
        self.user_response_speed = 0.1
        self.snake_speed = 0.2

    def generate_apple_position(self):
        while True:
            position = [random.randint(1, self.board_size[0] - 2), random.randint(1, self.board_size[1] - 2)]
            if position not in self.snake_position:
                return position

    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Controls:")
        print("- Press 'w' to move up")
        print("- Press 's' to move down")
        print("- Press 'a' to move left")
        print("- Press 'd' to move right")
        print("- Press 'q' to quit\n")

        print(f"Score: {self.score}\n")

        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                if i == 0 or i == self.board_size[0] - 1 or j == 0 or j == self.board_size[1] - 1:
                    print(Fore.YELLOW + " █ ", end="")
                elif [i, j] in self.snake_position:
                    if [i, j] == self.snake_position[0]:
                        print(Fore.GREEN + " ⦿ ", end="")
                    else:
                        print(Fore.GREEN + " ● ", end="")
                elif i == self.apple_position[0] and j == self.apple_position[1]:
                    print(Fore.RED + " 🍎 ", end="")
                else:
                    print("   ", end="")
            print()

    def get_user_input(self):
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'w':
                self.direction = 'w'
            elif key == 's':
                self.direction = 's'
            elif key == 'a':
                self.direction = 'a'
            elif key == 'd':
                self.direction = 'd'
            elif key == 'q':
                self.game_over = True

    def check_collision(self):
        head = self.snake_position[0].copy()

        if self.direction == 'w':
            head[0] -= 1
        elif self.direction == 's':
            head[0] += 1
        elif self.direction == 'a':
            head[1] -= 1
        elif self.direction == 'd':
            head[1] += 1

        if head == self.apple_position:
            self.score += 1
            self.snake_position.insert(0, head)
            self.apple_position = self.generate_apple_position()
        else:
            self.snake_position.insert(0, head)
            self.snake_position.pop()

        if (
            head in self.snake_position[1:] or
            head[0] <= 0 or head[0] >= self.board_size[0] - 1 or
            head[1] <= 0 or head[1] >= self.board_size[1] - 1
        ):
            self.game_over = True
            print(Fore.RED + "\nGame Over! You hit the wall or yourself.")
            self.display_scorecard()

    def display_scorecard(self):
        print("\n" + Fore.CYAN + "-------- Scorecard --------")
        print(Fore.MAGENTA + f"🎉 Congratulations! You scored {self.score} points. 🎉")
        if self.score >= 10:
            print(Fore.GREEN + "👑 Great job! You're a Snake Master! 👑")
        elif self.score >= 5:
            print(Fore.YELLOW + "🌟 Well done! You're becoming a skilled snake player. 🌟")
        else:
            print(Fore.RED + "💪 Keep practicing! You'll improve with time. 💪")
        print("---------------------------")

    def play_game(self):
        input("Press a key to start...")

        while not self.game_over:
            self.display_board()
            self.get_user_input()
            self.check_collision()

            time.sleep(self.snake_speed)

def main():
    print(Fore.CYAN + "Welcome to Snake Game!\n")

    snake_game = SnakeGame()
    snake_game.play_game()

if __name__ == "__main__":
    main()
