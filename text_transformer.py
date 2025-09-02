from tkinter import *

root = Tk()
root.title("Text Transformer")
root.geometry("300x350")

def transform_text():
    text_input = text.get()
    joiner_input = joiner.get()
    result = joiner_input.join(text_input)


    output.delete(0, END)
    output.insert(0, result)

output = Entry(root, font=("Arial", 20))
output.insert(0, "Result", )
output.pack(pady=20, padx=20)

text = Entry(root, font=("Arial", 20))
text.insert(0, "Enter text here")
text.pack(pady=20, padx=20)

joiner = Entry(root, font=("Arial", 20))
joiner.insert(0, "Insert joiner here")
joiner.pack(pady=20, padx=20)

btn = Button(root, text="Transform", font=("Arial", 20), bg="#ccc", command=transform_text)
btn.pack(pady=20, fill=X, padx=20)

root.mainloop()