print("welcome to the quiz !")

playing = input("do you want to play ? ")
if playing.lower() != "yesss": 
    quit()

print (" Okay! Let's Play :) ")

score = 0

question = input("what does CPU stand for ? ")
if question.lower() == "central processing unit":
    print("CORRECT !")
    score += 1
else: 
    print("INCORRECT !")

question = input("what does GPU stand for ? ")
if question.lower() == "graphics processing unit":
    print("CORRECT !")
    score += 1
else: 
    print("INCORRECT !")

question = input("what does ISAMM stand for ? ")
if question.lower() == "hell":
    print("CORRECT !")
    score += 1
else: 
    print("INCORRECT !")

question = input("what does coding stand for ? ")
if question.lower() == "torture":
    print("CORRECT !")
    score += 1
else: 
    print("INCORRECT !")

print("you got " + str(score) + " questions correct !")
print("you got " + str((score /4) *100) + "%.")
