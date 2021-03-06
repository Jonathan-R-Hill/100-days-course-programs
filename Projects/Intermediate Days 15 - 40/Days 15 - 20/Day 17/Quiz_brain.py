valid = ["True", "False"]

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        while True:
            answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ").title()
            if answer in valid:
                break
            
        if answer == current_question.answer:
            self.score += 1
            print(f"That was correct! Your score is {self.score}\n")
        else:
            print(f"That was the wrong answer. The answer was: {current_question.answer}\n")
    
    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
    
