class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        new_question = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f"Q.{self.question_number}: {new_question.text} (True/False)? ")
        self.check_answer(user, new_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right.")
            print(f"The correct answer is {correct_answer}")
            print(f"Your score: {self.score}/{self.question_number}")
            print("\n")
        else:
            print("That's wrong.")
            print(f"The correct answer is {correct_answer}")
            print(f"Your score: {self.score}/{self.question_number}")
            print("\n")

        if not self.still_has_questions():
            print("You completed the quiz! Thanks for playing.")
            print(f"Your final score: {self.score}/{self.question_number}")



