from view import *
from controller.user_controller import UserController
from model.entity.user import User


class UserView:

    def save_click(self):
        user_controller = UserController()
        status, message = user_controller.save(
            self.user_id.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.username.get(),
            self.password.get(),
            self.role.get(),
            self.locked.get(),
        )
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        user_controller = UserController()
        status, message = user_controller.edit(
            self.user_id.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.username.get(),
            self.password.get(),
            self.role.get(),
            self.locked.get(),
        )
        if status:
            msg.showinfo("Edite", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def delete_click(self):
        user_controller = UserController()
        status, message = user_controller.delete(
            self.user_id.get(),
        )
        if status:
            msg.showinfo("Remove", message)
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def show_data_on_table(self, status, user_list):
        if status:
            if user_list is None:
                user_list=[]

            for item in self.table.get_children():
                self.table.delete(item)

            for user in user_list:
                self.table.insert(
                    "",
                    END,
                    values=user,
                    tags="Locked" if user[6] else "OK",
                )
        else:
            msg.showerror("Error", "Error getting users data")

    def reset_form(self):
        self.user_id.set(0)
        self.first_name.set("")
        self.last_name.set("")
        self.username.set("")
        self.password.set("")
        self.role.set("")
        self.locked.set(False)
        user_controller = UserController()
        status, user_list = user_controller.find_all()
        self.show_data_on_table(status, user_list)

    def select_user(self, event):
        user = User(*self.table.item(self.table.focus())["values"])
        self.user_id.set(user.user_id)
        self.first_name.set(user.first_name)
        self.last_name.set(user.last_name)
        self.username.set(user.username)
        self.password.set(user.password)
        self.role.set(user.role)
        self.locked.set(bool(user.locked))

    def search_first_name_last_name(self, event):
        user_controller = UserController()
        status, user_list = user_controller.find_by_first_name_last_name(self.search_first_name.get(),
                                                                         self.search_last_name.get())
        self.show_data_on_table(status, user_list)

    def search_by_username(self,event):
        user_controller = UserController()
        status, user_list = user_controller.find_by_username(self.search_username.get())
        self.show_data_on_table(status, user_list)

    def search_by_username_password(self, event):
        user_controller = UserController()
        status, user_list = user_controller.find_by_username_password(self.search_username.get(),self.search_password.get())
        self.show_data_on_table(status, user_list)

    def search_by_user_id(self, event): #todo: work but an Error occurred
        user_controller = UserController()
        status, user_list = user_controller.find_by_user_id(self.search_user_id.get())
        self.show_data_on_table(status, user_list)

    def __init__(self):
        self.win = Tk()
        self.win.title("User Info")
        self.win.geometry("1200x400")
        self.win.config(cursor="hand2", background="light blue")

        ## Entries:
        # user id
        Label(self.win, text="User ID:", background="light blue").place(x=20, y=20)
        self.user_id = IntVar(value=1)
        Entry(self.win, textvariable=self.user_id, width=23).place(x=82, y=20)

        # first_name
        Label(self.win, text="First Name:", background="light blue").place(x=20, y=60)
        self.first_name = StringVar()
        Entry(self.win, textvariable=self.first_name).place(x=100, y=60)

        # last_name
        Label(self.win, text="Last Name:", background="light blue").place(x=20, y=90)
        self.last_name = StringVar()
        Entry(self.win, textvariable=self.last_name).place(x=100, y=90)

        # username
        Label(self.win, text="Username:", background="light blue").place(x=20, y=120)
        self.username = StringVar()
        Entry(self.win, textvariable=self.username).place(x=100, y=120)

        # password
        Label(self.win, text="Password:", background="light blue").place(x=20, y=150)
        self.password = StringVar()
        Entry(self.win, textvariable=self.password).place(x=100, y=150)

        # role
        Label(self.win, text="Role:", background="light blue").place(x=20, y=180)
        self.role = StringVar()
        Entry(self.win, textvariable=self.role).place(x=100, y=180)

        # locked_checkbox:
        Label(self.win, text="Locked:", background="light blue").place(x=20, y=210)
        self.locked = BooleanVar(value=False)
        Checkbutton(self.win, variable=self.locked, background="light blue").place(x=97, y=210)

        ##search:
        Label(self.win, text="Search by :", background="light blue").place(x=950, y=20)

        # # search_user id: todo: work but an Error occurred
        Label(self.win, text="User ID:", background="light blue").place(x=950, y=50)
        self.search_user_id = IntVar()
        self.search_user_id_txt = Entry(self.win, textvariable=self.search_user_id, width=23, fg="gray64")
        self.search_user_id_txt.bind("<KeyRelease>", self.search_by_user_id)
        self.search_user_id_txt.place(x=1020, y=50)

        # search_first_name:
        Label(self.win, text="First Name :", background="light blue").place(x=950, y=80)
        self.search_first_name = StringVar()
        self.search_first_name_txt = Entry(self.win, textvariable=self.search_first_name, width=23, fg="gray64")
        self.search_first_name_txt.bind("<KeyRelease>", self.search_first_name_last_name)
        self.search_first_name_txt.place(x=1020, y=80)

        # search_last_name:
        Label(self.win, text="Last Name :", background="light blue").place(x=950, y=110)
        self.search_last_name = StringVar()
        self.search_last_name_txt = Entry(self.win, textvariable=self.search_last_name, width=23, fg="gray64")
        self.search_last_name_txt.bind("<KeyRelease>", self.search_first_name_last_name)
        self.search_last_name_txt.place(x=1020, y=110)

        # search_username:
        Label(self.win, text="Username :", background="light blue").place(x=950, y=140)
        self.search_username = StringVar()
        self.search_username_txt = Entry(self.win, textvariable=self.search_username, width=23, fg="gray64")
        self.search_username_txt.bind("<KeyRelease>", self.search_by_username)
        self.search_username_txt.place(x=1020, y=140)

        # search_password:
        Label(self.win, text="Password :", background="light blue").place(x=950, y=170)
        self.search_password = StringVar()
        self.search_password_txt = Entry(self.win, textvariable=self.search_password, width=23, fg="gray64")
        self.search_password_txt.bind("<KeyRelease>", self.search_by_username_password)
        self.search_password_txt.place(x=1020, y=170)

        ## Table:
        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5, 6, 7], show="headings", height=15)

        # table_heading
        self.table.heading(1, text="User ID")
        self.table.heading(2, text="First Name")
        self.table.heading(3, text="Last Name")
        self.table.heading(4, text="Username")
        self.table.heading(5, text="Password")
        self.table.heading(6, text="Role")
        self.table.heading(7, text="Locked")

        # table_column
        self.table.column(1, width=60, anchor="center")
        self.table.column(2, width=100, anchor="center")
        self.table.column(3, width=100, anchor="center")
        self.table.column(4, width=100, anchor="center")
        self.table.column(5, width=100, anchor="center")
        self.table.column(6, width=100, anchor="center")
        self.table.column(7, width=100, anchor="center")

        self.table.tag_configure("OK", background="lightgreen")
        self.table.tag_configure("Locked", background="pink")
        self.table.bind("<ButtonRelease>", self.select_user)

        self.table.place(x=265, y=20)

        ## Buttons:

        # save_btn
        Button(self.win, text="Save", width=6, command=self.save_click).place(x=30, y=280)

        # edit_btn
        Button(self.win, text="Edit", width=6, command=self.edit_click).place(x=100, y=280)

        # remove_btn
        Button(self.win, text="Delete", width=6, command=self.delete_click).place(x=170, y=280)

        # reset_btn
        Button(self.win, text="Clear", width=26, command=self.reset_form).place(x=30, y=240)

        # search_btn
        # Button(self.win, text="Search", width=6, command=self.search_click).place(x=1000, y=360)

        self.reset_form()

        self.win.mainloop()
