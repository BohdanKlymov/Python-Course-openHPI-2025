# You probably know the game "Rock, Paper, Scissors". 
# A game for two players. Each player has three options, namely rock, paper, scissors, which are formed by the player's hand. 
# The rules are quite easy:

#     - rock beats scissors
#     - scissors beats paper
#     - paper beats rock.

# If both players have chosen the same object, it's a draw.

# In the following, we play 100 consecutive games. 
# Each player has to hand in a file consisting of one letter per line. The letters are either "R", "P" or "S".

# Write a Python program that reads two files player1.txt and player2.txt. 
# These files are organized according to the above rules. 
# The program should compare both inputs and calculate how many games have been won by player1, 
# by player2 and how many games ended in a draw. The results are written into a file result.txt which looks as follows:

# Player1 wins: 23
# Player2 wins: 48
# Draws: 29

# The sum should always be 100.


with open("player1.txt", "r") as f1:
    player1_moves = [line.strip() for line in f1]

with open("player2.txt", "r") as f2:
    player2_moves = [line.strip() for line in f2]

p1_wins = 0
p2_wins = 0
draws = 0

for m1, m2 in zip(player1_moves, player2_moves):
    if m1 == m2:
        draws += 1
    elif (m1 == "R" and m2 == "S") or (m1 == "S" and m2 == "P") or (m1 == "P" and m2 == "R"):
        p1_wins += 1
    else:
        p2_wins += 1

with open("result.txt", "w") as result_file:
    result_file.write(f"Player1 wins: {p1_wins}\n")
    result_file.write(f"Player2 wins: {p2_wins}\n")
    result_file.write(f"Draws: {draws}\n")