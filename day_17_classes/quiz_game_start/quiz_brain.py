class QuizBrain:
    
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_num = 0
        self.score = 0
        
    def still_has_questions(self):
        return self.question_num < len (self.question_list)

    
    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num+=1
        user_answer = input(f"Q.{self.question_num}: {current_question.text} (True/False)?: " )
        correct_answer = current_question.answer
        self.check_answer(correct_answer,user_answer)
        
    def check_answer(self,correct_answer,user_answer):
        if correct_answer.lower() == user_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong!")
        print(f"The Correct answer was {correct_answer}")
        print(f"Current Score is: {self.score}/{self.question_num}")
        print("\n")
    
