class Category:
    
    def __init__(self, name):
        """
        Initializes a Category object with a name and an empty ledger.
        """
        self.ledger = []  # Stores transaction records
        self.name = name  # Name of the category

    def __str__(self):
        """
        Returns a formatted string representation of the category.
        """
        # Step 1: Title line (Category name centered within 30 '*' characters)
        title = self.name.center(30, "*") 
        
        # Step 2: Ledger entries formatted correctly
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23]  # Truncate description to 23 characters
            amount = f"{entry['amount']:>7.2f}"  # Right-align amount with 2 decimal places
            items += f"{description:<23}{amount}\n"  # Left-align description

        # Step 3: Total balance
        total = f"Total: {self.get_balance():.2f}"

        # Step 4: Combine everything into the final output
        return f"{title}\n{items}{total}"

    def deposit(self, amount, description=''):
        """
        Adds a deposit to the ledger.
        """
        self.ledger.append({'amount': amount, 'description': description})
    
    def get_balance(self):
        """
        Returns the current balance of the category.
        """
        return sum(item['amount'] for item in self.ledger)

    def withdraw(self, amount, description=''):
        """
        Withdraws an amount from the category if there are sufficient funds.
        """
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True  # Successful withdrawal
        return False  # Insufficient funds
    
    def transfer(self, amount, category):
        """
        Transfers an amount to another category.
        """
        # Check if there are enough funds
        if self.check_funds(amount):
            # Withdraw from this category
            self.withdraw(amount, f"Transfer to {category.name}")
            # Deposit into the target category
            category.deposit(amount, f"Transfer from {self.name}") 
            return True  # Transfer successful
        return False  # Not enough funds, transfer fails

    def check_funds(self, amount):
        """
        Checks if there are enough funds in the category.
        Returns True if there are sufficient funds, False otherwise.
        """
        return amount <= self.get_balance()


def create_spend_chart(categories):
    """
    Creates a bar chart showing spending percentages per category.
    """
    # Get total withdrawals per category
    spent = {category.name: sum(-item["amount"] for item in category.ledger if item["amount"] < 0) for category in categories}

    # Calculate percentages
    total_spent = sum(spent.values())
    percentages = {name: (spent[name] / total_spent) * 100 for name in spent}

    # Round down to nearest 10
    percentages = {name: (percentages[name] // 10) * 10 for name in spent}

    # Build the chart header
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        row = f"{i:>3}| "  # Right-align percentage labels
        for name in spent:
            row += "o  " if percentages[name] >= i else "   "  # Align category bars
        chart += row + "\n"

    # Add the horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Format category names vertically
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        row = "     "  # Align below the chart
        for category in categories:
            row += (category.name[i] + "  ") if i < len(category.name) else "   "
        chart += row.rstrip() + "  \n"  # **Ensure two spaces after last category**

    return chart.rstrip("\n")  # Remove final newline
