from questions import question_dict

class Question:
    def __init__(self, answer: str, question:str) -> None:

        self.question = question
        self.answer = answer

    def ask_answer(self)->str:
       
        return self.question

    def get_answer (self)->str:

        while True:
            user_answer = input("Enter 'y' for Yes or 'n' for No: ")

            if user_answer.lower() == 'y' or user_answer.lower() == 'n':
                return user_answer.lower()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        
class Quiz:
    def __init__(self, questions_dict: dict) -> None:
        self.questions_dict = questions_dict
        self.score = 0

    def start_game (self) -> None:
        
        for question, answer in self.questions_dict.items():
            
            question = Question(question=question, answer=answer)

            print(question.ask_answer())
            
            user_answer = question.get_answer()

            if user_answer == answer:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect.")

        print("Final score:", self.score)
   

quiz = Quiz(questions_dict=question_dict) 
quiz.start_game()
