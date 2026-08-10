import tkinter as tk

# program 1
# simple calculator GUI

def add():
    a = int(e1.get())
    b = int(e2.get())
    result.config(text="Result: " + str(a + b))

window = tk.Tk()
window.title("Calculator")

e1 = tk.Entry(window)
e1.pack()

e2 = tk.Entry(window)
e2.pack()

btn = tk.Button(window, text="Add", command=add)
btn.pack()

result = tk.Label(window, text="Result:")
result.pack()

window.mainloop()


# program 2
# login GUI

def login():
    user = entry1.get()
    pwd = entry2.get()

    if user == "admin" and pwd == "1234":
        msg.config(text="Login Successful")
    else:
        msg.config(text="Login Failed")

window = tk.Tk()
window.title("Login System")

entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window, show="*")
entry2.pack()

btn = tk.Button(window, text="Login", command=login)
btn.pack()

msg = tk.Label(window, text="")
msg.pack()

window.mainloop()