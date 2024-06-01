# Import module  
import os
import tkinter as tk

# Create object  
root = tk.Tk() 

#Creating Question page 1 
def questionpage():

          root.destroy()         
          Q1 = tk.Tk() 
          Q1.title("Question 1")
          Q1.geometry("1400x700")
          Q1.mainloop()


#chnage window title name 
root.title("Rekki's Global Mind Melt")

# Adjust size  
root.geometry("1400x700") 

#add image file 
bg = tk.PhotoImage(file="start1.png")

#Create Canvas
canvas1= tk.Canvas(root, width=1400, height=700)
canvas1.pack(fill="both", expand=True)

#display image 
canvas1.create_image(0, 0, image=bg, anchor="nw")

#adding button to canvas 
b1 = tk.Button(root, text='Start', width=40,
          height=5, bd='10', command=questionpage)

b1.place(x=450, y=450)

# Execute tkinter 
root.mainloop()