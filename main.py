import os
os.system('pip install Pillow')

# Import module  
from tkinter import * 
from PIL import Image, ImageTk
import ramdom

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
    qnum = ramdom.radint(1,10)
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
        

        
#start of Program~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
# Create object  
if __name__ == "__main__":
        root = Tk()
        root.title("Rekki's Global Mind Melt")
       

main_object = Main(root)

# Execute tkinter 
root.mainloop()