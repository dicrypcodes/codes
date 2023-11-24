x = "my name is daniel"
y = " left coding for a little while"
z = " but i am back and stronger now!"
print(x + y + z)


def classifier(identify):
    return lambda age : identify + age

description = classifier("my name is ")
print(description("19"))
 
import random
def new_code():
   Teacher = input( "Introduce yourself : ")
   options = ["Daniel", "Afolabi", "Adeola", "Marley"]
   student_name = random.choice(options)
   response = {"Teachers": Teacher, "Student": student_name}
   
   if student_name == "Daniel":
     return "my name is " + "Daniel"
   elif student_name == "Afolabi":
      return "my name is " + "Afolabi"    
   elif student_name == "Adeola":
      return "my name is " + "Adeola"
   else:
      return "my name is " + "Marley"
   print(response)
new_code()

"""import random
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors:")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
get_choices()

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "it's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! you win!"
        else:
            return "Paper smashes scissors! you lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! you win!"
        else:
            return "Rock smashes scissors! you lose."
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)


        """