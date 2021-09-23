from Day_17.data import question_data
from Day_17.question import Question
from Day_17.quiz_brain import QuizBrain


def construct_question_bank():
    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank


if __name__ == "__main__":
    ques_list = construct_question_bank()
    quiz = QuizBrain(ques_list)
    begin_quiz = input("Do you want to begin the quiz? 'Y' or 'N'.")
    while begin_quiz == 'Y':
        quiz.display_question()
        if quiz.is_end_of_quiz():
            quiz.print_final_score()
            begin_quiz = 'N'






