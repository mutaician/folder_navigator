# Budget app


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # deposit method
    def deposit(self, amount: int, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # withdraw method
    def withdraw(self, amount: int, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    # get balance
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    # transfer funds
    def transfer(self, amount: int, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    # check funds
    def check_funds(self, amount: int):
        return self.get_balance() >= amount

    # print budget
    def __str__(self) -> str:
        title_line = self.name.center(30, "*")
        # items in ledger
        items = ""
        for item in self.ledger:
            items += f"{item['description'][0:23]:23s}{item['amount']:>7.2f}\n"
        # total balance
        total_balance = self.get_balance()
        return f"{title_line}\n{items}Total: {total_balance:.2f}"


# create spending bar chart
def create_spend_chart(categories):
    # category names and each withdrawals
    category_info = [
        (
            category.name,
            [abs(entry["amount"]) for entry in category.ledger if entry["amount"] < 0],
        )
        for category in categories
    ]
    # total withdrawals
    total_withdrawals = sum([sum(withdrawals) for _, withdrawals in category_info])
    # percentages spent
    percentages = [
        (category, (sum(withdrawals) / total_withdrawals * 100 // 10) * 10)
        for category, withdrawals in category_info
    ]
    # title
    result = "Percentage spent by category\n"
    # bar chart
    for i in range(100, -10, -10):
        dots = ""
        for _, percentage in percentages:
            if percentage >= i:
                dots += "o  "
            else:
                dots += "   "
        result += f"{i:>3}| {dots}\n"
    # formart category names
    max_len = max([len(category) for category, _ in percentages])
    result += "    " + "-" * ((len(category_info) + 2) * 2)
    for j in range(max_len):
        result += "\n     "
        for category, _ in percentages:
            if len(category) > j:
                result += category[j] + "  "
            else:
                result += "   "

    return result

# tests
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(business)
print(food)
print(entertainment)

print(create_spend_chart([business, food, entertainment]))
