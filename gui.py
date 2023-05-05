import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from tkinter import font
from main_data_maps import mainGoogleMaps

class FileChooserWindow:
    def __init__(self, parent, input_style, label_font, button_font, ch_font):
        self.parent = parent
        self.frame = tk.Frame(self.parent, bg="white")
        self.frame.pack(fill="both", expand=True)
        self.input_style = input_style
        self.label_font = label_font
        self.btn_font = button_font
        self.file_path = tk.StringVar()
        self.file_path.set("Select Keyword File")

        self.label1 = tk.Label(self.frame, text="Choose the keyword file:", font=self.label_font, bg="white")
        self.label1.pack(pady=10)

        self.path_entry = tk.Entry(self.frame, textvariable=self.file_path, **self.input_style)
        self.path_entry.pack(pady=0)

        self.browse_button = tk.Button(self.frame, text="Browse", font=self.btn_font, bg="#1dbf73", fg="white", width=30 ,height=1, command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.next_button = tk.Button(self.frame, text="Next", font=self.btn_font, bg="#1dbf73", fg="white", width=30 ,height=1, command=self.next_window)
        self.next_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Choose a file")
        if file_path:
            self.file_path.set(file_path)

    def next_window(self):
        path = self.file_path.get()
        if not path.endswith('.txt'):
            messagebox.showerror("Error", "The file must be a txt file")
            return

        if not os.path.exists(path):
            messagebox.showerror("Error", "File path is invalid!")
            return

        self.frame.destroy()
        FileNameWindow(self.parent, path, self.input_style, self.label_font, self.btn_font, ch_font)


class FileNameWindow:
    def __init__(self, parent, file_path, input_style, label_font, btn_font, ch_font):
        self.parent = parent
        self.file_path = file_path
        self.input_style = input_style
        self.label_font = label_font
        self.btn_font = btn_font
        self.ch_font = ch_font

        self.frame = tk.Frame(self.parent, bg="white")
        self.frame.pack(fill="both", expand=True)

        self.file_name = tk.StringVar()
        self.file_name.set("output file name")

        self.label1 = tk.Label(self.frame, text="Enter a Output file name:", font=self.label_font, bg="white")
        self.label1.pack(pady=10)

        self.name_entry = tk.Entry(self.frame, textvariable=self.file_name, **self.input_style)
        self.name_entry.pack(pady=10)

        # create the checkboxes input field
        self.label_checkboxes = tk.Label(self.frame, text="Select Parameters:", font=self.label_font, bg="white")
        self.label_checkboxes.pack(pady=10)
        self.check_var1 = tk.BooleanVar()
        self.check_var2 = tk.BooleanVar()
        self.check_var3 = tk.BooleanVar()
        self.check_var4 = tk.BooleanVar()
        self.check_var5 = tk.BooleanVar()
        self.check_var6 = tk.BooleanVar()
        self.check_var7 = tk.BooleanVar()
        self.check_var8 = tk.BooleanVar()
        self.checkbox1 = tk.Checkbutton(self.frame, text="Category", font=self.ch_font, variable=self.check_var1, bg="white")
        self.checkbox2 = tk.Checkbutton(self.frame, text="Title", font=self.ch_font, variable=self.check_var2, bg="white"   )
        self.checkbox3 = tk.Checkbutton(self.frame, text="Rating", font=self.ch_font, variable=self.check_var3, bg="white"   )
        self.checkbox4 = tk.Checkbutton(self.frame, text="Description", font=self.ch_font, variable=self.check_var4, bg="white"   )
        self.checkbox5 = tk.Checkbutton(self.frame, text="Address", font=self.ch_font, variable=self.check_var5, bg="white" )
        self.checkbox6 = tk.Checkbutton(self.frame, text="Hours", font=self.ch_font, variable=self.check_var6, bg="white"   )
        self.checkbox7 = tk.Checkbutton(self.frame, text="Website", font=self.ch_font, variable=self.check_var7, bg="white" )
        self.checkbox8 = tk.Checkbutton(self.frame, text="Phone", font=self.ch_font, variable=self.check_var8, bg="white"   )
        self.checkbox1.pack(padx=10)
        self.checkbox2.pack(padx=10)
        self.checkbox3.pack(padx=10)
        self.checkbox4.pack(padx=10)
        self.checkbox5.pack(padx=10)
        self.checkbox6.pack(padx=10)
        self.checkbox7.pack(padx=10)
        self.checkbox8.pack(padx=10)

        # create the file radio buttons field
        self.label_file_type = tk.Label(self.frame, text="Chose Output File type:", font=self.label_font, bg="white")
        self.label_file_type.pack(pady=10)
        self.file_type_var = tk.StringVar(value="XLSX")
        self.radio_xlsx = tk.Radiobutton(self.frame, text="XLSX", font=self.ch_font, variable=self.file_type_var, value="XLSX", bg="white")
        self.radio_csv = tk.Radiobutton(self.frame, text="CSV", font=self.ch_font, variable=self.file_type_var, value="CSV", bg="white")
        self.radio_sql = tk.Radiobutton(self.frame, text="SQL", font=self.ch_font, variable=self.file_type_var, value="SQL", bg="white")
        self.radio_json = tk.Radiobutton(self.frame, text="JSON", font=self.ch_font, variable=self.file_type_var, value="JSON", bg="white")
        self.radio_xlsx.pack( padx=10)
        self.radio_csv.pack(padx=10)
        self.radio_sql.pack(padx=10)
        self.radio_json.pack( padx=10)

        self.start_button = tk.Button(self.frame, text="Submit", font=self.btn_font, bg="#1dbf73", fg="white", width=30 ,height=1,command=self.submit_ntwd)
        self.start_button.pack(pady=10)


    def submit_ntwd(self):
        # get the values of the input fields
        file_name = self.file_name.get()
        output_name = self.name_entry.get()
        file_type = self.file_type_var.get()
        checkboxes = [self.check_var1.get(), self.check_var2.get(), self.check_var3.get(), self.check_var4.get(), self.check_var5.get(), self.check_var6.get(), self.check_var7.get(), self.check_var8.get()]
        
        para = ["Category", "Title", "Rating", "Description", "Address","Hours", "Website",  "Phone"]
        dictionary = dict(zip(para, checkboxes))
        if not file_name:
            messagebox.showerror("Error", "File name cannot be empty!")
            return
        # self.frame.destroy

        # validate the input fields
        if not self.file_path or not any(checkboxes) or not output_name or not file_type:
            messagebox.showerror("Error", "Please fill all required fields.")
            # self.status_label.config(text="Please fill all required fields.")
            return

        # perform some action with the input values
        # print(f"File path: {self.file_path}")
        # print(f"Output file name: {output_name}")
        # print(f"File type: {file_type}")
        # print(f"Parameters: {dictionary}")


        self.frame.destroy()
        startProgramWindow(self.parent, self.file_path,output_name+"."+file_type, dictionary, self.btn_font)



class startProgramWindow:
    def __init__(self, parent, file_path, output_file_name, para,btn_font):
        # super().__init__(parent)
        self.parent = parent
        self.file_path = file_path
        self.file_name = output_file_name
        self.para = para
        self.btn_font = btn_font


        self.frame = tk.Frame(self.parent, bg="white")
        self.frame.pack(fill="both", expand=True)
        # self.title("Start Program")
        # Create a Label widget to display file_path
        file_path_label = tk.Label(self.frame, text=f"File path: {self.file_path}", bg="white")
        file_path_label.pack(pady=30)
        
        # Create a Label widget to display output_file_name
        output_file_label = tk.Label(self.frame, text=f"Output file name: {self.file_name}", bg="white")
        output_file_label.pack(pady=30)
        
        # Create a Label widget to display para
        self.parameters= []
        for keys, values in para.items():
            if values is True:
                self.parameters.append(keys)
        para_label = tk.Label(self.frame, text=f"Parameters: {self.parameters}", bg="white")
        para_label.pack(pady=30)
        
        # Add a Close button to the window
        self.start_button = tk.Button(self.frame, text="Start Program", font=self.btn_font, bg="#1dbf73", fg="white", width=30 ,height=1,command=self.run_program)
        self.start_button.pack(pady=10)        
    def run_program(self):
        # Call the function from other_file
        
        mainGoogleMaps(self.file_path, self.file_name, self.parameters)


input_style = {
    "font": ("Arial", 12),
    "foreground": "#333",
    "background": "#f7f7f7",
    "border": 10,
    "relief": tk.SOLID,
    "highlightthickness": 0,
    "insertbackground": "#333",
    "selectbackground": "#ccc",
    "selectforeground": "#333",
    "width": 50,
    "borderwidth": 1,
    "highlightcolor": "#ddd",
    "highlightbackground": "#ddd"
}


if __name__ == "__main__":

    master = tk.Tk()

    style = ttk.Style()
    # Theme availabe = ['clam', 'alt', 'default', 'classic']
    # style.theme_use('alt')
    # style.theme_use('default')
    # style.theme_use('classic')
    style.theme_use('clam')
    master.title("Starting Program")
    master.geometry("800x600")
    master.configure(bg="white")
    label_font = font.Font(family="Montserrat", size=14, weight="normal")
    ch_font = font.Font(family="Montserrat", size=10, weight="normal")
    button_font = font.Font(family="Montserrat", size=12, weight="normal")
    FileChooserWindow(master, input_style, label_font, button_font, ch_font)
    master.mainloop()