from tkinter import *
window=Tk()

window.title("Interest Calculator")
window.geometry("380x400")
window.configure(bg='grey')

def calculate_interest():
    principal = float(principal.get())
    rate = float(rate.get())
    time = float(time.get())
    i = (principal*rate*time)/100
    interest = round(1, 2)
    name = username.get()

    result_label.destroy.get()

    msg=""
    
    output_message=Label(result_frame,text=name+",your interest is"+str(interest)+"and"+msg,bg="grey",font=("calibri",12),width=42)
    output_message.place(x=20,y=40)
    output_message.pack()

app_label=Label(window,text="INTEREST CALCULATOR",fg="black",bg="grey",font=("calibri",20),bd=1)
app_label.place(x=50,y=20)

name_label=Label(window,text="Your Name",fg="black",bg="grey",font=("calibri",12),bd=1)
name_label.place(x=20,y=90)

username=Entry(window,text="",bd=2,width=22)
username.place(x=150,y=92)

principle_label=name_label=Label(window,text="Enter Principal",fg="black",bg="grey",font=("calibri",12))
principle_label.place(x=20,y=140)

principle_entry=Entry(window, text="", bd=2, width=15)
principle_entry.place(x=150, y=142)

rate_label=Label(window, text="Enter Rate", fg = "black", bg = "grey", font=("Calibri", 12))
rate_label.place(x=20, y=185)

rate_entry=Entry(window, text="", bd=2, width=15)
rate_entry.place(x=150, y=187)

time_label=Label(window, text="Enter Time", fg = "black", bg = "grey", font=("Calibri", 12))
time_label.place(x=20, y=228)

time_entry=Entry(window, text="", bd=2, width=15)
time_entry.place(x=150, y=230)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "cyan",bd=4,command=calculate_interest)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "grey", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "grey", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()


window.mainloop()