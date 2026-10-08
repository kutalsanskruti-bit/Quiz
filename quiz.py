import tkinter as tk
from tkinter import messagebox
import random



questions = [
    {
        "question": "Which language is used for AI and Machine Learning?",
        "options": ["HTML", "Python", "CSS", "SQL"],
        "answer": "Python"
    },

    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Control Processing Unit"
        ],
        "answer": "Central Processing Unit"
    },

    {
        "question": "Which data structure follows FIFO?",
        "options": ["Stack", "Tree", "Queue", "Graph"],
        "answer": "Queue"
    },

    {
        "question": "Which protocol is used for secure web communication?",
        "options": ["HTTP", "FTP", "HTTPS", "SMTP"],
        "answer": "HTTPS"
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    }
]


random.shuffle(questions)




current_question = 0
score = 0
player_name = ""
selected_answer = ""




root = tk.Tk()

root.title("Python Computer Quiz")

root.geometry("850x700")

root.resizable(False, False)

root.configure(bg="#0f172a")




def clear_window():

    for widget in root.winfo_children():
        widget.destroy()




def show_welcome():

    clear_window()

    title = tk.Label(
        root,
        text="PYTHON COMPUTER QUIZ",
        font=("Arial", 30, "bold"),
        bg="#0f172a",
        fg="#38bdf8"
    )

    title.pack(pady=(80, 20))


    subtitle = tk.Label(
        root,
        text="Test Your Computer Science Knowledge!",
        font=("Arial", 17),
        bg="#0f172a",
        fg="#cbd5e1"
    )

    subtitle.pack(pady=10)


    name_label = tk.Label(
        root,
        text="Enter Your Name",
        font=("Arial", 15, "bold"),
        bg="#0f172a",
        fg="white"
    )

    name_label.pack(pady=(50, 10))


    name_entry = tk.Entry(
        root,
        width=28,
        font=("Arial", 16),
        justify="center",
        bg="#1e293b",
        fg="white",
        insertbackground="white",
        relief="flat"
    )

    name_entry.pack(ipady=10)


    def start_quiz():

        global player_name

        player_name = name_entry.get().strip()

        if player_name == "":
            messagebox.showwarning(
                "Name Required",
                "Please enter your name."
            )
            return

        show_quiz()


    start_button = tk.Button(
        root,
        text="START QUIZ",
        font=("Arial", 15, "bold"),
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=45,
        pady=12,
        command=start_quiz
    )

    start_button.pack(pady=35)


    info = tk.Label(
        root,
        text="5 Questions  |  Multiple Choice  |  Instant Results",
        font=("Arial", 11),
        bg="#0f172a",
        fg="#94a3b8"
    )

    info.pack()


# =========================================================
# QUIZ SCREEN
# =========================================================

def show_quiz():

    global selected_answer

    selected_answer = ""

    clear_window()

    

    header = tk.Frame(
        root,
        bg="#111827"
    )

    header.pack(
        fill="x",
        padx=30,
        pady=(20, 10)
    )


    question_number = tk.Label(
        header,
        text=f"Question {current_question + 1} of {len(questions)}",
        font=("Arial", 15, "bold"),
        bg="#111827",
        fg="#38bdf8"
    )

    question_number.pack(
        side="left",
        padx=20,
        pady=15
    )


    score_text = tk.Label(
        header,
        text=f"Score: {score}",
        font=("Arial", 15, "bold"),
        bg="#111827",
        fg="#22c55e"
    )

    score_text.pack(
        side="right",
        padx=20,
        pady=15
    )


   
    progress_background = tk.Frame(
        root,
        bg="#334155",
        height=8
    )

    progress_background.pack(
        fill="x",
        padx=50,
        pady=(0, 20)
    )


    progress_value = (
        current_question + 1
    ) / len(questions)


    progress_fill = tk.Frame(
        progress_background,
        bg="#38bdf8"
    )

    progress_fill.place(
        x=0,
        y=0,
        relwidth=progress_value,
        relheight=1
    )


    

    question_text = tk.Label(
        root,
        text=questions[current_question]["question"],
        font=("Arial", 21, "bold"),
        bg="#0f172a",
        fg="white",
        wraplength=720,
        justify="center"
    )

    question_text.pack(
        pady=(20, 25)
    )


    

    options_frame = tk.Frame(
        root,
        bg="#0f172a"
    )

    options_frame.pack(
        fill="x",
        padx=80
    )


    option_buttons = []


    def select_answer(answer, button):

        global selected_answer

        selected_answer = answer

        # Reset all buttons
        for item in option_buttons:

            item.configure(
                bg="#1e293b",
                fg="white"
            )

        # Highlight selected button
        button.configure(
            bg="#2563eb",
            fg="white"
        )


    for option in questions[current_question]["options"]:

        button = tk.Button(
            options_frame,
            text=option,
            font=("Arial", 13),
            bg="#1e293b",
            fg="white",
            activebackground="#2563eb",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            anchor="w",
            padx=20,
            pady=10
        )

        button.pack(
            fill="x",
            pady=4
        )


        button.configure(
            command=lambda answer=option, btn=button:
            select_answer(answer, btn)
        )


        option_buttons.append(button)


    

    def submit_answer():

        global current_question
        global score

        if selected_answer == "":

            messagebox.showwarning(
                "Select Answer",
                "Please select an answer first."
            )

            return


        correct_answer = questions[current_question]["answer"]


        # Check answer
        if selected_answer == correct_answer:

            score += 1

            messagebox.showinfo(
                "Correct!",
                "Correct Answer!"
            )

        else:

            messagebox.showerror(
                "Wrong Answer",
                "Wrong Answer!\n\n"
                "Correct Answer: " + correct_answer
            )


        # Move to next question
        current_question += 1


        if current_question < len(questions):

            show_quiz()

        else:

            show_result()


    submit_button = tk.Button(
        root,
        text="SUBMIT ANSWER",
        font=("Arial", 14, "bold"),
        bg="#22c55e",
        fg="white",
        activebackground="#16a34a",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=45,
        pady=11,
        command=submit_answer
    )

    submit_button.pack(
        pady=18
    )




def show_result():

    clear_window()

    percentage = (
        score / len(questions)
    ) * 100


    title = tk.Label(
        root,
        text="QUIZ COMPLETED!",
        font=("Arial", 30, "bold"),
        bg="#0f172a",
        fg="#38bdf8"
    )

    title.pack(
        pady=(70, 20)
    )


    name_label = tk.Label(
        root,
        text=f"Well Done, {player_name}!",
        font=("Arial", 21, "bold"),
        bg="#0f172a",
        fg="white"
    )

    name_label.pack(
        pady=10
    )


    score_label = tk.Label(
        root,
        text=f"{score} / {len(questions)}",
        font=("Arial", 48, "bold"),
        bg="#0f172a",
        fg="#22c55e"
    )

    score_label.pack(
        pady=15
    )


    percentage_label = tk.Label(
        root,
        text=f"Percentage: {percentage:.2f}%",
        font=("Arial", 19),
        bg="#0f172a",
        fg="#cbd5e1"
    )

    percentage_label.pack(
        pady=10
    )


    # Performance message
    if percentage >= 80:

        performance = "Excellent Performance!"
        performance_color = "#22c55e"

    elif percentage >= 60:

        performance = "Good Performance!"
        performance_color = "#38bdf8"

    elif percentage >= 40:

        performance = "Keep Practicing!"
        performance_color = "#facc15"

    else:

        performance = "Need More Practice!"
        performance_color = "#ef4444"


    performance_label = tk.Label(
        root,
        text=performance,
        font=("Arial", 19, "bold"),
        bg="#0f172a",
        fg=performance_color
    )

    performance_label.pack(
        pady=20
    )


    # -----------------------------------------------------
    # PLAY AGAIN
    # -----------------------------------------------------

    def play_again():

        global current_question
        global score

        current_question = 0
        score = 0

        random.shuffle(questions)

        show_welcome()


    play_button = tk.Button(
        root,
        text="PLAY AGAIN",
        font=("Arial", 15, "bold"),
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=45,
        pady=12,
        command=play_again
    )

    play_button.pack(
        pady=30
    )




show_welcome()

root.mainloop()