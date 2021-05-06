# random module to generate a random number from a range
import random

name = ""

question = "Will I win the lottery?"

answer = ""

random_number = random.randint(1,9) # randint function to generate random number
# will generate a random number between 1 (inclusive) and 9 (inclusive)

#print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"


if not question:
  print("What is your question?")
else:
  if not name:
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
  else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)