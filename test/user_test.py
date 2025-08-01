from model.entity.user import User
from model.repository.user_repository import UserRepository
from controller.user_controller import UserController
from model.repository.book_repository import BookRepository
from model.repository.customer_repository import CustomerRepository

# test user:
# user_1 = User(108, "mohsen", "alipour", "MOHSEN108", "mohsen123", "customer")
# user_1.username = "username2"
# user_1.password = "PASSWORD2"
# # print(user_1)
#
# # test user-repository:
# user_repo = UserRepository()

# #test_save_pass
# user_repo.save(user_1)

# #test_edit_pass
# user_repo.edit(user_1)

#test_delete_pass
# user_repo.delete(108)

# print(user_1)

# find_all_test_pass
# print(user_repo.find_all())

# find by name test_pass
# print(user_repo.find_by_first_name_last_name("mohsen", "alipour"))

# find by username_pass
# print(user_repo.find_by_username("sahelsal"))
####
#test user_controller:
# user_controller=UserController()
# save_test_pass
# print(user_controller.save(111, "sahar", "sahari", "SAHAR876", "sahar876", "admin", 1))



################################
# test book:
from model.entity.book import Book
# book_1 = Book(9,"zamin","mohsen",20000,3,"ofogh",5)
# book_1.price=30000
# book_1.number=6
# # print(book_1)
#
#  # test book-repository:
# book_repo = BookRepository()
# #test_save_pass
# book_repo.save(book_1)
# #test_edit_pass
# book_repo.edit(book_1)
#test_delete_pass
# book.repo.delete(9)
# print(book_1)
###############################
# # test customer:
from model.entity.customer import Customer
# customer_1 = Customer(33,"ali","alipour","09365445656","tehran-iran")
# customer_1.address="tabriz-iran"
# customer_1.phone_number="+989363213322"
# # print(customer_1)
#
#  # test customer-repository:
# customer_repo = CustomerRepository()
# # #test_save_pass
# customer_repo.save(customer_1)
# #test_edit_pass
# customer_repo.edit(customer_1)
#test_delete_pass
# customer_repo.delete(33)
# print(customer_1)
