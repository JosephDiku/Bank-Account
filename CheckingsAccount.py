class CheckingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)

        self.transfer_limit = transfer_limit

    def checking_deposit(self, amount):
        if amount > self.transfer_limit:
            print("Deposit Declined! Amount Exceeds Transfer Limit")
        else:
            super().deposit(amount)

    def checking_withdraw(self, amount):
        if amount > self.transfer_limit:
            print("Withdraw Declined! Amount Exceeds Transfer Limit")
        else:
            super().withdraw(amount)