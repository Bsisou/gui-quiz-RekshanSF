import os
os.system('pip install Pillow')

# Import module  
from tkinter import * 
from PIL import Image, ImageTk
import random


# Main class
class Main:

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
    
    def __init__(self, parent):
        self.bgcolor = "lightgrey"
        self.textcolor = "white"
        self.btextcolor = "black"
        self.buttoncolor = "#f72585"
        self.names = []
        self.asked = []
        self.score = 0
        self.qnum = None

        # Frame Setup
        self.quiz_frame = Frame(parent, bg=self.bgcolor, width=800, height=600)
        self.quiz_frame.pack(expand=True, fill='both')

        # Label widget for heading
        self.heading_label = Label(self.quiz_frame, text="Welcome to \n Rekki's Global Mind Melt!", font=("impact", 30, "bold"), bg=self.buttoncolor, fg=self.textcolor,relief="solid", bd=3)
        self.heading_label.pack(pady=40)

        # Label for enter your name text 
        self.user_label = Label(self.quiz_frame, text="Enter Your Name Below", font=("impact", 20, "bold"), bg=self.buttoncolor, fg=self.textcolor,relief="solid", bd=3)
                                
        self.user_label.pack(pady=40)

        # Entry box for name
        self.entry_box = Entry(self.quiz_frame, justify="center", font=("impact", 15, "bold"),relief="solid", bd=3)
        
        self.entry_box.pack(pady=10)

        # Next button 
        self.nextbutton = Button(self.quiz_frame, text="Start Quiz!", bg="limegreen", fg= "white",font=("impact", 20),relief="solid", bd=3, command=self.namecollect)
        self.nextbutton.pack(pady=60)

        #Label to show the error message
        self.errorlabel =  Label(self.quiz_frame, text="", font=("impact", 15, "bold"), bg=self.bgcolor, fg="red")

        self.errorlabel.pack(pady=10)
    
    # this fuction is used to add the users name in the names list
    # This fuction is also used to check if the name entered is accepcted into the boudary.
    
    def namecollect(self):
        name = self.entry_box.get()

        if not name.isalpha(): #This checks if the characters enetered are letters only 
            self.errorlabel.config(text="Name Must Only Contain Letters")

        #This makes sure that the name entered is greater than 2 characters 
        elif len(name) < 2: 
            self.errorlabel.config(text="Name must be at least 2 characters")

        #This makes sure that the name entered is not greater than 10 characters.
        elif len(name) > 10: 
             self.errorlabel.config(text="Name must be 10 characters or less")
            
        #if the name is acceptable then it is added into the name list and starts the quiz with the question page.
        else: 
            self.names.append(name)
            self.quiz_frame.destroy()
            Question(root, self.names, self.asked, self.score)
        

    # this fuction is used to reset all the varibles to their oringal states, This is activated only if the users wants to restart the quiz. This can be done by pressing the restart button at the end of the quiz
    
    def restart(self):
        self.names = []
        self.asked = []
        self.score = 0
        self.__init__(root)

# Question Page Class 
class Question:
    def __init__(self, parent, names, asked, score):
        self.bgcolor = "lightgrey"
        self.textcolor = "white"
        self.btextcolor = "black"
        self.buttoncolor = "#f72585"
        self.names = names
        self.asked = asked
        self.score = score
        self.qnum = None

        # Frame Setup
        self.quiz_frame = Frame(parent, bg=self.bgcolor, width=800, height=600)
        self.quiz_frame.pack (expand=True, fill='both')

        self.randomer()

        # Label widget for heading
        self.question_label = Label(self.quiz_frame, text=Main.q_a[self.qnum][0], font=("impact", 30, "bold"), bg=self.buttoncolor, fg=self.textcolor, relief="solid", bd=5,)
        
        self.question_label.pack(pady=30)


        # Holds the value of the radio button 
        self.var1 = IntVar()

        # First radio button
        self.rb1 = Radiobutton(self.quiz_frame, text=Main.q_a[self.qnum][1], font=("impact", 12), bg=self.buttoncolor,fg=self.btextcolor, relief="solid", bd=3, value=1, variable=self.var1, pady=10, padx=10)
        
        self.rb1.pack(pady=10)

        # Second radio button
        self.rb2 = Radiobutton(self.quiz_frame, text=Main.q_a[self.qnum][2], font=("impact", 12), bg=self.buttoncolor, fg=self.btextcolor,relief="solid", bd=3, value=2, variable=self.var1, pady=10, padx=10)
        
        self.rb2.pack(pady=10)

        # Third radio button
        self.rb3 = Radiobutton(self.quiz_frame, text=Main.q_a[self.qnum][3], font=("impact", 12), bg=self.buttoncolor, fg= self.btextcolor,relief="solid", bd=3, value=3, variable=self.var1, pady=10, padx=10)
        
        self.rb3.pack(pady=10)

        # Fourth radio button
        self.rb4 = Radiobutton(self.quiz_frame, text=Main.q_a[self.qnum][4], font=("impact", 12), bg=self.buttoncolor, fg= self.btextcolor,relief="solid", bd=3, value=4, variable=self.var1, pady=10, padx=10)
        
        self.rb4.pack(pady=10)

        
        # Confirm button
        self.confirm = Button(self.quiz_frame, text="Confirm", bg="limegreen", fg= self.textcolor,font=("impact", 22), relief="solid", bd=3, command=self.score_nextq)
        
        self.confirm.pack(pady=25)

        # Score label 
        self.score_label = Label(self.quiz_frame, text="Score", font=("impact", 15, "bold"), bg="dodgerblue", fg=self.textcolor, relief="solid", bd=3)
        
        self.score_label.pack(pady=10)

    def randomer(self):

        #this varible contains all questions from the dictionary that is not yet asked 
        remaining_questions = [q for q in Main.q_a.keys() if q not in self.asked]

        #this shuffles the reamining questions so that the order is ramdom 
        if remaining_questions:
            random.shuffle(remaining_questions)
            self.qnum = remaining_questions[0]
            self.asked.append(self.qnum) #adds new question to the asked list

        else:
            self.qnum = None     #after all questions have been asked 

    def question_setup(self):
        if len(self.asked) < 10:
            self.randomer()
            self.var1.set(0)
            self.question_label.config(text=Main.q_a[self.qnum][0])
            self.rb1.config(text=Main.q_a[self.qnum][1])
            self.rb2.config(text=Main.q_a[self.qnum][2])
            self.rb3.config(text=Main.q_a[self.qnum][3])
            self.rb4.config(text=Main.q_a[self.qnum][4])
        else:
            self.quiz_frame.destroy()
            End(root, self.score, self.names[0])

    def score_nextq(self):
        choice = self.var1.get()  # This collects the answer the user has chosen
        # This checks if the answer the user has chosen is correct
        if choice == Main.q_a[self.qnum][6]:
            self.score += 1
            self.score_label.configure(text=f"Score: {self.score}")  # This if statement shows what happens when the user gets the question correct, an f string is used for the score label to show the score
        else:
            self.score_label.configure(text=f"The correct answer was: {Main.q_a[self.qnum][5]}")  # This else statement shows what happens when the user gets the answer wrong, It configures the score label to show the correct answer

        if len(self.asked) >= 10:
            self.confirm.config(text="Finish", command=self.end_quiz)
        else:
            self.question_setup()

    def end_quiz(self):
        self.quiz_frame.destroy()
        End(root, self.score, self.names[0])


#Class for my End Page 
class End:
    def __init__(self, parent, score, name): 
        self.bgcolor = "lightgrey"
        self.textcolor = "white"
        self.btextcolor = "black"
        self.buttoncolor = "#f72585"
        
        self.score = score
        self.name = name

        # Setting up the frame 
        self.end_frame = Frame(parent, bg=self.bgcolor,width=800, height=600)
        self.end_frame.pack(expand=True, fill='both')

        # Label to display score at the end 
        self.end_label = Label(self.end_frame, text=f"Your final score is {self.score}", font=("impact", 30, "bold"), bg=self.buttoncolor, fg=self.textcolor, relief="solid", bd=3)
        self.end_label.pack(pady=80)

        #Label to display the costom message at the end of the quiz 
        self.custommesage = self.custommesage()
        self.messagelabel = Label(self.end_frame, text=self.custommesage, font=("impact", 30, "bold"), bg=self.buttoncolor, fg=  self.textcolor, relief="solid", bd=3)
        self.messagelabel.pack(pady=40)


        #Button to restart the quiz 
        self.restartbutton = Button(self.end_frame, text="Restart", bg="limegreen", fg= self.textcolor,font=("impact", 20),relief="solid", bd=3, command= self.restartquiz)
        self.restartbutton.pack(pady=60)

    def restartquiz(self):
        self.end_frame.destroy()
        main_object.restart()
        

#This fuction is for the custom message element of my quiz, This message is depentant on the score the user gets at the end of the quiz.
    
    def custommesage(self): 
        if self.score == 10:
            return f"Congrats {self.name}, You have Earned the Title of Global Genius!"

        elif self.score >= 7: 
            return f"Great Job {self.name},\n You are quite a Global Geek!"

        elif self.score >= 4:
            return f"Good One {self.name},\n I guess you know a bit about\n this circle we called Earth"
        
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
