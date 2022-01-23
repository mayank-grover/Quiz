import random

optionList = []

class Question:
  def __init__(self, question, options, answer):
    self.question = question
    self.options = options
    self.answer = answer
  def askQuestion(self):
    print(self.question + "\n")
    random.shuffle(self.options)
    for i in self.options:
      print(i)
  
    userChoice = input("\n" + "What is your answer?")

    if userChoice == self.answer:
      print("Correct!")
      return True
    else:
      print("Incorrect")
      return False

x = Question("What is your favourite food?", ["burger", "noodles", "brownie", "pizza"], "pizza")
x.askQuestion()