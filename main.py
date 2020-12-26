from random import randint

boys_names_file = open("lists/boys_names.txt", "r")
girls_names_file = open("lists/girls_names.txt", "r")
items_file = open("lists/items.txt", "r")

boys_names = boys_names_file.readlines()
girls_names = girls_names_file.readlines()
objects = items_file.readlines()
types = ["+","-","x"]
times = ["month", "day", "week", "year"]

random_boy = boys_names[randint(0, 59)].capitalize()
random_girl = girls_names[randint(0, 59)].capitalize()

random_boy2 = boys_names[randint(0, 59)].capitalize()
random_girl2 = girls_names[randint(0, 59)].capitalize()

rand_item = objects[randint(0, 39)].rstrip("\n")
random_type = types[randint(0, 2)]
boys_or_girls = randint(0, 1)
boys_or_girls2 = randint(0, 1)
random_time = times[randint(0, 3)]

def generate_word_problem(difficulty):
  word_problem = ""
  num1 = 0
  num2 = 0
  
  if difficulty == 1:
    num1 += randint(1, 20)
    num2 += randint(1, 20)
  elif difficulty == 2:
    num1 += randint(20, 60)
    num2 += randint(20, 60)
  elif difficulty == 3:
    num1 += randint(60, 200)
    num2 += randint(60, 200)
  elif difficulty == 4:
    num1 += randint(200, 800)
    num2 += randint(200, 800)
  elif difficulty == 5:
    num1 += randint(800, 4000)
    num2 += randint(800, 4000)
  
  if boys_or_girls == 0:
    word_problem += random_boy.rstrip("\n")
  elif boys_or_girls == 1:
    word_problem += random_girl.rstrip("\n")
  
  word_problem += f" has {num1} {rand_item}."
  
  if boys_or_girls == 0:
    word_problem += " He"
  elif boys_or_girls == 1:
    word_problem += " She"
    
  if random_type == "+":
    word_problem += f" receives {num2} from "
    
    if boys_or_girls2 == 0:
      word_problem += random_boy2.rstrip("\n") + "."
    elif boys_or_girls2 == 1:
      word_problem += random_girl2.rstrip("\n") + "."
      
  elif random_type == "-":
    word_problem += f" gives {num2} to "
    if boys_or_girls2 == 0:
      word_problem += random_boy2.rstrip("\n") + "."
    elif boys_or_girls2 == 1:
      word_problem += random_girl2.rstrip("\n") + "."
  
  elif random_type == "x":
    word_problem += f" multiplies it by {num2} the next {random_time}."
    
  word_problem += f" How many {rand_item} does "
  
  if boys_or_girls == 0:
    word_problem += "he have now?"
  elif boys_or_girls == 1:
    word_problem += "she have now?"
  
  answer = 0
  
  if random_type == "+":
    answer += (num1 + num2)
  elif random_type == "-":
    answer += (num1 - num2)
  elif random_type == "x":
    answer += (num1 * num2)
  
  answer = f"{answer} {rand_item}"
  
  return [word_problem, answer, random_type]