import random, sys


# Number guessing game with unlimited turns

"""
print("\n I'm thinking of anumber between 1 and 2")
num = random.randint(1,10)
while True:
        print('\n take a guess: \n')
        userinput = int(input())
        if userinput < num:
            print("\ncYour number is too low! \n")
        elif userinput > num:
            print("\n Your number is too high! \n")        
        else:
              print('You won')
              break
"""        
    
# Number guessing game with only 5 turns

print("I'm thinking of a number")    
num = random.randint(1,10)
takes = 5
for guesses in range(1,6):
    if takes>1:
        print("You have", takes,  "takes. Take a guess: ")    
    else:
        print("It's your last take. Take a guess: ")    
    takes -= 1    
    userinput = int(input())
    if userinput > num:
      print("Your input is too high! ")
    elif userinput < num:      
      print("Your input is too low! ")
    else:
        print("Congrats You won!!")
        print('You guessed in',(guesses), ' attempts')
        break  
print("You lost, The number was", num)    