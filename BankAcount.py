class BankAccount:
    title = "Scope Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

        self._account_number = account_number # Protected
        self.__routing_number = routing_number # Private

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("Transaction Declined! Amount Would Fall Below Minimum Balance ")
        else:
            self.current_balance -= amount

    def print_customer_information(self):
        return f"Bank: {self.title}\nCustomer: {self.customer_name}\nCurrent Balance: ${self.current_balance}\nMinimum Balance: ${self.minimum_balance}"