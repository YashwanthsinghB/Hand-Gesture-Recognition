import tkinter as tk
import subprocess

class App:
    def __init__(self, master):
        self.master = master
        master.title("Hand Gesture Recognition System")
        master.config(bg="#f2d024")  # Set background color to yellow

        # Create a frame for better organization
        self.frame = tk.Frame(master, bg="#f2d024")
        self.frame.pack(pady=20)

        # Add title label
        self.title_label = tk.Label(self.frame, text="Hand Gesture Recognition System", font=("Arial", 24, "bold"), bg="#f2d024", fg="black")
        self.title_label.grid(row=0, columnspan=2, pady=10)

        # Add headings
        headings = [
            "DR. T. THIMMAIAH INSTITUTE OF TECHNOLOGY",
            "An Improved Approach for Assisting Multi-Sensory Impaired People using Machine Learning Techniques",
            "Under the Guidance of",
            "Dr. Sreedhar Kumar S & Prof. Sangeetha V"
        ]
        for i, heading_text in enumerate(headings, start=1):
            heading = tk.Label(self.frame, text=heading_text, font=("Arial", 16), bg="#f2d024", fg="black")
            heading.grid(row=i, columnspan=2, pady=5)

        # Add buttons with black text on yellow background
        button_texts = ["Input", "Identifying Hand Landmarks", "Feature Extraction", "Predict Hand Gestures"]
        button_commands = [self.run_file1, self.run_file2, self.run_file3, self.run_file4]

        for i, (text, command) in enumerate(zip(button_texts, button_commands), start=len(headings) + 1):
            button = tk.Button(self.frame, text=text, command=command, font=("Arial", 14), bg="#000000", fg="#f2d024",
                               activebackground="#f2d024", activeforeground="#000000", padx=10, pady=5)
            button.grid(row=i, columnspan=2, pady=10, padx=50, sticky="we")
            button.bind("<Enter>", lambda event, btn=button: btn.config(bg="#ffd400", fg="#000000"))  # Hover effect
            button.bind("<Leave>", lambda event, btn=button: btn.config(bg="#000000", fg="#f2d024"))  # Restore original color

    def run_file1(self):
        subprocess.run(['python3', '/Users/yashwanthsingh/Desktop/hand-gesture-recognition-main/hand-gesture-recognition-main/get_image.py'])

    def run_file2(self):
        subprocess.run(['python3', '/Users/yashwanthsingh/Desktop/hand-gesture-recognition-main/hand-gesture-recognition-main/test_mediapipe.py'])

    def run_file3(self):
        subprocess.run(['python3', '/Users/yashwanthsingh/Desktop/hand-gesture-recognition-main/hand-gesture-recognition-main/get_data.py'])

    def run_file4(self):
        subprocess.run(['python3', '/Users/yashwanthsingh/Desktop/hand-gesture-recognition-main/hand-gesture-recognition-main/hands_gesture_recog.py'])

root = tk.Tk()
app = App(root)
root.mainloop()
