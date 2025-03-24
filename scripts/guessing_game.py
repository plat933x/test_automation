import random

winning_number = random.randint(1,500)
counter = 10

user_input = 0

while user_input != winning_number:
    if counter > 0:
      user_input = int(input("Please provide number between 1 and 500: "))
      counter -= 1

      if user_input == winning_number:
          print("Congratz! You won the lottery with number: ", winning_number)
          break

      elif user_input < winning_number:
          print(f"Provide number bigger than {user_input}.")
      else:
          print(f"Provide number smaller than {user_input}.")
    else:
      print("No more shots left! The number was: ", winning_number)
      break
    print("Shoots left: ", counter)