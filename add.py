import tkinter as tk
from tkinter import messagebox

class AdmissionSystemApp:
    def __init__(self, master):
        self.master = master
        master.title("Admission System")

        self.choice_var = tk.StringVar()

        # Create UI elements
        self.label = tk.Label(master, text="Choose an option:")
        self.label.pack()

        self.options = [
            "1. Register Student",
            "2. Submit Application",
            "3. Update Application Status",
            "4. View Application Status",
            "5. Communicate with Applicant",
            "6. Exit"
        ]

        for option in self.options:
            radio = tk.Radiobutton(master, text=option, variable=self.choice_var, value=option[0])
            radio.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.handle_choice)
        self.submit_button.pack()

        self.message_label = tk.Label(master, text="")
        self.message_label.pack()

    def handle_choice(self):
        choice = self.choice_var.get()
        
        if choice == "1":
            self.register_student()
        elif choice == "2":
            self.submit_application()
        elif choice == "3":
            self.update_application_status()
        elif choice == "4":
            self.view_application_status()
        elif choice == "5":
            self.communicate_with_applicant()
        elif choice == "6":
            self.master.quit()
        else:
            messagebox.showerror("Error", "Invalid choice, please try again.")

    def register_student(self):
        student_id = self.prompt_user("Enter student ID:")
        name = self.prompt_user("Enter student name:")
        email = self.prompt_user("Enter student email:")
        # Call the method to register the student
        admission_system.register_student(student_id, name, email)
        self.message_label.config(text="Student registered successfully.")

    def submit_application(self):
        student_id = self.prompt_user("Enter student ID:")
        program = self.prompt_user("Enter program:")
        # Call the method to submit application
        admission_system.submit_application(student_id, program)
        self.message_label.config(text="Application submitted successfully.")

    def update_application_status(self):
        student_id = self.prompt_user("Enter student ID:")
        status = self.prompt_user("Enter status:")
        # Call the method to update application status
        admission_system.update_application_status(student_id, status)
        self.message_label.config(text="Application status updated successfully.")

    def view_application_status(self):
        student_id = self.prompt_user("Enter student ID:")
        # Call the method to view application status
        status = admission_system.view_application_status(student_id)
        self.message_label.config(text=f"Application status: {status}")

    def communicate_with_applicant(self):
        student_id = self.prompt_user("Enter student ID:")
        message = self.prompt_user("Enter message:")
        # Call the method to communicate with applicant
        admission_system.communicate_with_applicant(student_id, message)
        self.message_label.config(text="Message sent to applicant.")

    def prompt_user(self, prompt):
        return simpledialog.askstring("Input", prompt)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdmissionSystemApp(root)
    root.mainloop()
