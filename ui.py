from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(row=1, column=2)
        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="some questions",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)
        self.button_check = Button(text="✔️", bg="green", fg="white", width=8, height=3, command=self.true_pressed)
        self.button_check.grid(row=3, column=1)
        self.button_cross = Button(text="❌", bg="red", fg="white", width=6, height=2, padx=10, pady=10,
                                   command=self.false_pressed)
        self.button_cross.grid(row=3, column=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the out of the question")
            self.button_check.config(state = "disabled")
            self.button_cross.config(state = "disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
