import random
moves = ['rock', 'paper', 'scissor']


class Player:
    round = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        b1 = (move1 == 'rock' and move2 == 'scissor')
        b2 = (move1 == 'scissor' and move2 == 'paper')
        b3 = (move1 == 'paper' and move2 == 'rock')
        B1 = (move2 == 'rock' and move1 == 'scissor')
        B2 = (move2 == 'scissor' and move1 == 'paper')
        B3 = (move2 == 'paper' and move1 == 'rock')
        boolean1 = b1 or b2 or b3
        boolean2 = B1 or B2 or B3
        boolean1 = str(boolean1)
        boolean2 = str(boolean2)
        if boolean1 == "True" and boolean2 == "False":
            self.p1.score2 = self.p1.score2+1
        elif boolean1 == "False" and boolean2 == "True":
            self.p2.score2 = self.p2.score2+1
        print(f"Player 1:{move1}  Player 2:{move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def single(self):
        print("Game started!")
        for round in range(1):
            print(f"Round {round}:")
            self.play_round()
            self.p1.round += 1
            s = self.p1.score2
            s2 = self.p2.score2
            print(f"Player1 score: {s}  Player2 score : {s2}")
        if self.p1.score2 > self.p2.score2:
            print("Congratulations you win ")
        elif self.p1.score2 < self.p2.score2:
            print("Game over!")
        elif self.p1.score2 == self.p2.score2:
            print("Tied game")

    def play_game(self):
        print("Game started!")
        for round in range(3):
            print(f"Round {round+1}:")
            self.play_round()
            self.p1.round += 1
            s = self.p1.score2
            s2 = self.p2.score2
            print(f"Player1 score: {s}  Player2 score : {s2}")
        if self.p1.score2 > self.p2.score2:
            print("Congratulations you win ")
        elif self.p1.score2 < self.p2.score2:
            print("Game over!")
        elif self.p1.score2 == self.p2.score2:
            print("Tied game")


class human_player(Player):
    score2 = 0

    def move(self):
        choice = input("Rock, Paper or Scissor ?")
        final_choice = choice.lower()
        self.Move = final_choice
        if final_choice == "rock":
            last_move = "Rock"
            return final_choice
        elif final_choice == "paper":
            last_move = "Paper"
            return final_choice
        elif final_choice == "scissor":
            last_move = "Scissor"
            return final_choice
        else:
            print("Invalid input .. Try again!!")
            choice = input("Enter again: ")
            choice = choice.lower()
            while (True):

                c1 = (choice == "rock")
                c2 = (choice == "paper")
                c3 = (choice == "scissor")
                if c1 or c2 or c3:
                    break
                else:
                    print("Invalid input .. Try again:")
                    choice = input("Enter again: ")
                    choice = choice.lower()
            return choice.lower()


class random_player(Player):
    score2 = 0

    def move(self):
        random_choice = random.choice(moves)
        return random_choice


class rock_player (Player):
    score2 = 0

    def move(self):
        return 'rock'


class reflect_player(Player):
    score2 = 0

    def learn(self, my_move, their_move):
        self.my_move = their_move
        return self.my_move

    def move(self):
        if self.round == 0:
            self.round += 1
            return random.choice(moves)
        else:
            return self.my_move


class cycle_player(Player):
    score2 = 0

    def learn(self, my_move, their_move):
        self.my_move = my_move
        if my_move == "rock":
            self.my_move = "paper"
            return self.my_move
        elif my_move == "paper":
            self.my_move = "scissor"
            return self.my_move
        elif my_move == "scissor":
            self.my_move = "rock"
            return self.my_move

    def move(self):
        if self.round == 0:
            self.round += 1
            return random.choice(moves)
        else:
            print(self.my_move)
            return self.my_move


def start_game():
    str1 = "Enter 1 to play with RockPlayer\n"
    str2 = "Enter 2 to play with RandomPlayer\n"
    str3 = "Enter 3 to play with ReflectPlayer\n"
    str4 = "Enter 4 to play with CyclePlayer\nEnter exit to quit\n"
    print(str1+str2+str3+str4)
    x = input("Enter your choice:")
    if 'exit' in x:
        print("Game finished")
    elif x == '1':
        game = Game(human_player(), rock_player())
        game.play_game()
    elif x == '2':
        game = Game(human_player(), random_player())
        game.play_game()
    elif x == '3':
        game = Game(human_player(), reflect_player())
        game.play_game()
    elif x == '4':
        game = Game(human_player(), cycle_player())
        game.play_game()
    else:
        print("Invalid Input!!")
        start_game()


def single_start_game():
    str1 = "Enter 1 to play with RockPlayer\n"
    str2 = "Enter 2 to play with RandomPlayer\n"
    str3 = "Enter 3 to play with ReflectPlayer\n"
    str4 = "Enter 4 to play with CyclePlayer\n Enter exit to quit\n"
    print(str1+str2+str3+str4)
    x = input(" Enter your choice:")
    if 'exit' in x:
        print("Game finished")
    elif x == '1':
        game = Game(human_player(), rock_player())
        game.single()
    elif x == '2':
        game = Game(human_player(), random_player())
        game.single()
    elif x == '3':
        game = Game(human_player(), reflect_player())
        game.single()
    elif x == '4':
        game = Game(human_player(), cycle_player())
        game.single()
    else:
        print("Invalid Input!!")
        single_start_game()


if __name__ == '__main__':
    x = input("Do u want to play single or multiple match?")
    if x == "single":
        single_start_game()
    elif x == "multiple":
        start_game()
    else:
        print("Invalid choice")
