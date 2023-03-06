class Question:
    def __init__(self, answer: str, question:str) ->str:
        self.question = question
        self.answer = answer


    def get_question_and_answer(self)->str:
      
        print(self.question)

        while True:
            user_answer = input("Enter 'y' for Yes or 'n' for No: ")

            if user_answer.lower() == 'y' or user_answer.lower() == 'n':
                return user_answer.lower()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        

class PlayQuiz:
    def __init__(self, questions_dict: dict) -> None:
        self.questions_dict = questions_dict
        self.score = 0

    def start_game (self) -> None:
        for question, answer in self.questions_dict.items():
            ask_answer = Question(question=question, answer=answer)
            user_answer = ask_answer.get_question_and_answer()

            if user_answer == answer:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect.")

        print("Final score:", self.score)
   
question_dict = {
    "Is the earth round?": "y",
    "Does the city Crimea belongs to Ukraina": "y",
    "Is it true that you can't touch the elbow with your tongue?" : "n",
    "Is the city Siauliai capital of Lithuania?": "n",
    "Is Lithuania language harder to learn than Python":"n"
}


quiz = PlayQuiz(questions_dict=question_dict) 
quiz.start_game()