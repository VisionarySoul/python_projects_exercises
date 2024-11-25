import tkinter

screen = tkinter.Tk()
screen.title("Calculator")
screen.geometry("280x280")
screen.config(padx=20, pady=20)

screen.configure(background="silver")


def add_char(button):
    entry.insert(tkinter.END, button)


def add_text():
    entry.insert(tkinter.END, "Text")


def evaluate():
    try:
        text = entry.get()
        # Evaluate the expression and display the result in the entry
        result = eval(text)
        entry.delete(0, "end")  # Clear the entry
        entry.insert(tkinter.END, str(result))  # Insert the result
    except Exception as e:
        entry.delete(0, "end")
        entry.insert(tkinter.END, "Error")  # Display error if evaluation fails


def clear():
    entry.delete(0, "end")


def setup_gui():
    # Create an Entry widget
    global entry  # Declare entry as global to use it in other functions
    entry = tkinter.Entry()
    entry.grid(row=0, column=0, columnspan=4, padx=10)
    entry.config(width=20, font=("default", 14))

    # Create buttons and pass the button values correctly
    button_1 = tkinter.Button(text="1", command=lambda: add_char("1"))
    button_1.grid(row=3, column=0)
    button_1.config(width=5, padx=5, pady=5, font=("default", 10))

    button_2 = tkinter.Button(text="2", command=lambda: add_char("2"))
    button_2.grid(row=3, column=1)
    button_2.config(width=5, padx=5, pady=5, font=("default", 10))

    button_3 = tkinter.Button(text="3", command=lambda: add_char("3"))
    button_3.grid(row=3, column=2)
    button_3.config(width=5, padx=5, pady=5, font=("default", 10))

    button_4 = tkinter.Button(text="4", command=lambda: add_char("4"))
    button_4.grid(row=4, column=0)
    button_4.config(width=5, padx=5, pady=5, font=("default", 10))

    button_5 = tkinter.Button(text="5", command=lambda: add_char("5"))
    button_5.grid(row=4, column=1)
    button_5.config(width=5, padx=5, pady=5, font=("default", 10))

    button_6 = tkinter.Button(text="6", command=lambda: add_char("6"))
    button_6.grid(row=4, column=2)
    button_6.config(width=5, padx=5, pady=5, font=("default", 10))

    button_7 = tkinter.Button(text="7", command=lambda: add_char("7"))
    button_7.grid(row=5, column=0)
    button_7.config(width=5, padx=5, pady=5, font=("default", 10))

    button_8 = tkinter.Button(text="8", command=lambda: add_char("8"))
    button_8.grid(row=5, column=1)
    button_8.config(width=5, padx=5, pady=5, font=("default", 10))

    button_9 = tkinter.Button(text="9", command=lambda: add_char("9"))
    button_9.grid(row=5, column=2)
    button_9.config(width=5, padx=5, pady=5, font=("default", 10))

    button_0 = tkinter.Button(text="0", command=lambda: add_char("0"))
    button_0.grid(row=6, column=1)
    button_0.config(width=5, padx=5, pady=5, font=("default", 10))

    button_plus = tkinter.Button(text="+", command=lambda: add_char("+"))
    button_plus.grid(row=3, column=3)
    button_plus.config(width=5, padx=5, pady=5, font=("default", 10))

    button_minus = tkinter.Button(text="-", command=lambda: add_char("-"))
    button_minus.grid(row=4, column=3)
    button_minus.config(width=5, padx=5, pady=5, font=("default", 10))

    button_multiply = tkinter.Button(text="*", command=lambda: add_char("*"))
    button_multiply.grid(row=5, column=3)
    button_multiply.config(width=5, padx=5, pady=5, font=("default", 10))

    button_divide = tkinter.Button(text="/", command=lambda: add_char("/"))
    button_divide.grid(row=6, column=3)
    button_divide.config(width=5, padx=5, pady=5, font=("default", 10))

    button_eval = tkinter.Button(text="=", command=evaluate)
    button_eval.grid(row=6, column=2)
    button_eval.config(width=5, padx=5, pady=5, font=("default", 10))

    button_clear = tkinter.Button(text="CE", command=clear)
    button_clear.grid(row=6, column=0)
    button_clear.config(width=5, padx=5, pady=5, font=("default", 10))


setup_gui()

screen.mainloop()
