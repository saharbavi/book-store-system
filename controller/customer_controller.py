from model.entity.customer import Customer
from model.repository.customer_repository import CustomerRepository

class CustomerController:
    def save(self, custom_id, first_name, last_name, phone_number, address):
        try:
            customer = Customer(custom_id, first_name, last_name, phone_number, address)
            customer_repo = CustomerRepository()
            customer_repo.save(customer)
            return True, f"customer saved successfully {customer}"
        except Exception as e:
            return False, f"error saving customer : {e}"

    def edit(self, custom_id, first_name, last_name, phone_number, address):
        try:
            customer = Customer(custom_id, first_name, last_name, phone_number, address)
            customer_repo = CustomerRepository()
            customer_repo.edit(customer)
            return True, f"customer edited successfully {customer}"
        except Exception as e:
            return False, f"error editing customer : {e}"

    def delete(self, custom_id):
        try:
            customer_repo = CustomerRepository()
            customer_repo.delete(custom_id)
            return True, f"customer removed successfully {custom_id}"
        except Exception as e:
            return False, f"error removing customer : {e}"

    # search_customer
    def find_all(self):
        try:
            customer_repo = CustomerRepository()
            return True, customer_repo.find_all()
        except Exception as e:
            return False, f"error find all customers : {e}"

    def find_by_custom_id(self, custom_id):
        try:
            customer_repo = CustomerRepository()
            customer = customer_repo.find_by_custom_id(custom_id)
            if customer is None:
                return True, []
            else:
                return True, [customer]
        except Exception as e:
            return False, f"error find custom_id : {custom_id} error : {e}"

    def find_by_first_name_last_name(self, first_name, last_name):
        try:
            customer_repo = CustomerRepository()
            return True, customer_repo.find_by_first_name_last_name(first_name, last_name)
        except Exception as e:
            return False, f"error find first_name : {first_name} last_name : {last_name} error : {e}"
