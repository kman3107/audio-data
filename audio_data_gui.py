"""
a simple gui
"""

import os
import sys
from pathlib import Path
import tkinter
from tkinter import messagebox
import customtkinter
from audio_data import AudioFiles as Af


# function for a way to exit app
def exit_button():
    sys.exit(0)


class TheFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # ask for path to directory with files to work with
        self.working_dir_dialog = customtkinter.CTkInputDialog(title="Working Directory",
                                                               text="Input absolute path to working directory:")
        # Set favicon (title bar icon)
        self.after(250, lambda: self.working_dir_dialog.iconbitmap(os.path.join(Path(__file__).parent, "favicon_light.ico")))

        self.prep_data_var = customtkinter.StringVar()
        self.rm_data_var = customtkinter.StringVar()
        self.set_data_var = customtkinter.StringVar(value=self.working_dir_dialog.get_input())
        self.radio_var = tkinter.IntVar(value=0)

        # noinspection PyTypeChecker
        self.grid_columnconfigure((0, 1), weight=8)
        self.grid_columnconfigure(2, weight=2)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # add labels
        self.prep_data_label = customtkinter.CTkLabel(master=self, font=("Frankling Gothic", 14),
                                                      text="Prepend filename with:")
        self.prep_data_label.grid(column=0, row=0, padx=4, pady=5, sticky="ew")
        self.rm_data_label = customtkinter.CTkLabel(master=self, font=("Frankling Gothic", 14),
                                                    text="Remove from filename:")
        self.rm_data_label.grid(column=0, row=1, padx=4, pady=5, sticky="ew")
        self.set_data_label = customtkinter.CTkLabel(master=self, font=("Frankling Gothic", 14),
                                                     text="Set MP4 tags for files in path:")
        self.set_data_label.grid(column=0, row=3, padx=4, pady=5, sticky="ew")
        self.get_data_label = customtkinter.CTkLabel(master=self, font=("Frankling Gothic", 14),
                                                     text="Get MP4 tags for files in path:")
        self.get_data_label.grid(column=0, row=4, padx=4, pady=5, sticky="ew")

        # add entry boxes
        self.prep_data_entry = customtkinter.CTkEntry(master=self, font=("Franklin Gothic", 14),
                                                      textvariable=self.prep_data_var)
        self.prep_data_entry.grid(column=1, row=0, padx=4, pady=5, sticky="ew")
        self.rm_data_entry = customtkinter.CTkEntry(master=self, font=("Franklin Gothic", 14),
                                                    textvariable=self.rm_data_var)
        self.rm_data_entry.grid(column=1, row=1, padx=4, pady=5, sticky="ew")
        self.set_data_entry = customtkinter.CTkEntry(master=self, font=("Franklin Gothic", 14),
                                                     textvariable=self.set_data_var, fg_color="transparent",
                                                     border_width=0, state="readonly")
        self.set_data_entry.grid(column=1, row=3, rowspan=2, padx=4, pady=5, sticky="nsew")

        # add radio buttons
        self.prep_data_radio = customtkinter.CTkRadioButton(master=self, font=("Frankling Gothic", 14), text="",
                                                            variable=self.radio_var, value=1)
        self.prep_data_radio.grid(column=2, row=0, padx=4, pady=5, sticky="e")
        self.rm_data_radio = customtkinter.CTkRadioButton(master=self, font=("Frankling Gothic", 14), text="",
                                                          variable=self.radio_var, value=2)
        self.rm_data_radio.grid(column=2, row=1, padx=4, pady=5, sticky="e")
        self.set_data_radio = customtkinter.CTkRadioButton(master=self, font=("Frankling Gothic", 14), text="",
                                                           variable=self.radio_var, value=3)
        self.set_data_radio.grid(column=2, row=3, padx=4, pady=5, sticky="e")
        self.get_data_radio = customtkinter.CTkRadioButton(master=self, font=("Frankling Gothic", 14), text="",
                                                           variable=self.radio_var, value=4)
        self.get_data_radio.grid(column=2, row=4, padx=4, pady=5, sticky="e")

        # add button
        self.submit_button = customtkinter.CTkButton(master=self, font=("Frankling Gothic", 14), text="Submit",
                                                     command=self.do_deed)
        self.submit_button.grid(column=1, row=5, padx=4, pady=5, sticky="nsew")

    def do_deed(self):
        work_dir = str(self.set_data_var.get())
        prep_str = str(self.prep_data_var.get())
        rm_str = str(self.rm_data_var.get())
        janitor = Af(work_dir)
        match self.radio_var.get():
            case 1:
                if prep_str:
                    janitor.prepend(prep_str)
                    messagebox.showinfo(master=None, parent=app, title="MP4 Tags",
                                        message=f"{prep_str} has been prepended for all files in: {work_dir}")
            case 2:
                if rm_str:
                    janitor.remove_substr(rm_str)
                    messagebox.showinfo(master=None, parent=app, title="MP4 Tags",
                                        message=f"Removed {rm_str} in all filenames in '{work_dir}' if found")
            case 3:
                janitor.set_metadata()
                messagebox.showinfo(master=None, parent=app, title="MP4 Tags",
                                    message=f"Artist and title tags have been set for all files in: {work_dir}")
            case 4:
                messagebox.showinfo(master=None, parent=app, title="MP4 Tags",
                                    message=f"{janitor.get_metadata()}")
            case _:
                messagebox.showinfo(master=None, parent=app, title="MP4 Tags",
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
        self.iconbitmap(os.path.join(Path(__file__).parent, "favicon_light.ico"))

        # Set some variables to be used by CTk
        # self.textbox_var = customtkinter.StringVar(value="EXAMPLE")

        # Set window title, size, grid index and width
        self.title("Edit MP4")
        self.geometry("900x600")
        self.minsize(900, 600)

        # create grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # noinspection PyTypeChecker

        # Initialize content frames
        self.the_frame = TheFrame(master=self)
        self.the_frame.grid(column=0, row=0, rowspan=2, pady=30, padx=30, sticky="nswe")

        # bind the feature to all Text widget
        self.bind_class("Entry", "<Button-3><ButtonRelease-3>", self.show_textmenu)
        self.bind_class("Entry", "<Control-a>", self.callback_select_all)

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
