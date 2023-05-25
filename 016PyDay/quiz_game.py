from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


# Create question bank
question_bank = []

for questions in question_data:
  question = questions["text"]
  answer = questions["answer"]
  new_question = Question(question, answer)
  question_bank.append(new_question)

# Begin Quiz
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()
print(f"\n---Score was: {quiz.score}---")
