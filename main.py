from model.repository.database_creator import create_database
from view.user_view import UserView
from view.book_view import BookView
from view.customer_view import CustomerView

create_database()

# ui=UserView()

ui=BookView()

# ui=CustomerView()