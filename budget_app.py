# A Budget class that allows for deposit, withdrawal,
# and transfer across different categories like food, clothing, etc.
# Author: Kizito Ofoegbu
# References: Zuri Team, Ingressive4Good
# Date: 17-04-2021

class Budget:
    """
    A simple attempt to model a budget app using a class.
    This model allows you create instances of a class and transfer funds,
    withdraw, deposit and check balances like you would on a real budget app.
    """

    def __init__(self, category, amount):
        """Initialize attributes for the budget"""
        self.category = category.title()
        self.amount = amount
        self.withdraw = 0
        self.transfer = 0

    def deposit_funds(self):
        """Allow for depositing funds across categories"""
        deposit_bal = self.amount
        return f"\n\u20a6{deposit_bal} has been deposited " \
               f"into the {self.category.title()} category."

    def withdraw_funds(self, withdraw_amount):
        """Allow for withdrawal of funds across categories"""
        self.withdraw = withdraw_amount
        if self.withdraw < self.amount:
            self.amount -= self.withdraw
        elif self.withdraw == self.amount:
            self.amount -= self.withdraw

        return f"You have withdrawn \u20a6{self.withdraw}"

    def check_balance(self):
        """Check balance after a transaction"""
        if self.amount < 0:
            return f"Insufficient funds!"
        else:
            return f"The new balance for {self.category} is \u20a6{self.amount}"

    def transfer_funds(self, category_to_transfer, transfer_amount):
        """Allow for transfer of funds"""
        self.transfer = transfer_amount
        if self.transfer <= self.amount:
            self.amount -= self.transfer
            return f"\n\u20a6{self.transfer} has been " \
                   f"transferred to {str(category_to_transfer)} category. " \
                   f"Your new balance is \u20a6{self.amount}\n"
        else:
            return "\nYou do not have enough funds to make this transfer."


# Sample Test. Feel free to adjust the arguments for further testing.
category_1 = Budget('food', 50000)
print(category_1.deposit_funds())  # Test deposit
# print(category_1.withdraw_funds(50000))  # Test exceeded withdraw
print(category_1.check_balance())  # Test balance

category_2 = Budget('clothing', 35000)
print(category_2.deposit_funds())  # Test deposit
# print(category_1.withdraw_funds(10000))  # Test normal withdraw
print(category_2.check_balance())  # Test balance

# Test transfer
print(category_1.transfer_funds(category_2.category, 20000))
print(category_2.transfer_funds(category_1.category, 20000))

# Test that the balance for category_1 and 2 changed appropriately after the transfer
print(category_1.check_balance())
print(category_2.check_balance())