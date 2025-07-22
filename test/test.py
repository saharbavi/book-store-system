from model.entity.user import User
# from model.repository.database_creator import create_database
from model.repository.user_repository import UserRepository
from model.repository.book_repository import BookRepository
from model.repository.customer_repository import CustomerRepository

# create_database()
# test user:
user_1 = User(108, "mohsen", "alipour", "MOHSEN108", "mohsen123", "customer")
# print(user_1.to_tuple())
user_1.username = "username"
user_1.password = "PASSWORD"
# print(user_1)

# test user-repository:
user_repo = UserRepository()
#test_save_pass
# user_repo.save(user_1)
#test_edit_pass
user_repo.edit(user_1)
print(user_1)


# test book:
from model.entity.book import Book
# book_1 = Book(3,"zamin","mohsen",20000,3,"ofogh",5)
# book_1.price=30000
# book_1.number=2
# print(book_1)

 # test book-repository:
# book_repo = BookRepository()
# book_repo.save(book_1)
# print(book_1)

# test customer:
from model.entity.customer import Customer

# customer_1 = Customer(34,"ali","alipour","09365445656","tehran-iran")
# customer_1.address="tabriz-iran"
# customer_1.phone_number="+989363213322"
# print(customer_1)

 # test customer-repository:
# customer_repo = CustomerRepository()
# customer_repo.save(customer_1)
# print(customer_1)
