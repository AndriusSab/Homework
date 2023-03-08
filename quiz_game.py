from questions import question_dict
import logging
logging.basicConfig(level=logging.DEBUG,filename='quiz_game.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Question:
    def __init__(self, answer: str, question:str) -> None:

        self.question = question
        self.answer = answer

    def ask_question(self)->str:
       
        return self.question

    def get_answer (self)->str:

        while True:
            user_answer = input("Enter 'y' for Yes or 'n' for No: ")
            logging.info("Geting user input :{user_answer}")
            if user_answer.lower() == 'y' or user_answer.lower() == 'n':
                return user_answer.lower()
            else:
                logging.error("Wrong user imput")
                print("Invalid input. Please enter 'y' or 'n'.")
        
class Quiz(Question):

    def __init__(self, questions_dict: dict) -> None:
        # adding question)dict aatribute to Quiz class
        self.questions_dict = questions_dict

    def start_game (self) -> None:
    
        self.score = 0
            # iterating through a dictionary
        for question, answer in self.questions_dict.items():
            # instantiation Class Question
            question = Question(question=question, answer=answer)

            print(question.ask_question())
            
            user_answer = question.get_answer()
            
            if user_answer == answer:
                logging.info("Checking if user answer is correct")
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect.")

        print("Thanks for playing, your final score is:", self.score)
   

quiz = Quiz(questions_dict=question_dict) 
quiz.start_game()
