from data import question_data
from Quiz_brain import QuizBrain, Question

question_bank = []
for i in range(0, len(question_data)):
    i = question_data[i]
    question_bank.append(Question(i["text"], i["answer"]))


quiz = QuizBrain(question_bank)
while quiz.still_has_questions() != False:
    quiz.next_question()

print(f"Quiz complete! \nYour final score is: {quiz.score}/{len(question_bank)}")
    