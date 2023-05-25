# Class in charge of:
# Asking questions,
# Checking if given answer is correct,
# Checking if quiz is over.

class QuizBrain:

  def __init__(self, q_bank):
    self.question_number = 0
    self.questions_list = q_bank
    self.score = 0


  def still_has_questions(self):
    return self.question_number < len(self.questions_list)

    
  def next_question(self):
    current_question = self.questions_list[self.question_number].question
    correct_answer = self.questions_list[self.question_number].answer
    
    self.question_number += 1
    given_answer = input(f"Q.{self.question_number}: {current_question}. (True/False)? -> ")
    
    self.check_answer(given_answer, correct_answer)


  def check_answer(self, given_answer, correct_answer):
    
    if given_answer.lower() == correct_answer.lower():
      self.score += 1
      print("That's right!")
    else:
      print("Oh, no. That's not it.")
      
    print(f"Answer was: {correct_answer}")
    print(f"Current score is: {self.score}\n")
