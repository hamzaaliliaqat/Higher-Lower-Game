from art import logo
from art import vs
from game_data import data
import random
import os

def format_data(account):
  """ Format the account data into a printable format """
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}: a {account_description} from {account_country}"

def check_answer(guess, a_follower_count,  b_follower_count):
  """Take the user guess and follower counts and returns if the answer is true or not"""
  if a_follower_count >  b_follower_count:
    return guess == "a"
  else:
    return guess == "b"

#display art
print(logo)

score = 0
should_game_continue = True
account_b = random.choice(data)

#to clear the screen
clear = lambda: os.system('clear')

#make the game repeatable
while should_game_continue:
  #generate a random account from data
  #convert previous b into a
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")

  #ask user for a guess
  guess = input("Who has more followers? A or B: ").lower()

  #check if user is corrrect
  #check number of followers
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  #clear the screen
  clear()
  print(logo)

  #give feedback to user
  if is_correct:
    score += 1
    print(f"You are right!. Current score is {score}.")
  else:
    should_game_continue = False
    print(f"Sorry, that's wrong. Your score is {score}")