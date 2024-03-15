import os
import threading
import time
import tkinter as tk
from tkinter import filedialog, messagebox, font


class FileWritingApp:
    def __init__(self, master):
        self.master = master
        master.title('ZED recording')

        window_width = 500
        window_height = 200

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        center_x = int((screen_width/2) - (window_width / 2))
        center_y = int((screen_height/2) - (window_height / 2))
        master.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        bold_font = font.Font(weight='bold')
        self.cwd_label_text = tk.StringVar()
        self.cwd_label_text.set('Current Working Directory: ' + os.getcwd())
        self.cwd_label = tk.Label(master, textvariable=self.cwd_label_text, font=bold_font)
        self.cwd_label.pack()

        self.change_dir_button = tk.Button(
            master,
            text='Change Directory',
            command=self.change_directory,
        )
        self.change_dir_button.pack()

        self.file_name_label = tk.Label(master, text='Enter File Name:')
        self.file_name_label.pack()

        self.file_name_entry = tk.Entry(master)
        self.file_name_entry.pack()

        self.start_button = tk.Button(master, text='Start', command=self.start_writing)
        self.start_button.pack()

        self.stop_button = tk.Button(
            master,
            text='Stop',
            command=self.stop_writing,
            state=tk.DISABLED,
        )
        self.stop_button.pack()

        self.time_elapsed = tk.StringVar()
        self.time_elapsed.set('Time: 0 seconds')
        self.time_label = tk.Label(master, textvariable=self.time_elapsed)
        self.time_label.pack()

        self.exit_button = tk.Button(master, text='Exit', command=self.exit_app)
        self.exit_button.pack()

        self.is_writing = False
        self.start_time = None

    def change_directory(self):
        new_dir = filedialog.askdirectory()
        if new_dir:
            os.chdir(new_dir)
            self.cwd_label_text.set('Current Working Directory: ' + os.getcwd())

    def start_writing(self):
        self.file_name = self.file_name_entry.get()
        if self.file_name:
            if os.path.exists(self.file_name):
                messagebox.showerror('Error', 'File already exists. Please enter a different name.')
                return
            self.is_writing = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.file_name_entry.config(state=tk.DISABLED)
            self.change_dir_button.config(state=tk.DISABLED)
            self.write_thread = threading.Thread(target=self.write_numbers)
            self.write_thread.start()
            self.start_time = time.time()

        else:
            messagebox.showerror('Error', 'Please enter a file name.')
            return

    def stop_writing(self):
        self.is_writing = False
        self.write_thread.join()
        self.write_thread = None
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.file_name_entry.config(state=tk.NORMAL)
        self.change_dir_button.config(state=tk.NORMAL)
        self.time_elapsed.set('Time: 0 seconds')

    def write_numbers(self):
        with open(self.file_name, 'w') as f:
            i = 1
            while self.is_writing:
                f.write(f'{i}\n')
                f.flush()
                elapsed_time = int(time.time() - self.start_time)
                self.time_elapsed.set(f'Time: {elapsed_time} seconds')
                self.master.update_idletasks()
                i += 1
                time.sleep(1)

    def exit_app(self):
        if self.is_writing:
            self.stop_writing()
        self.master.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = FileWritingApp(root)
    root.mainloop()
