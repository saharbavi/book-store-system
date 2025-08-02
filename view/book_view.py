from view import *
from controller.book_controller import BookController
from model.entity.book import Book
from model.tools.data_list import publisher_list

class BookView:

    def save_click(self):
        book_controller = BookController()
        status, message = book_controller.save(
            self.code.get(),
            self.title.get(),
            self.author.get(),
            self.price.get(),
            self.edition.get(),
            self.publisher.get(),
            self.number.get()
        )
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        book_controller = BookController()
        status, message = book_controller.edit(
            self.code.get(),
            self.title.get(),
            self.author.get(),
            self.price.get(),
            self.edition.get(),
            self.publisher.get(),
            self.number.get()
        )
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def delete_click(self):
        book_controller = BookController()
        status, message = book_controller.delete(
            self.code.get(),
        )
        if status:
            msg.showinfo("Remove", message)
            self.reset_form()
        else:
            msg.showerror("Remove Error", message)

    def show_data_on_table(self, status, book_list):
        if status:
            if book_list is None:
                book_list = []

            for item in self.table.get_children():
                self.table.delete(item)

            for book in book_list:
                self.table.insert(
                    "",
                    END,
                    values=book,
                    tags="",
                )
        else:
            msg.showerror("Error", "Error getting books data")

    def reset_form(self):
        self.code.set(0)
        self.title.set("")
        self.author.set("")
        self.price.set(0)
        self.edition.set("")
        self.publisher.set("افق")
        self.number.set(0)
        book_controller = BookController()
        status, book_list = book_controller.find_all()
        self.show_data_on_table(status, book_list)

    def select_book(self, event):
        book = Book(*self.table.item(self.table.focus())["values"])
        self.code.set(book.code)
        self.title.set(book.title)
        self.author.set(book.author)
        self.price.set(book.price)
        self.edition.set(book.edition)
        self.publisher.set(book.publisher)
        self.number.set(book.number)

    def search_by_code(self, event): #todo: work but an Error occurred
        book_controller = BookController()
        status, book_list = book_controller.find_by_code(self.search_code.get())
        self.show_data_on_table(status, book_list)

    def search_by_title_author(self, event):
        book_controller = BookController()
        status, book_list = book_controller.find_by_title_author(self.search_title.get(),
                                                                         self.search_author.get())
        self.show_data_on_table(status, book_list)


    def __init__(self):
        self.win = Tk()
        self.win.title("Book Info")
        self.win.geometry("1200x400")
        self.win.config(cursor="hand2", background="light blue")

        ## Entries:
        # code
        Label(self.win, text="Code:", background="light blue").place(x=20, y=20)
        self.code = IntVar(value=1)
        Entry(self.win, textvariable=self.code, width=23).place(x=82, y=20)

        # title
        Label(self.win, text="Title:", background="light blue").place(x=20, y=60)
        self.title = StringVar()
        Entry(self.win, textvariable=self.title).place(x=100, y=60)

        # author
        Label(self.win, text="Author:", background="light blue").place(x=20, y=90)
        self.author = StringVar()
        Entry(self.win, textvariable=self.author).place(x=100, y=90)

        # publisher
        Label(self.win, text="Publisher:", background="light blue").place(x=20, y=130)
        self.publisher = StringVar(value="افق")
        ttk.Combobox(self.win, textvariable=self.publisher, values=publisher_list,width=17).place(x=100, y=130)

        # edition
        Label(self.win, text="Edition:", background="light blue").place(x=20, y=160)
        self.edition = StringVar()
        Entry(self.win, textvariable=self.edition).place(x=100, y=160)

        #price
        Label(self.win, text="Price:", background="light blue").place(x=20, y=190)
        self.price = IntVar()
        Entry(self.win, textvariable=self.price).place(x=100, y=190)

        #numbers
        Label(self.win, text="Numbers:", background="light blue").place(x=20, y=220)
        self.number = IntVar()
        Entry(self.win, textvariable=self.number).place(x=100, y=220)

        #search_book:
        Label(self.win, text="Search by :", background="light blue").place(x=950, y=20)

        # code #todo: work but an Error occurred
        Label(self.win, text="Code:", background="light blue").place(x=950, y=60)
        self.search_code = IntVar()
        self.search_code_txt=Entry(self.win, textvariable=self.search_code)
        self.search_code_txt.bind("<KeyRelease>", self.search_by_code)
        self.search_code_txt.place(x=999, y=60)

        # title
        Label(self.win, text="Title:", background="light blue").place(x=950, y=90)
        self.search_title = StringVar()
        self.search_title_txt = Entry(self.win, textvariable=self.search_title)
        self.search_title_txt.bind("<KeyRelease>", self.search_by_title_author)
        self.search_title_txt.place(x=999, y=90)

        # author
        Label(self.win, text="Author:", background="light blue").place(x=950, y=120)
        self.search_author = StringVar()
        self.search_author_txt = Entry(self.win, textvariable=self.search_author)
        self.search_author_txt.bind("<KeyRelease>", self.search_by_title_author)
        self.search_author_txt.place(x=999, y=120)

        ## Table:
        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5, 6, 7], show="headings", height=15)

        # table_heading
        self.table.heading(1, text="Code")
        self.table.heading(2, text="Title")
        self.table.heading(3, text="Author")
        self.table.heading(4, text="Price")
        self.table.heading(5, text="Edition")
        self.table.heading(6, text="Publisher")
        self.table.heading(7, text="Numbers")

        # table_column
        self.table.column(1, width=60, anchor="center")
        self.table.column(2, width=100, anchor="center")
        self.table.column(3, width=100, anchor="center")
        self.table.column(4, width=100, anchor="center")
        self.table.column(5, width=100, anchor="center")
        self.table.column(6, width=100, anchor="center")
        self.table.column(7, width=100, anchor="center")

        # self.table.tag_configure("OK", background="lightgreen")
        # self.table.tag_configure("Locked", background="pink")
        self.table.bind("<ButtonRelease>", self.select_book)

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