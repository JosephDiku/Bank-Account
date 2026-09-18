import SavingsAccount
import CheckingsAccount


user1 = CheckingsAccount.CheckingsAccount("Neymar Junior", 50000, 5000, "123456789", "987654321", 1000)

user2 = CheckingsAccount.CheckingsAccount("Lionel Messi", 75000, 5000, "234567890", "098765432", 2000)

user3 = SavingsAccount.SavingsAccount("Cristiano Ronaldo", 100000, 10000, "345678901", "109876543", 0.05)

user4 = SavingsAccount.SavingsAccount("Kylian Mbappe", 125000, 10000, "456789012", "210987654", 0.08)

print("Checkings Account for User 1: ")
print(f"Original Balnce: ${user1.current_balance}")
user1.checking_deposit(500)
print("Deposited $500")
print("Attempting to withdraw $5000")
user1.checking_withdraw(5000)
print(user1.print_customer_information())
print()

print("Checkings Account for User 2: ")
print(f"Original Balnce: ${user2.current_balance}")
user2.checking_deposit(300)
print("Deposited $300")
print("Attempting to withdraw $1000")
user2.checking_withdraw(1000)
print(user2.print_customer_information())
print()

print("Savings Account for User 3: ")
print(f"Original Balnce: ${user3.current_balance}")
print(f"Interest Rate: {user3.interest_rate}")
user3.apply_interest()
print("User 3 Info:")
print(user3.print_customer_information())
print()

print("Savings Account for User 4: ")
print(f"Original Balnce: ${user4.current_balance}")
print(f"Interest Rate: {user4.interest_rate}")
user4.apply_interest()
print("User 4 Info:")
print(user4.print_customer_information())
print()