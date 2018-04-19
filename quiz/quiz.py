def show_menu():
    print("1. Ask question")
    print("2. Add a question")
    print("3. Exit")
    
    option = input("Enter Option: ")
    return option

def ask_question():
    questions = []
    answers = []
    
    with open("questions.txt", "r") as file:
        line = file.read().splitlines()
    
    for i, text in enumerate(line):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    
    number_of_questions = len(questions)
    questions_and_answers = zip(questions,answers)
    
    score = 0
            
    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        if guess == answer:
            score +=1
            print("right!")
            print("Your current score is {0}".format(score))
        else:
            print("wrong")
    
    print("You got {0} out of {1}".format(score, number_of_questions))
            
def add_question():
    print(" ")
    question = input("Enter a question\n")
    
    print(" ")
    print("ok tell me the answer")
    answer = input("{0}\n".format(question))
    
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

    

def game_loop():
    while True:
        option = show_menu()
        if option == "1":
           ask_question()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else: 
            print("please select an option")
        print(" ")
    
game_loop()