import tkinter as tk

window = tk.Tk()
window.title("Hello world")
window.geometry("400x300")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()