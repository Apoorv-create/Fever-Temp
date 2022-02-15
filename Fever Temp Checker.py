from tkinter import *
root = Tk()
root.title("Fever_Report")
root.geometry("600x600")

question1_radioButton = StringVar(value = "0")
Question1 = Label(root, text = "Do U have a headache or a soar throught?")
Question1.pack()
Question1_o1 = Radiobutton(root, text = "yes", variable=question1_radioButton, value = "yes")
Question1_o1.pack()                           
Question1_o2 = Radiobutton(root, text = "no", variable=question1_radioButton, value = "no")
Question1_o2.pack()

question2_radioButton = StringVar(value = "0")
Question2 = Label(root, text = "Is your body Temprature high?")
Question2.pack()
Question2_o1 = Radiobutton(root, text = "yes", variable=question2_radioButton, value = "yes")
Question2_o1.pack()                           
Question2_o2 = Radiobutton(root, text = "no", variable=question2_radioButton, value = "no")
Question2_o2.pack()

question3_radioButton = StringVar(value = "0")
Question3 = Label(root, text = "Are there any symptoms of eye redness?")
Question3.pack()
Question3_o1 = Radiobutton(root, text = "yes", variable=question3_radioButton, value = "yes")
Question3_o1.pack()                           
Question3_o2 = Radiobutton(root, text = "no", variable=question3_radioButton, value = "no")
Question3_o2.pack()

def fever_score():
    score = 0
    if question1_radiobutton.get() == "yes":
       score = score + 20
       print(score)
    if question2_radiobutton.get() == "yes":
        score = score+ 20
        print (score)
    if question3_radiobutton.get() == "yes":
        score = score+20
        print(score)
    
    if score <= 20:
        messagebox.showinfo("You don't need a doctor, But do take care!")
        
    elif score > 20 and score <= 40:
        messagebox.showinfo("You should go see a doctor!")
    else:
        messagebox.showinfo("I advise you strongly to visit a doctor!")
        
btn = Button(root, text = "Click me to get results!", command=fever_score)
btn.pack()

root.mainloop
    