from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import filedialog
from tkinter import messagebox


class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.__controller = controller
        self.__width = 800
        self.__height = 500
        self.__regular_font = font.Font(family="Courier", size=14)
        self.__Treeview_font = font.Font(family="Verdana", size=14)

        self.title("Inimese Otsimine")
        self.center_window(self.__width, self.__height)

        self.__top_frame = self.create_top_frame()
        self.__bottom_frame = self.create_bottom_frame()

        self.__lbl_info, self.__lbl_notifications = self.create_lables()

        self.__text_box = self.create_text_box()

        self.__btn_send, self.__btn_file_selection = self.create_buttons()
        self.__char_input = Entry(self.__top_frame, width=25, justify="center", font=self.__regular_font)
        self.__char_input.grid(row=1, column=0, padx=5, pady=2, sticky=EW)

    @property
    def text_box(self):
        return self.__text_box

    def notifications(self, info):
        self.__lbl_notifications.config(text=info)  # Insert new content

    def change_send_btn(self, change):
        if change:
            self.__btn_send.config(state=NORMAL)
        else:
            self.__btn_send.config(state=DISABLED)

    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_top_frame(self):
        frame = Frame(self, bg="#ffe5c5", height=15)
        frame.pack(expand=False, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def destroy_table(self):
        pass


    def create_text_box(self):
        # Tekitab info kasti kuhu tuleb tulemused ja lisab sellele scrollbari
        txt_box = Text(self.__bottom_frame, font=self.__regular_font, state=DISABLED)
        scrollbar = Scrollbar(self.__bottom_frame, orient="vertical")
        scrollbar.config(command=txt_box.yview)
        txt_box.configure(yscrollcommand=scrollbar.set)

        # scrollbar.pack(side=RIGHT, fill=Y)
        txt_box.pack(padx=5, pady=2)

        return txt_box

    def create_buttons(self):
        send = Button(self.__top_frame, text="Otsi", font=self.__regular_font, state=DISABLED, command=lambda:self.__controller.search_click(self.__char_input.get()))
        file_selection = Button(self.__top_frame, text="Fail", font=self.__regular_font, command=self.__controller.file_ask)

        send.grid(row=1, column=1, padx=5, pady=2)
        file_selection.grid(row=1, column=2, padx=5, pady=2, sticky=EW)

        return send, file_selection

    def create_lables(self):
        info = Label(self.__top_frame, text="Sisesta Info Otsimiseks", font=self.__regular_font, bg="#ffe5c5")
        notifications = Label(self.__top_frame, text="Valige fail", font=self.__regular_font, bg="#ffe5c5", fg="red")

        info.grid(row=0, column=0, padx=5, pady=2, sticky=EW)
        notifications.place(x=290, y=2.5)

        return info, notifications

    @staticmethod
    def show_folder():
        initial_dir = "C:/Users/Ralf Markus.Pärn/Documents/Python Projects/Faili_lugeja/failid"
        file_path = filedialog.askopenfilename(title="Select a File",
                                               filetypes=[("All files", "*.*")], initialdir=initial_dir)
        return file_path

    def generate_table(self, data):
        #data = data_str.strip("{}").split(";")
        # Extract the first (and only) element from the list

        for child in self.__bottom_frame.winfo_children():
            child.destroy()

        my_table = ttk.Treeview(self.__bottom_frame)

        vsb = Scrollbar(self.__bottom_frame, orient="vertical", command=my_table.yview)
        vsb.pack(side=RIGHT, fill="y")
        my_table.configure(yscrollcommand=vsb.set)

        my_table["columns"] = ("Eesnimi", "Perenimi", "Sünniaeg", "Sugu", "Isikukood")


        my_table.column("#0", width=0, stretch=NO)
        my_table.column("Eesnimi", width=100, anchor="center")
        my_table.column("Perenimi", width=100, anchor="center")
        my_table.column("Sünniaeg", width=100, anchor="center")
        my_table.column("Sugu", width=50, anchor="center")
        my_table.column("Isikukood", width=100, anchor="center")

        # Tabeli päis (heading)
        my_table.heading("Eesnimi", text="Eesnimi", anchor="center")
        my_table.heading("Perenimi", text="Perenimi", anchor="center")
        my_table.heading("Sünniaeg", text="Sünniaeg", anchor="center")
        my_table.heading("Sugu", text="Sugu", anchor="center")
        my_table.heading("Isikukood", text="Isikukood", anchor="center")

        for data_str in data:
            data_str = data_str[0]
            row = data_str.strip('{}').split(';')
            my_table.insert("", "end", values=row)


        # Pack the table into the frame
        #my_table.pack(padx=5, pady=2)
        my_table.pack(fill="both", expand=True)

        return my_table

    def generate_large_table(self, data):
        for child in self.__bottom_frame.winfo_children():
            child.destroy()

        my_table = ttk.Treeview(self.__bottom_frame)

        vsb = Scrollbar(self.__bottom_frame, orient="vertical", command=my_table.yview)
        vsb.pack(side=RIGHT, fill="y")
        my_table.configure(yscrollcommand=vsb.set)

        my_table["columns"] = ("Eesnimi", "Perenimi", "Sugu", "Sünniaeg", "Surnud", "Asula", "Tüüp", "Maakond")

        my_table.column("#0", width=0, stretch=NO)
        my_table.column("Eesnimi", width=100, anchor="center")
        my_table.column("Perenimi", width=100, anchor="center")
        my_table.column("Sugu", width=35, anchor="center")
        my_table.column("Sünniaeg", width=90, anchor="center")
        my_table.column("Surnud", width=90, anchor="center")
        my_table.column("Asula", width=100, anchor="center")
        my_table.column("Tüüp", width=100, anchor="center")
        my_table.column("Maakond", width=100, anchor="center")

        # Tabeli päis (heading)
        my_table.heading("#0", text="", anchor=CENTER)
        my_table.heading("Eesnimi", text="Eesnimi", anchor="center")
        my_table.heading("Perenimi", text="Perenimi", anchor="center")
        my_table.heading("Sugu", text="Sugu", anchor="center")
        my_table.heading("Sünniaeg", text="Sünniaeg", anchor="center")
        my_table.heading("Surnud", text="Surnud", anchor="center")
        my_table.heading("Asula", text="Asula", anchor="center")
        my_table.heading("Tüüp", text="Tüüp", anchor="center")
        my_table.heading("Maakond", text="Maakond", anchor="center")

        for data_str in data:
            data_str = data_str[0]
            row = data_str.strip('{}').split(';')
            my_table.insert("", "end", values=row)

        # Pack the table into the frame
        # my_table.pack(padx=5, pady=2)
        my_table.pack(fill="both", expand=True)

        return my_table

    def create_messagebox(self, title, message):
        messagebox.showinfo(title, message)
