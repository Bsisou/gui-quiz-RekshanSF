import os
os.system('pip install Pillow')

# Import module  
from tkinter import * 
from PIL import Image, ImageTk

#list of names
names = []

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
        

        
#start of Program       
# Create object  
if __name__ == "__main__":
        root = Tk()
        root.title("Rekki's Global Mind Melt")
       

main_object = Main(root)

# Execute tkinter 
root.mainloop()