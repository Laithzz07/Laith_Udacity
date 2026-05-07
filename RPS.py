import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        pass

    def learn(self, my_move, other_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.enemy_choice = random.choice(moves)

    def move(self):
        return self.enemy_choice

    def learn(self, my_move, other_move):
        self.enemy_choice = other_move


class CyclePlayer(Player):
    def __init__(self):
        self.last_choice = random.choice(moves)

    def move(self):
        if self.last_choice == 'rock':
            return 'paper'
        elif self.last_choice == 'paper':
            return 'scissors'
        else:
            return 'rock'

    def learn(self, my_move, other_move):
        self.last_choice = my_move


class HumanPlayer(Player):
    def move(self):
        while True:
            user_choice = input(
                "Enter rock, paper, scissors or quit: "
            ).lower()

            if user_choice == 'quit':
                return user_choice

            if user_choice in moves:
                return user_choice

            print("Invalid input. Try again.")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2
        self.score1 = 0
        self.score2 = 0
        self.rounds = 1

    def play_round(self):
        print("\nRound", self.rounds)

        move1 = self.player1.move()

        if move1 == 'quit':
            return False

        move2 = self.player2.move()

        print("Player 1:", move1)
        print("Player 2:", move2)

        if move1 == move2:
            print("It's a tie!")

        elif beats(move1, move2):
            print("Player 1 wins this round!")
            self.score1 += 1

        else:
            print("Player 2 wins this round!")
            self.score2 += 1

        print(
            "\nYOUR score:",
            self.score1,
            "||||",
            self.score2,
            "ENEMY score"
        )

        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)

        self.rounds += 1
        return True

    def play_game(self):
        print("Game start!")

        while True:
            again = self.play_round()

            if again is False:
                break

        print("\nGame over")
        print("Final score:", self.score1, self.score2)

        if self.score1 > self.score2:
            print("YOU are the winner!")

        elif self.score2 > self.score1:
            print("Player 2 is the winner!")

        else:
            print("It's a draw!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
