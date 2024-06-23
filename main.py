import os
os.system('pip install Pillow')

# Import module  
from tkinter import * 
from PIL import Image, ImageTk
import random

#list of names
names = []

global q_a

asked = []

#dictionary of all my questions and answers
q_a = {
    
    #index 0 is the question, index 1-4 are the answers, index 5 is the correct answer written again, index 6 is the correct answer index
    
    1: ["What Flag is this ?", 'Nepal', 'Sri lanka', 'China', 'South Korea', 'Sri Lanka', 2],
    
    2: ["Kangaroos Are The National Animal Of What Country?", 'USA', 'India', 'Italy', 'Australia', 'Australia', 4],

    3: ["What is the capital city of Japan?", 'Seoul', 'Beijing', 'Tokyo', 'Bangkok', 'Tokyo', 3],

    4: ["What is the smallest country in the world?", 'Monaco', 'Vatican City', 'San Marino', 'Liechtenstein', 'Vatican City', 2],

    5: ["What is the longest river in the world?", 'Amazon', 'Nile', 'Yangtze', 'Mississippi', 'Nile', 2],

    6: ["What is the tallest mountain in the world?", 'Mount Ruapehu', 'Kangchenjunga', 'Mount Everest', 'Lhotse', 'Mount Everest', 3],

    7: ["Which country is known for the Taj Mahal?", 'India', 'Pakistan', 'Bangladesh', 'Nepal', 'India', 1],

    8: ["What is the official language of Brazil?", 'Spanish', 'Portuguese', 'French', 'English', 'Portuguese', 2],

    9: ["What is the capital of Canada?", 'Toronto', 'Ottawa', 'Vancouver', 'Montreal', 'Ottawa', 2],

    10: ["Which country has the largest population?", 'India', 'USA', 'China', 'Russia', 'China', 3]

}

def ramdomer():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        ramdomer()

#_______ Creating main class
class Main:
    def __init__(self, parent):
        bgcolor = "blue"
        # Frame Setup
        self.quiz_frame = Frame(parent, bg=bgcolor, padx=100, pady=100)
        self.quiz_frame.grid()
        
        # Label widget for heading
        self.heading_label = Label(self.quiz_frame, text="Welcome to \n Rekki's Global Mind Melt!",font=("impact", 30, "bold"), bg=bgcolor)
        self.heading_label.grid(row=0)
        #label for enter your name text 
        self.user_label = Label(self.quiz_frame, text="Enter Your Name Below", font=("impact", 20, "bold"), bg=bgcolor, pady=50, padx=20 )
        self.user_label.grid(row=1)

        #entry box for name
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2)

        #Next button 
        self.nextbutton = Button(self.quiz_frame, text="Next", bg="green", command=self.namecollect)
        self.nextbutton.grid(row=3, pady=30)

        #name collection
    def namecollect(self):
        name = self.entry_box.get()
        names.append(name)
        self.quiz_frame.destroy()
        Question(root)
    

#Question Page Class 

class Question:
    def __init__(self, parent):
        bgcolor = "blue"
        # Frame Setup
        self.quiz_frame = Frame(parent, bg=bgcolor, padx=100, pady=100)
        self.quiz_frame.grid()

        ramdomer()
        # Label widget for heading
        self.question_label = Label(self.quiz_frame, text= q_a[qnum][0], font=("impact", 30, "bold"), bg=bgcolor)
        self.question_label.grid(row=0, padx=10,pady=10)

        #Holds the value of the radio button 
        self.var1=IntVar()

        #first radio button
        self.rb1 = Radiobutton (self.quiz_frame,text=q_a[qnum][1], font= ("impact", 12), bg=bgcolor, value=1, variable=self.var1, pady=10, padx=10)
        self.rb1.grid(row=1)

        #2nd radio button
        self.rb2 = Radiobutton (self.quiz_frame,text=q_a[qnum][2], font= ("impact", 12), bg=bgcolor, value=2, variable=self.var1, pady=10, padx=10)
        self.rb2.grid(row=3)

        #3rd radio button
        self.rb3 = Radiobutton (self.quiz_frame,text=q_a[qnum][3], font= ("impact", 12), bg=bgcolor, value=3, variable=self.var1, pady=10, padx=10)
        self.rb3.grid(row=5)

        #4th radio button
        self.rb4 = Radiobutton (self.quiz_frame,text=q_a[qnum][4], font= ("impact", 12), bg=bgcolor, value=4, variable=self.var1, pady=10, padx=10)
        self.rb4.grid(row=7)

        #confirm button
        self.confirm = Button(self.quiz_frame, text="Confirm", bg="green", command=self.score_nextq)
        self.confirm.grid(row=10)


        #Score label 
        self.score_label = Label(self.quiz_frame, text="Score", font=("impact", 20, "bold"), bg=bgcolor, pady=50, padx=20 )
        self.score_label.grid(row=12)
        

        #Next question code
    def question_setup(self):
        if len(asked) < 10:
            ramdomer()
            self.var1.set(0)
            self.question_label.config(text=q_a[qnum][0])
            self.rb1.config(text=q_a[qnum][1])
            self.rb2.config(text=q_a[qnum][2])
            self.rb3.config(text=q_a[qnum][3])
            self.rb4.config(text=q_a[qnum][4])
        else : 
            self.quiz_frame.destroy()
            End(root)
        

        #to keep track of progress througout the quiz (score)

    def score_nextq(self):
        global score
        scr_label = self.score_label
        choice = self.var1.get() #This collects the answer the user has chosen

        #this checks if the answer the user has chosen is correct
        if choice == q_a[qnum][6]:
            score += 1
            scr_label.configure(text = f"Score: {score}") #This if stament shows what happends when the user gets the question correct, an f string is used for the score label to show the score
        else:
            scr_label.configure(text=f"The correct answer was: {q_a[qnum][5]}") #this else stament shows what happedns when the user gets the answer wrong, It configures the score label to show the correct answer

        if len(asked) >=10:
            self.confirm.config(text="finish", command=self.end_quiz)
        else:
            self.question_setup()

    def end_quiz(self):
        self.quiz_frame.destroy()
        End(root)

                
            
        

class End:
    def __init__(self,parent): 
        bgcolor = "blue"

        #seting up the frame 
        self.end_frame = Frame(parent, bg = bgcolor, padx=100,pady=100)
        self.end_frame.grid()

        #label to display score at the end 

        self.end_label = Label(self.end_frame, text =f"Your final score is {score}", font= ("impact", 30, "bold"), bg=bgcolor)
    
        self.end_label.grid(row=0, padx=10, pady=10)
        

#start of Program~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
# Create object  
if __name__ == "__main__":
        score = 0
        root = Tk()
        root.title("Rekki's Global Mind Melt")
       

main_object = Main(root)

# Execute tkinter 
root.mainloop()