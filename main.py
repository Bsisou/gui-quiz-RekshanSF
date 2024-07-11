import os
os.system('pip install Pillow')

# Import module  
from tkinter import * 
from PIL import Image, ImageTk
import random

# Dictionary of all my questions and answers

# index 0 is the question, index 1-4 are the answers, index 5 is the correct answer written again, index 6 is the correct answer index
q_a ={
    1: ["The Lion is the National Animal \nof what Country?", 'Nepal', 'Sri Lanka', 'China', 'South Korea', 'Sri Lanka', 2],
    2: ["Kangaroos Are The National \nAnimal Of What Country?", 'USA', 'India', 'Italy', 'Australia', 'Australia', 4],
    3: ["What is the capital city \nof Japan?", 'Seoul', 'Beijing', 'Tokyo', 'Bangkok', 'Tokyo', 3],
    4: ["What is the smallest country \nin the world?", 'Monaco', 'Vatican City', 'San Marino', 'Liechtenstein', 'Vatican City', 2],
    5: ["What is the longest river \nin the world?", 'Amazon', 'Nile', 'Yangtze', 'Mississippi', 'Nile', 2],
    6: ["What is the tallest mountain \nin the world?", 'Mount Ruapehu', 'Kangchenjunga', 'Mount Everest', 'Lhotse', 'Mount Everest', 3],
    7: ["Which country is known \nfor the Taj Mahal?", 'India', 'Pakistan', 'Bangladesh', 'Nepal', 'India', 1],
    8: ["What is the official language \nof Brazil?", 'Spanish', 'Portuguese', 'French', 'English', 'Portuguese', 2],
    9: ["What is the capital \nof Canada?", 'Toronto', 'Ottawa', 'Vancouver', 'Montreal', 'Ottawa', 2],
    10: ["Which country has the largest \npopulation?", 'India', 'USA', 'China', 'Russia', 'China', 3]
}

# Main class
class Main:
    def __init__(self, parent):
        self.bgcolor = "blue"
        self.names = []
        self.asked = []
        self.score = 0
        self.qnum = None

        # Frame Setup
        self.quiz_frame = Frame(parent, bg=self.bgcolor, width=800, height=600)
        self.quiz_frame.pack(expand=True, fill='both')

        # Label widget for heading
        self.heading_label = Label(self.quiz_frame, text="Welcome to \n Rekki's Global Mind Melt!", font=("impact", 30, "bold"), bg=self.bgcolor)
        self.heading_label.pack(pady=20)

        # Label for enter your name text 
        self.user_label = Label(self.quiz_frame, text="Enter Your Name Below", font=("impact", 20, "bold"), bg=self.bgcolor, pady=50, padx=20)
        self.user_label.pack(pady=20)

        # Entry box for name
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.pack(pady=10)

        # Next button 
        self.nextbutton = Button(self.quiz_frame, text="Next", bg="green", command=self.namecollect)
        self.nextbutton.pack(pady=20)

    def namecollect(self):
        name = self.entry_box.get()
        self.names.append(name)
        self.quiz_frame.destroy()
        Question(root, self.names, self.asked, self.score)

# Question Page Class 
class Question:
    def __init__(self, parent, names, asked, score):
        self.bgcolor = "blue"
        self.names = names
        self.asked = asked
        self.score = score
        self.qnum = None

        # Frame Setup
        self.quiz_frame = Frame(parent, bg=self.bgcolor, width=800, height=600)
        self.quiz_frame.pack (expand=True, fill='both')

        self.randomer()

        # Label widget for heading
        self.question_label = Label(self.quiz_frame, text=q_a[self.qnum][0], font=("impact", 30, "bold"), bg=self.bgcolor)
        self.question_label.pack(pady=20)


        # Holds the value of the radio button 
        self.var1 = IntVar()

        # First radio button
        self.rb1 = Radiobutton(self.quiz_frame, text=q_a[self.qnum][1], font=("impact", 12), bg=self.bgcolor, value=1, variable=self.var1, pady=10, padx=10)
        self.rb1.pack(pady=10)

        # Second radio button
        self.rb2 = Radiobutton(self.quiz_frame, text=q_a[self.qnum][2], font=("impact", 12), bg=self.bgcolor, value=2, variable=self.var1, pady=10, padx=10)
        self.rb2.pack(pady=10)

        # Third radio button
        self.rb3 = Radiobutton(self.quiz_frame, text=q_a[self.qnum][3], font=("impact", 12), bg=self.bgcolor, value=3, variable=self.var1, pady=10, padx=10)
        self.rb3.pack(pady=10)

        # Fourth radio button
        self.rb4 = Radiobutton(self.quiz_frame, text=q_a[self.qnum][4], font=("impact", 12), bg=self.bgcolor, value=4, variable=self.var1, pady=10, padx=10)
        self.rb4.pack(pady=10)

        # Confirm button
        self.confirm = Button(self.quiz_frame, text="Confirm", bg="green", command=self.score_nextq)
        self.confirm.pack(pady=10)

        # Score label 
        self.score_label = Label(self.quiz_frame, text="Score", font=("impact", 20, "bold"), bg=self.bgcolor, pady=50, padx=20)
        self.score_label.pack(pady=10)

    def randomer(self):
        self.qnum = random.randint(1, 10)
        if self.qnum not in self.asked:
            self.asked.append(self.qnum)
        else:
            self.randomer()

    def question_setup(self):
        if len(self.asked) < 10:
            self.randomer()
            self.var1.set(0)
            self.question_label.config(text=q_a[self.qnum][0])
            self.rb1.config(text=q_a[self.qnum][1])
            self.rb2.config(text=q_a[self.qnum][2])
            self.rb3.config(text=q_a[self.qnum][3])
            self.rb4.config(text=q_a[self.qnum][4])
        else:
            self.quiz_frame.destroy()
            End(root, self.score, self.names[0])

    def score_nextq(self):
        choice = self.var1.get()  # This collects the answer the user has chosen
        # This checks if the answer the user has chosen is correct
        if choice == q_a[self.qnum][6]:
            self.score += 1
            self.score_label.configure(text=f"Score: {self.score}")  # This if statement shows what happens when the user gets the question correct, an f string is used for the score label to show the score
        else:
            self.score_label.configure(text=f"The correct answer was: {q_a[self.qnum][5]}")  # This else statement shows what happens when the user gets the answer wrong, It configures the score label to show the correct answer

        if len(self.asked) >= 10:
            self.confirm.config(text="Finish", command=self.end_quiz)
        else:
            self.question_setup()

    def end_quiz(self):
        self.quiz_frame.destroy()
        End(root, self.score, self.names[0])

class End:
    def __init__(self, parent, score, name): 
        self.bgcolor = "blue"
        self.score = score
        self.name = name

        # Setting up the frame 
        self.end_frame = Frame(parent, bg=self.bgcolor,width=800, height=600)
        self.end_frame.pack(expand=True, fill='both')

        # Label to display score at the end 
        self.end_label = Label(self.end_frame, text=f"Your final score is {self.score}", font=("impact", 30, "bold"), bg=self.bgcolor)
        self.end_label.pack(pady=20)

        #Label to display the costom message at the end of the quiz 
        self.custommesage = self.custommesage()
        self.messagelabel = Label(self.end_frame, text=self.custommesage, font=("impact", 30, "bold"), bg=self.bgcolor)
        self.messagelabel.pack(pady=20)
    

#This fuction is for the custom message element of my quiz, This message is depentant on the score the user gets at the end of the quiz.
    
    def custommesage(self): 
        if self.score == 10:
            return f"congrats {self.name}, You have Earned the Title of Global Genius!"
        else: 
            return f"Keep Trying {self.name},\nYou Still Have Lots to Learn"
    

# Start of Program
# Create object  
if __name__ == "__main__":
    root = Tk()
    root.title("Rekki's Global Mind Melt")
    root.geometry("800x600")
    root.resizable(False, False)  # Disable window resizing
    main_object = Main(root)
    # Execute tkinter 
    root.mainloop()
