"""

Name: Taha Sarfraz
Date: jan 15th
Author: lil solar (taha)
Program: tetris brae login screen
Desc: This screen utilizes tkinter library to create windows that allow you to
login, register, read instructions on how to play the game, and play the game if
you login succesfully.
You can register an account, and proceed to login. The code is written so that if you
attempt to register another account, the old registration credientials are over written
with the newer ones.

Kendrick lamar is played in the background.
"""

import tkinter
import pygame
pygame.mixer.init()
pygame.mixer.music.load('loginscreenmusic.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
# How to play screen back button function.
def back_h2p():
    main_screen()
    window_h2p.destroy()


# Login screen back button function.
def back_login():
    window_log.destroy()


# Register screen back button function.
def back_register():
    window2.destroy()


# Adds log-in details to text file and deals with login screen entries.
def login_file():
    global window_log
    # converts the values in the text boxes into string for programming
    #                                       usage
    username2 = username.get()
    username2 = str(username2)
    password2 = password.get()
    password2 = str(password2)
    # vadliation for programmer
    x = username2 + " " + password2 + " is le user + pass"
    print(x)

    file_in_name = "login.txt"
    input_file = open(file_in_name, "r")
    line_read = input_file.readline()
    # boolean vars control whether or not user is allowed to access game
    user_accepted = False
    pass_accepted = False
    while line_read != "":
        # parsing
        line_read = line_read.split()
        print(line_read)
        # Username inputted vs username in file
        if line_read[1] == username2:
            print("Username accepted")
            user_accepted = True
        else:
            print("Incorrect username")
            user_accepted = False
        # Password inputted vs passowrd in file
        if line_read[3] == password2:
            print("Pass accepted")
            pass_accepted = True
        else:
            print("Incorrect password")
            pass_accepted = False

        line_read = input_file.readline()

    input_file.close()

    # Starts game
    if pass_accepted == True and user_accepted == True:
        # validation of user and pass if correct ^^
        prompt3 = tkinter.Label(
            window_log,
            justify="left",
            text="Logged in. You're good to go.",
            font=("oswald", 25, "bold"),
            bg="#2c3f4f",
            fg="red",
        )
        prompt3.place(relx=0.5, rely=0.45, anchor="c")
        import tetrisBrae.py  # imports tetris game
        exec(tetrisBrae.py)  # executes le file

        # ~~~~ ENSURE tetrisBrae.py IS IN THE SAME DIRECTORY
        # AS tetrisBraeLogin.py OR ELSE
        # CODE WILL NOT WORK ~~~~~~~
    # Tells user incorrect password was entered.
    else:
        prompt3 = tkinter.Label(
            window_log,
            justify="left",
            text="Error. Incorrect username and/or password!",
            font=("oswald", 20, "bold"),
            bg="#2c3f4f",
            fg="red",
        )
        prompt3.place(relx=0.5, rely=0.45, anchor="c")


# Creates files for registering account details.
def register_file():
    global reg_username
    global reg_password
    global register_done
    global window2
    # Sets values to string
    new_user_reg1 = reg_username.get()
    new_pass_reg1 = reg_password.get()
    new_user_reg = str(new_user_reg1)
    new_pass_reg = str(new_pass_reg1)

    file_in_name = "login.txt"
    file_out_name = "login.txt"
    output_file = open(file_out_name, "w")
    input_file = open(file_in_name, "r")

    line_read = input_file.readline()

    # adds info into the login.txt file
    user_info2 = "user " + new_user_reg + " pass " + new_pass_reg
    user_info = "user " + new_user_reg + " pass " + new_pass_reg
    output_file.write(user_info)
    # validation for if anything goes wrong while registering
    if user_info2 == user_info:
        print("registeration done")
        register_done = True

    else:
        print("Error. Try again.")
        register_done = False

    window2.destroy()
    login()


# Register screen
def register_user():
    global reg_username
    global reg_password
    global window2

    # all this is pretty self explanatory i think u can undestand this
    #       without me explaining

    window2 = tkinter.Tk()
    window2.geometry("800x800")
    window2.title("Register Screen")
    window2.configure(bg="#2c3f4f")  # blue grey background shown

    txt = tkinter.Label(
        window2,
        text="Set Account Details",
        bg="#2c3f4f",
        anchor="center",
        fg="black",
        width=18,
        font=("Oswald", 45, "bold"),
    )
    txt.place(relx=0.5, rely=0.32, anchor="c")

    register_title = tkinter.Label(
        window2,
        text="CREATE ACCOUNT",
        bg="#081016",
        anchor="center",
        fg="yellow",
        width=18,
        font=("Oswald", 55, "bold"),
    )
    register_title.place(relx=0.5, rely=0.18, anchor="c")

    username_txt = tkinter.Label(
        window2,
        text="Username:",
        bg="#2c3f4f",
        anchor="center",
        fg="black",
        width=9,
        font=("Oswald", 35, "bold"),
    )
    username_txt.place(relx=0.19, rely=0.45, anchor="c")

    reg_username = tkinter.Entry(
        window2, bg="light grey", font=("Oswald", 25), fg="black", width=20
    )
    reg_username.place(relx=0.58, rely=0.46, anchor="c")

    password_txt = tkinter.Label(
        window2,
        text="Password:",
        bg="#2c3f4f",
        anchor="center",
        fg="black",
        width=9,
        font=("Oswald", 35, "bold"),
    )
    password_txt.place(relx=0.19, rely=0.65, anchor="c")

    reg_password = tkinter.Entry(
        window2, bg="light grey", fg="black", font=("Oswald", 25), width=20
    )
    reg_password.place(relx=0.58, rely=0.66, anchor="c")

    reg_button = tkinter.Button(
        window2,
        text="Register",
        font=("Oswald", 30, "bold"),
        bg="yellow",
        fg="#081016",
        width=15,
        command=register_file,
    )
    reg_button.place(relx=0.55, rely=0.83, anchor="c")

    exit_button = tkinter.Button(
        window2,
        text="RETURN",
        width=8,
        font=("Oswald", 19, "bold"),
        bg="#26282a",
        fg="red",
        command=back_register,
    )
    exit_button.grid(row=0, column=0)

    window_log.destroy()


# Login screen
def login():

    global username
    global password
    global register_button
    global window_log

    # all this is pretty self explanatory i think u can undestand this
    #       without me explaining

    window_log = tkinter.Tk()
    window_log.geometry("800x800")
    window_log.title("Login Screen")
    window_log.configure(bg="#2c3f4f")

    login_title = tkinter.Label(
        window_log,
        text="ACCOUNT",
        bg="#081016",
        anchor="center",
        fg="yellow",
        width=11,
        font=("Oswald", 55, "bold"),
    )
    login_title.place(relx=0.63, rely=0.15, anchor="c")

    username = tkinter.Entry(window_log, bg="light grey", width=25, font=("Oswald", 25))
    username.place(relx=0.66, rely=0.36, anchor="c")

    username_txt = tkinter.Label(
        window_log,
        text="Username:",
        bg="#2c3f4f",
        anchor="center",
        fg="black",
        width=9,
        font=("Oswald", 35, "bold"),
    )
    username_txt.place(relx=0.2, rely=0.35, anchor="c")

    password = tkinter.Entry(
        window_log, bg="light grey", width=25, font=("Oswald", 25), fg="black"
    )
    password.place(relx=0.66, rely=0.57, anchor="c")

    password_txt = tkinter.Label(
        window_log,
        text="Password:",
        bg="#2c3f4f",
        anchor="center",
        fg="black",
        width=9,
        font=("Oswald", 35, "bold"),
    )
    password_txt.place(relx=0.2, rely=0.57, anchor="c")

    log_button = tkinter.Button(
        window_log,
        text="Login",
        font=("Oswald", 25, "bold"),
        width=20,
        fg="#081016",
        bg="yellow",
        command=login_file,
    )
    log_button.place(relx=0.6, rely=0.73, anchor="c")

    exit_button = tkinter.Button(
        window_log,
        text="RETURN TO MAIN SCREEN",
        font=("Oswald", 19, "bold"),
        bg="#26282a",
        fg="red",
        width=23,
        command=back_login,
    )
    exit_button.grid(row=0, column=0)

    register_button = tkinter.Button(
        window_log,
        text="Register",
        fg="#081016",
        bg="yellow",
        font=("Oswald", 25, "bold"),
        command=register_user,
        width=20,
    )
    register_button.place(relx=0.6, rely=0.86, anchor="c")


# How to play screen.
def how_to_play2():
    global window_h2p

    # all this is pretty self explanatory i think u can undestand this
    #       without me explaining

    window_h2p = tkinter.Tk()
    window_h2p.geometry("850x600")
    window_h2p.configure(bg="#2c3f4f")

    h2p_title = tkinter.Label(
        window_h2p,
        text="HOW TO PLAY",
        bg="#081016",
        anchor="center",
        fg="yellow",
        width=15,
        font=("Oswald", 55, "bold"),
    )
    h2p_title.place(relx=0.5, rely=0.15, anchor="c")

    h2p = tkinter.Label(
        window_h2p,
        text="""
                This program utilizes the Pygame library to create a functional Tetris game.
                The game includes a grid for the Tetrominoes to fall and stack on,
                a next piece preview, and a system for clearing full rows.
                The player can move and rotate the falling Tetromino using the arrow keys,
                  and the game ends if a Tetromino is unable to fit onto the grid.

                                        """,
        bg="black",
        fg="white",
        font=("Oswald", 16),
        relief="raised",
        width=85,
        height=11,
    )
    h2p.place(relx=0.5, rely=0.63, anchor="c")

    back_button = tkinter.Button(
        window_h2p,
        text="RETURN",
        width=8,
        font=("Oswald", 19, "bold"),
        bg="#26282a",
        fg="red",
        command=back_h2p,
    )
    back_button.grid(row=0, column=0)

    window.destroy()


# Main screen.
def main_screen():
    global window

    window = tkinter.Tk()
    window.title("Tetris Brae")
    window.geometry("800x800")

    window.configure(bg="#2c3f4f")

    text = tkinter.Label(
        window,
        text="Tetris Brae",
        bg="#081016",
        anchor="center",
        fg="yellow",
        font=("Oswald", 70, "bold"),
        width=13,
    )
    text.place(relx=0.5, rely=0.1, anchor="c")

    start_button = tkinter.Button(
        window,
        text="BEGIN",
        bg="yellow",
        fg="#081016",
        anchor="center",
        relief="raised",
        font=("Oswald", 45),
        width=9,
        command=login,
    )
    start_button.place(relx=0.5, rely=0.4, anchor="c")

    how_to_play = tkinter.Button(
        window,
        text="HOW TO PLAY",
        bg="yellow",
        anchor="center",
        relief="raised",
        font=("Oswald", 45),
        width=15,
        command=how_to_play2,
        fg="#081016",
    )
    how_to_play.place(relx=0.5, rely=0.7, anchor="c")


# Program begins.
main_screen()
