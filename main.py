# Import module  
import os
from tkinter import *

# Create object  
root = Tk() 

# Adjust size  
root.geometry("1400x700") 

#add image file 
bg = PhotoImage(file="start1.png")

# Resize image


#Create Canvas
canvas1= Canvas(root, width=1400, height=700)
canvas1.pack(fill="both", expand=True)

#display image 
canvas1.create_image(0, 0, image=bg, anchor="nw")



# Execute tkinter 
root.mainloop()