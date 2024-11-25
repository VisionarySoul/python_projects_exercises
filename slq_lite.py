import sqlite3
import random
import tkinter
import messagebox

connect = sqlite3.connect("database.db")

cursor = connect.cursor()


def add():
    cursor.execute("DROP TABLE User");
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS User(id INTEGER PRIMARY KEY AUTOINCREMENT, website TEXT, email TEXT,password TEXT);")
    cursor.execute(f"INSERT INTO User(id,website,email,password) VALUES (?,?,?,?)",
                   [1, f"{website.get()}", f"{email.get()}", f"{password.get()}"])
    tables = cursor.execute("SELECT * FROM User")
    for table in tables:
        print(table)
    connect.commit()
    # connect.close()
    return cursor


def generate_password():
    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    list_chars = ["/", "*", "@", "-", "-", "(", ")", "=", "%", "$", "#", "!", "~"]
    list_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    generate = random.choice([list_numbers, list_chars, list_letters])
    password_random = "".join(generate[:8])
    password.insert(0, password_random)


def search_website():
    search = cursor.execute(f"SELECT * FROM User WHERE website LIKE '%{find.get()}%' ")
    field = search.fetchone()
    messagebox.showinfo(title="Search", message=f"email:{field[1]} password:{field[2]}")
    connect.commit()
    # connect.close()
    return cursor


screen = tkinter.Tk()
screen.title("Generate Password")
screen.geometry("500x400")

img_path = "image.png"
image = tkinter.PhotoImage(file=img_path)
image_label = tkinter.Label(screen, image=image)
image_label.grid(row=0, column=1, columnspan=4, padx=10)

email_label = tkinter.Label(text="Email/Username")
email_label.grid(row=1, column=0)
email = tkinter.Entry()
email.grid(row=1, column=2, columnspan=4, padx=10)
email.config(width=20, font=("default", 14))

website_label = tkinter.Label(text="Website")
website_label.grid(row=3, column=0)
website = tkinter.Entry()
website.grid(row=3, column=2, columnspan=4, padx=10)
website.config(width=20, font=("default", 14))

password_label = tkinter.Label(text="Password")
password_label.grid(row=2, column=0)
password = tkinter.Entry()
password.grid(row=2, column=2, columnspan=4, padx=10)
password.config(width=20, font=("default", 14))

button_add = tkinter.Button(text="Add", command=add)
button_add.grid(row=4, column=0, columnspan=4, padx=10)
button_add.config(width=5, padx=5, pady=5, font=("default", 10))

generate_pass = tkinter.Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=4, columnspan=6, padx=10)
generate_pass.config(width=15, padx=5, pady=5, font=("default", 10))

search_label = tkinter.Label(text="Search")
search_label.grid(row=5, column=1)
find = tkinter.Entry()
find.grid(row=5, column=3, columnspan=4, padx=10)
find.config(width=20, font=("default", 14))

search_button = tkinter.Button(text="Search", command=search_website)
search_button.grid(row=5, column=4, columnspan=6, padx=10)
search_button.config(width=15, padx=5, pady=5, font=("default", 10))

screen.mainloop()
