from view import *
from controller.customer_controller import CustomerController
from model.entity.customer import Customer


class CustomerView:

    def save_click(self):
        customer_controller = CustomerController()
        status, message = customer_controller.save(
            self.custom_id.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.phone_number.get(),
            self.address.get(),
        )
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        customer_controller = CustomerController()
        status, message = customer_controller.edit(
            self.custom_id.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.phone_number.get(),
            self.address.get(),
        )
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def delete_click(self):
        customer_controller = CustomerController()
        status, message = customer_controller.delete(
            self.custom_id.get(),
        )
        if status:
            msg.showinfo("Remove", message)
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def show_data_on_table(self, status, customer_list):
        if status:
            if customer_list is None:
                customer_list=[]

            for item in self.table.get_children():
                self.table.delete(item)

            for customer in customer_list:
                self.table.insert(
                    "",
                    END,
                    values=customer,
                    tags="",
                )
        else:
            msg.showerror("Error", "Error getting customers data")

    def reset_form(self):
        self.custom_id.set(0)
        self.first_name.set("")
        self.last_name.set("")
        self.phone_number.set("")
        self.address.set("")
        customer_controller = CustomerController()
        status, customer_list = customer_controller.find_all()
        self.show_data_on_table(status, customer_list)

    def select_customer(self, event):
        customer = Customer(*self.table.item(self.table.focus())["values"])
        self.custom_id.set(customer.custom_id)
        self.first_name.set(customer.first_name)
        self.last_name.set(customer.last_name)
        self.phone_number.set(customer.phone_number)
        self.address.set(customer.address)

    def search_by_custom_id(self, event): #todo: work but an Error occurred
        customer_controller = CustomerController()
        status, customer_list = customer_controller.find_by_custom_id(self.search_custom_id.get())
        self.show_data_on_table(status, customer_list)

    def search_first_name_last_name(self, event):
        customer_controller = CustomerController()
        status, customer_list = customer_controller.find_by_first_name_last_name(self.search_first_name.get(),
                                                                         self.search_last_name.get())
        self.show_data_on_table(status, customer_list)


    def __init__(self):
        self.win = Tk()
        self.win.title("Customer Info")
        self.win.geometry("1110x400")
        self.win.config(cursor="hand2", background="light blue")

        ## Entries:
        # customer id
        Label(self.win, text="Customer ID:", background="light blue").place(x=20, y=20)
        self.custom_id = IntVar(value=1)
        Entry(self.win, textvariable=self.custom_id).place(x=100, y=20)

        # first_name
        Label(self.win, text="First Name:", background="light blue").place(x=20, y=60)
        self.first_name = StringVar()
        Entry(self.win, textvariable=self.first_name).place(x=100, y=60)

        # last_name
        Label(self.win, text="Last Name:", background="light blue").place(x=20, y=90)
        self.last_name = StringVar()
        Entry(self.win, textvariable=self.last_name).place(x=100, y=90)

        # address
        Label(self.win, text="Address:", background="light blue").place(x=20, y=120)
        self.address = StringVar()
        Entry(self.win, textvariable=self.address).place(x=100, y=120)

        # phone number
        Label(self.win, text="Phone Number:", background="light blue").place(x=20, y=150)
        self.phone_number = StringVar()
        Entry(self.win, textvariable=self.phone_number,width=18).place(x=110, y=150)

        ##search:
        Label(self.win, text="Search by :", background="light blue").place(x=860, y=20)

        # # search_customer id: todo: work but an Error occurred
        Label(self.win, text="Customer ID :", background="light blue").place(x=860, y=50)
        self.search_custom_id = IntVar()
        self.search_custom_id_txt = Entry(self.win, textvariable=self.search_custom_id,width=22 ,fg="gray64")
        self.search_custom_id_txt.bind("<KeyRelease>", self.search_by_custom_id)
        self.search_custom_id_txt.place(x=940, y=50)

        # search_first_name:
        Label(self.win, text="First Name :", background="light blue").place(x=860, y=80)
        self.search_first_name = StringVar()
        self.search_first_name_txt = Entry(self.win, textvariable=self.search_first_name, width=23, fg="gray64")
        self.search_first_name_txt.bind("<KeyRelease>", self.search_first_name_last_name)
        self.search_first_name_txt.place(x=935, y=80)

        # search_last_name:
        Label(self.win, text="Last Name :", background="light blue").place(x=860, y=110)
        self.search_last_name = StringVar()
        self.search_last_name_txt = Entry(self.win, textvariable=self.search_last_name, width=23, fg="gray64")
        self.search_last_name_txt.bind("<KeyRelease>", self.search_first_name_last_name)
        self.search_last_name_txt.place(x=935, y=110)

        ## Table:
        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5], show="headings", height=15)

        # table_heading
        self.table.heading(1, text="Customer ID")
        self.table.heading(2, text="First Name")
        self.table.heading(3, text="Last Name")
        self.table.heading(4, text="Phone Number")
        self.table.heading(5, text="Address")



        # table_column
        self.table.column(1, width=100, anchor="center")
        self.table.column(2, width=100, anchor="center")
        self.table.column(3, width=100, anchor="center")
        self.table.column(4, width=150, anchor="center")
        self.table.column(5, width=100, anchor="center")


        # self.table.tag_configure("", background="lightgreen")
        # self.table.tag_configure("", background="pink")
        self.table.bind("<ButtonRelease>", self.select_customer)

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




        self.reset_form()

        self.win.mainloop()
