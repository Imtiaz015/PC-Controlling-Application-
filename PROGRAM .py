import tkinter as tk
import tkinter.messagebox as messagebox
import subprocess
import time
from datetime import date
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fullscreen Black Background Interface")
        self.configure(background='black')

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        self.default_message = "Type Your Command Here"
        self.create_widgets()

    def create_widgets(self):
        heading = tk.Label(self, text="Enter Any Command To Execute ", fg="white", bg="black", font=("Arial", 24))
        heading.pack(pady=(50, 20))

        frame = tk.Frame(self, bg="white", bd=2)
        frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER, relwidth=0.9, height=40)

        send_icon = tk.PhotoImage(file="2.png").subsample(6)
        send_button = tk.Button(frame, image=send_icon, command=self.submit_message, bd=0, bg="white")
        send_button.image = send_icon
        send_button.pack(side="right")

        self.entry = tk.Entry(frame, font=("Arial", 14), bd=0, relief=tk.FLAT, bg="black", fg="grey", justify=tk.CENTER, insertbackground="white")
        self.entry.pack(fill="both", expand=True, side="right")
        self.entry.insert(tk.END, self.default_message)

        self.entry.bind("<FocusIn>", self.clear_default_message)
        self.entry.bind("<FocusOut>", self.restore_default_message)
        self.entry.bind("<Return>", self.submit_message)

        button_frame = tk.Frame(self, bg="black")
        button_frame.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

        show_developer_data_button = tk.Button(button_frame, text="Show Developer Data", command=self.show_developer_info, bg="black", fg="white", font=("Arial", 12, "bold"))
        show_developer_data_button.grid(row=0, column=0, padx=10)

        show_commands_button = tk.Button(button_frame, text="Show Commands", command=self.show_commands, bg="black", fg="white", font=("Arial", 12, "bold"))
        show_commands_button.grid(row=0, column=1, padx=10)

        contact_button = tk.Button(button_frame, text="Contact", command=self.open_email_client, bg="black", fg="white", font=("Arial", 12, "bold"))
        contact_button.grid(row=0, column=2, padx=10)

    def clear_default_message(self, event=None):
        if self.entry.get() == self.default_message and self.entry == self.focus_get():
            self.entry.delete(0, tk.END)
            self.entry.config(fg="white")
            self.entry.blink_cursor()

    def restore_default_message(self, event=None):
        if not self.entry.get():
            self.entry.insert(tk.END, self.default_message)
            self.entry.config(fg="grey")
            self.entry.stop_blink_cursor()

    def execute_command(self, command):
        try:
            if command.startswith("shutdown"):
                os.system("shutdown /s /t 1")
            elif command.startswith("restart"):
                os.system("shutdown /r /t 1")
            else:
                subprocess.run(command, shell=True)
        except Exception as e:
            print("Error executing command:", e)

    def open_platform(self, platform):
        platforms = {
            "google": "https://www.google.com",
            "facebook": "https://www.facebook.com",
            "chrome": "chrome",
            "youtube": "https://www.youtube.com",
            "twitter": "https://twitter.com",
            "yahoo": "https://www.yahoo.com",
            "chatgpt": "https://www.openai.com/chatgpt",
            "instagram": "https://www.instagram.com",
            "whatsapp": "https://web.whatsapp.com",
            "tiktok": "https://www.tiktok.com",
            "amazon": "https://www.amazon.com",
            "linkedin": "https://www.linkedin.com",
            "openai": "https://www.openai.com",
            "netflix": "https://www.netflix.com",
            "w3school": "https://www.w3schools.com",
            "microsoft365": "start https://www.office.com",
            "microsoftbing": "start https://www.bing.com",
            "blackboxai": "start https://www.blackboxai.com",
            "microsoft": "start https://www.microsoft.com",
            "wikipedia": "start https://www.wikipedia.org",
            "telegram": "start https://web.telegram.org",
            "zoom": "start zoom",
            "sleep": "rundll32.exe powrprof.dll,SetSuspendState 0,1,0",
            "controlpanel": "control panel",
            "mswinword": "start winword",
            "mspowerpnt": "start powerpnt",
            "msexcel": "start excel",
            "msdos": "start cmd",
            "popup": "msg * Developed By Imtiaz Ali Maitlo",
            "calendar": "start outlookcal:",
            "calculator": "calc",
            "time": lambda: self.execute_command(f"msg * Current Time: {time.strftime('%H:%M:%S')}"),
            "date": lambda: self.execute_command(f"msg * Current Date: {date.today()}"),
            "homescreen": "explorer.exe /n",
        }
        if platform in platforms:
            action = platforms[platform]
            if callable(action):
                action()  # Execute function directly
            elif action.startswith("https://"):
                self.execute_command(f"start {action}")  # Open URL in browser
            else:
                self.execute_command(action)  # Open command (e.g., Chrome)
        else:
            messagebox.showinfo("Command Not Found", "That command does not exist")

    def submit_message(self, event=None):
        command = self.entry.get().strip()
        if command:
            if command.startswith("open "):
                platform = command.split(" ", 1)[1]
                self.open_platform(platform)
            else:
                self.execute_command(command)
        self.restore_default_message()

    def blink_cursor(self):
        cursor_index = self.entry.index(tk.INSERT)
        self.entry.config(insertofftime=300)  # Hide cursor
        self.entry.after(300, lambda: self.show_cursor(cursor_index))

    def show_cursor(self, cursor_index):
        self.entry.config(insertofftime=0)  # Show cursor
        self.entry.after(300, lambda: self.blink_cursor())

    def stop_blink_cursor(self):
        self.entry.config(insertofftime=0)  # Show cursor

    def show_developer_info(self):
        developer_info = "Name : Imtiaz Ali Maitlo\nContact : maitloimtiazali36@gmail.com\nDeveloper Level : Basic Level"
        messagebox.showinfo("Developer Information", developer_info)

    def show_commands(self):
        commands = [
            "google", "facebook", "chrome", "youtube", "twitter", "yahoo", "chatgpt", "instagram", "whatsapp", "tiktok",
            "amazon", "linkedin", "openai", "netflix", "w3school", "microsoft365", "microsoftbing", "blackboxai",
            "microsoft", "wikipedia", "telegram", "zoom", "restart", "shutdown", "sleep", "controlpanel", "mswinword",
            "mspowerpnt", "msexcel", "msdos", "popup", "calendar", "calculator", "time", "date", "homescreen"
        ]
        commands_text = "\n".join(commands)
        messagebox.showinfo("Available Commands", commands_text)

    def open_email_client(self):
        recipient_email = "maitloimtiazali36@gmail.com"
        subject = "Contact Inquiry"
        body = "Dear Imtiaz,\n\nI would like to get in touch regarding..."
        mailto_link = f"mailto:{recipient_email}?subject={subject}&body={body}"

        try:
            os.system(mailto_link)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open email client: {e}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
