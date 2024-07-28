from tkinter import *
import os
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

false_image_path = r"API\quizzler_app_start\images\false.png"
true_image_path = r"API\quizzler_app_start\images\true.png"


class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score = 0
        
        
        #labels
        self.score_label = Label(text=f"Score: {self.score}",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)          
        
        self.canvas = Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.q_text = self.canvas.create_text(150,125,width=280,text="Viswa",fill="black",font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_image = PhotoImage(file=r"API\quizzler_app_start\images\true.png")
        false_image = PhotoImage(file=r"API\quizzler_app_start\images\false.png")
        self.false_button = Button(image=false_image,highlightthickness=0,command=self.false_answer)
        self.false_button.grid(row=2,column=0)
        
        
        self.true_button = Button(image = true_image,highlightthickness=0,command=self.true_answer)
        self.true_button.grid(row=2,column=1)
        
        self.get_next_question()
        
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg ="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text,text = question_text)
        else:
            self.canvas.itemconfig(self.q_text,text = f"You reached the end of Quiz and your Final Score is: {self.quiz.score}/10")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")    
            
    def true_answer(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)   
        
    def false_answer(self):
        is_right = self.quiz.check_answer(user_answer="False")  
        self.give_feedback(is_right)    

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000,self.get_next_question)