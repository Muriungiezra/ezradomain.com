from tkinter import *
from tkinter import messagebox
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
from PIL import Image, ImageTk

bot = ChatBot('Bot')
trainer = ListTrainer(bot)
for files in os.listdir('Data/data_main/'):
    data = open('Data/data_main/' + files, 'r', encoding='utf-8').readlines()

    trainer.train(data)


def login():
    # Create a new login window
    login_window = Toplevel()
    login_window.title('Login')
    login_window.geometry('800x600')
    login_window.resizable(False, False)

    username_label = Label(login_window, text='Username:')
    username_label.pack()

    username_entry = Entry(login_window)
    username_entry.pack()

    password_label = Label(login_window, text='Password:')
    password_label.pack()

    password_entry = Entry(login_window, show='*')
    password_entry.pack()

    def check_credentials():
        # Get the username and password input from the user
        username = username_entry.get()
        password = password_entry.get()

        # Compare the input with pre-defined credentials
        if username == "ezra" and password == "1234":
            # Show a success message if the credentials are correct
            messagebox.showinfo("Success", "Login successful")
            # Close the login window and open the main window for the chatbot
            login_window.destroy()
            main_window()
        else:
            # Show an error message if the credentials are incorrect
            messagebox.showerror("Error", "Incorrect username or password")

    login_button = Button(login_window, text='Login', command=check_credentials)
    login_button.pack()


def main_window():
    root = Tk()
    root.geometry("500x570+100+30")
    root.title('chatbot created by MR EZRA MURIUNGI ')
    root.config(bg='green')


    centerFrame = Frame(root)
    centerFrame.pack()

    scrollbar = Scrollbar(centerFrame)
    scrollbar.pack(side=RIGHT)

    textarea = Text(centerFrame, font=('times new roman', 20, 'bold'), height=10
                    , wrap='word')
    textarea.pack(side=LEFT)
    scrollbar.config(command=textarea.yview)

    questionField = Entry(root, font=('verdana', 20, 'bold'))
    questionField.pack(pady=15, fill=X)

    def botReply():
        question = questionField.get()
        answer = bot.get_response(question)
        textarea.insert(END, 'you: ' + question + '\n\n')

        textarea.insert(END, 'Bot: ' + str(answer) + '\n\n')
        pyttsx3.speak(answer)
        questionField.delete(0, END)

    def photoImage(file):
        image = Image.open(file)
        photo = ImageTk.PhotoImage(image)
        return photo

    def photoImage(file):
        pass
    askpic = photoImage('C:/Users/pro/Downloads/sent.gif')

    askButton = Button(root, image=askpic,command=botReply)
    askButton.pack()

    root.mainloop()

# Add a button to the main file that opens the login page
root = Tk()
login_button = Button(root, text ='Login', command=login)
login_button.pack()
root.mainloop()
