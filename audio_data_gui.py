"""
a simple gui
"""
import re
import os
import sys
import tkinter
from tkinter import messagebox
import customtkinter
from audio_data import AudioFiles as Af
from PIL import ImageTk


class TheFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # ask for path to directory with files to work with
        self.working_dir_dialog = customtkinter.CTkInputDialog(title="Working Directory",
                                                               text="Input absolute path to working directory:")
        # Set favicon (title bar icon)
        bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        path_to_logo = os.path.abspath(os.path.join(bundle_dir, 'favicon_light.ico'))
        self.working_dir_dialog.iconpath = ImageTk.PhotoImage(file=path_to_logo)
        self.working_dir_dialog.wm_iconbitmap()
        self.after(250, lambda: self.working_dir_dialog.iconphoto(False, self.working_dir_dialog.iconpath))

        self.ape_data_var = customtkinter.StringVar()
        self.prep_data_var = customtkinter.StringVar()
        self.rm_data_var = customtkinter.StringVar()
        self.rep_data_var = customtkinter.StringVar()
        self.add_data_var = customtkinter.StringVar()
        self.set_data_var = customtkinter.StringVar(value=self.working_dir_dialog.get_input())
        self.radio_var = tkinter.IntVar(value=0)

        # noinspection PyTypeChecker
        self.grid_columnconfigure((0, 1, 2), weight=8)
        self.grid_columnconfigure(3, weight=2)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        # add labels
        self.ape_data_label = customtkinter.CTkLabel(master=self, font=("Frankling Gothic", 14),
                                                     text="Append filename with:")
        self.ape_data_label.grid(column=0, row=0, padx=4, pady=5, sticky="ew")
        self.prep_data_label = customtkinter.CTkLabel(master=self, font=("Frankling Gothic", 14),
                                                      text="Prepend filename with:")
        self.prep_data_label.grid(column=0, row=1, padx=4, pady=5, sticky="ew")
        self.rm_data_label = customtkinter.CTkLabel(master=self, font=("Frankling Gothic", 14),
                                                    text="Remove from filename:")
        self.rm_data_label.grid(column=0, row=2, padx=4, pady=5, sticky="ew")
        self.rep_data_label = customtkinter.CTkLabel(master=self, font=("Frankling Gothic", 14),
                                                     text="Replace substring:")
        self.rep_data_label.grid(column=0, row=3, padx=4, pady=5, sticky="ew")
        self.set_data_label = customtkinter.CTkLabel(master=self, font=("Frankling Gothic", 14),
                                                     text="Set tags for files in path:")
        self.set_data_label.grid(column=0, row=5, padx=4, pady=5, sticky="ew")
        self.get_data_label = customtkinter.CTkLabel(master=self, font=("Frankling Gothic", 14),
                                                     text="Get tags for files in path:")
        self.get_data_label.grid(column=0, row=6, padx=4, pady=5, sticky="ew")

        # add entry boxes
        self.ape_data_entry = customtkinter.CTkEntry(master=self, font=("Franklin Gothic", 14),
                                                     textvariable=self.ape_data_var)
        self.ape_data_entry.grid(column=1, row=0, columnspan=2, padx=4, pady=5, sticky="ew")
        self.prep_data_entry = customtkinter.CTkEntry(master=self, font=("Franklin Gothic", 14),
                                                      textvariable=self.prep_data_var)
        self.prep_data_entry.grid(column=1, row=1, columnspan=2, padx=4, pady=5, sticky="ew")
        self.rm_data_entry = customtkinter.CTkEntry(master=self, font=("Franklin Gothic", 14),
                                                    textvariable=self.rm_data_var)
        self.rm_data_entry.grid(column=1, row=2, columnspan=2, padx=4, pady=5, sticky="ew")
        self.rep_data_entry = customtkinter.CTkEntry(master=self, font=("Franklin Gothic", 14),
                                                     textvariable=self.rep_data_var)
        self.rep_data_entry.grid(column=1, row=3, padx=4, pady=5, sticky="ew")
        self.add_data_entry = customtkinter.CTkEntry(master=self, font=("Franklin Gothic", 14),
                                                     textvariable=self.add_data_var)
        self.add_data_entry.grid(column=2, row=3, padx=4, pady=5, sticky="ew")
        self.set_data_entry = customtkinter.CTkEntry(master=self, font=("Franklin Gothic", 14),
                                                     textvariable=self.set_data_var, fg_color="transparent",
                                                     border_width=0, state="readonly")
        self.set_data_entry.grid(column=1, row=5, columnspan=2, rowspan=2, padx=4, pady=5, sticky="nsew")

        # add radio buttons
        self.ape_data_radio = customtkinter.CTkRadioButton(master=self, font=("Frankling Gothic", 14), text="",
                                                           variable=self.radio_var, value=1)
        self.ape_data_radio.grid(column=3, row=0, padx=4, pady=5, sticky="e")
        self.prep_data_radio = customtkinter.CTkRadioButton(master=self, font=("Frankling Gothic", 14), text="",
                                                            variable=self.radio_var, value=2)
        self.prep_data_radio.grid(column=3, row=1, padx=4, pady=5, sticky="e")
        self.rm_data_radio = customtkinter.CTkRadioButton(master=self, font=("Frankling Gothic", 14), text="",
                                                          variable=self.radio_var, value=3)
        self.rm_data_radio.grid(column=3, row=2, padx=4, pady=5, sticky="e")
        self.mk_data_radio = customtkinter.CTkRadioButton(master=self, font=("Frankling Gothic", 14), text="",
                                                          variable=self.radio_var, value=4)
        self.mk_data_radio.grid(column=3, row=3, padx=4, pady=5, sticky="e")
        self.set_data_radio = customtkinter.CTkRadioButton(master=self, font=("Frankling Gothic", 14), text="",
                                                           variable=self.radio_var, value=5)
        self.set_data_radio.grid(column=3, row=5, padx=4, pady=5, sticky="e")
        self.get_data_radio = customtkinter.CTkRadioButton(master=self, font=("Frankling Gothic", 14), text="",
                                                           variable=self.radio_var, value=6)
        self.get_data_radio.grid(column=3, row=6, padx=4, pady=5, sticky="e")

        # add button
        self.submit_button = customtkinter.CTkButton(master=self, font=("Frankling Gothic", 14), text="Submit",
                                                     command=self.do_deed)
        self.submit_button.grid(column=1, row=7, columnspan=2, padx=4, pady=(0, 10), sticky="nsew")

    def do_deed(self):
        work_dir = str(self.set_data_var.get())
        ape_str = str(self.ape_data_var.get())
        prep_str = str(self.prep_data_var.get())
        rm_str = str(self.rm_data_var.get())
        add_str = str(self.add_data_var.get())
        rep_str = str(self.rep_data_var.get())
        janitor = Af(work_dir)
        match self.radio_var.get():
            case 1:
                if ape_str:
                    janitor.append(ape_str)
                    messagebox.showinfo(master=None, parent=app, title="File Tags",
                                        message=f"{ape_str} has been appended for all files in: {work_dir}")
            case 2:
                if prep_str:
                    janitor.prepend(prep_str)
                    messagebox.showinfo(master=None, parent=app, title="File Tags",
                                        message=f"{prep_str} has been prepended for all files in: {work_dir}")
            case 3:
                if rm_str:
                    janitor.remove_substr(rm_str)
                    messagebox.showinfo(master=None, parent=app, title="File Tags",
                                        message=f"Removed {rm_str} in all filenames in '{work_dir}' if found")
            case 4:
                if rep_str:
                    janitor.replace_substr(rep_str, add_str)
                    messagebox.showinfo(master=None, parent=app, title="File Tags",
                                        message=f"Replaced {rep_str} with {add_str} in all filenames in '{work_dir}' if found")
            case 5:
                janitor.set_metadata()
                messagebox.showinfo(master=None, parent=app, title="File Tags",
                                    message=f"Artist and title tags have been set for all files in: {work_dir}")
            case 6:
                new_list = []
                for element in janitor.get_metadata():
                    for key in element:
                        if key == "artist" or "title" in key:
                            if key == "artist":
                                new_list.append(f"{element[key]}")
                            else:
                                new_list.append(f"\n{element[key]}")
                new_list2 = " ".join(new_list)
                new_list3 = re.sub("({.*?})", "", new_list2)
                messagebox.showinfo(master=None, parent=app, title="File Tags", message=new_list3)
            case _:
                messagebox.showinfo(master=None, parent=app, title="File Tags",
                                    message="Please choose a function before trying to submit")


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # initialize pop up text menu
        self.the_menu = tkinter.Menu(self, tearoff=0)
        self.make_textmenu()

        # Set theme and color options
        customtkinter.set_appearance_mode("dark")  # Modes: System (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

        # Set favicon (title bar icon)
        bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        path_to_logo = os.path.abspath(os.path.join(bundle_dir, 'favicon_light.ico'))
        self.iconpath = ImageTk.PhotoImage(file=path_to_logo)
        self.wm_iconbitmap()
        self.iconphoto(False, self.iconpath)

        # Set window title, size, grid index and width
        self.title("Edit MP3/4")
        self.geometry("720x480")
        self.minsize(720, 480)

        # bind the feature to all Entry widget
        self.bind_class("Entry", "<Button-3><ButtonRelease-3>", self.show_textmenu)
        self.bind_class("Entry", "<Control-a>", self.callback_select_all)

        # create grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Initialize content frames
        self.the_frame = TheFrame(master=self)
        self.the_frame.grid(column=0, row=0, rowspan=2, pady=30, padx=30, sticky="nswe")

    # create menu call
    def show_textmenu(self, event):
        e_widget = event.widget
        self.the_menu.entryconfigure("Cut", command=lambda: e_widget.event_generate("<<Cut>>"))
        self.the_menu.entryconfigure("Copy", command=lambda: e_widget.event_generate("<<Copy>>"))
        self.the_menu.entryconfigure("Paste", command=lambda: e_widget.event_generate("<<Paste>>"))
        self.the_menu.entryconfigure("Select all", command=lambda: e_widget.select_range(0, 'end'))
        # self.the_menu.entryconfigure("Select all", command=lambda: e_widget.tag_add("sel", "1.0", "end"))
        self.the_menu.tk.call("tk_popup", self.the_menu, event.x_root, event.y_root)

    # create the menu for the cut, copy, paste
    def make_textmenu(self):
        self.the_menu.add_command(label="Cut")
        self.the_menu.add_command(label="Copy")
        self.the_menu.add_command(label="Paste")
        self.the_menu.add_separator()
        self.the_menu.add_command(label="Select all")

    def callback_select_all(self, event):
        # for entry widgets
        self.after(50, lambda: event.widget.select_range(0, 'end'))
        # for text widgets
        # self.after(50, lambda: event.widget.tag_add("sel", "1.0", "end"))


if __name__ == "__main__":
    app = App()
    app.mainloop()
