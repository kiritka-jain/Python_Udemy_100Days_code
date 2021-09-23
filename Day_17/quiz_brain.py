class QuizBrain:
    def __init__(self, question_list):
        self.present_question_number = 0
        self.score = 0
        self.question_list = question_list

    def display_question(self):
        ques = self.question_list[self.present_question_number]
        user_ans = input(f"Q.{self.present_question_number + 1} {ques.text}('True/False')?")
        self.__update_present_question_number()
        self.__check_answer(ques, user_ans)

    def __check_answer(self, ques, user_ans):
        print(ques.correct_answer)
        if ques.correct_answer == user_ans:
            self.__increase_score()
            print("Your answer is correct.")
            return True
        print("Your answer is incorrect.")
        return False

    def __increase_score(self):
        self.score += 1

    def is_end_of_quiz(self):
        total_questions = len(self.question_list)
        if self.present_question_number < total_questions:
            return False
        return True

    def __update_present_question_number(self):
        self.present_question_number += 1

    def print_final_score(self):
        print(f"Your final score of the quiz is:{self.score}")
