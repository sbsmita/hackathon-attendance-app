import random


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self):
        self.score += 1

    def __str__(self):
        return self.name

def game(player):
    answer = []
    index = 0
    print(f"Welcome {player.name} to two choos and a lie !")
    print("Enter two fun facts about you? \n ")

    while len(answer) < 2:
        fact = input(f"Fact {index + 1} :")
        answer.append(fact)
        index += 1


    lie = ai_generate_lie()
    answer.append(lie)
    

    print("\nHere are the statements:")
    for i, statement in enumerate(answer):
        print(f"{i + 1}. {statement} \n")


    guess = int(input("Which statement is a lie? "))
    while guess != answer[guess -1]:
        print("That is incorrect please guess again:\n")
        guess = int(input("Which statement is a lie? "))

        if answer[guess - 1] == lie:
            print("You are correct!")
            player.add_score()
            break
     

def generate_pictures(questions):
    for item in range(0, len(questions) -1):
        print(questions[item])

def ai_generate_lie():
    lie = "I hate Hackathons"
    return lie

def test_player():
    player = Player("Alice")
    player.add_score()
    print(player.score)
    game(player)

test_player()