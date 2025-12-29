from src.database import Database

class BudgetManager:
    """Custom class"""
    def __init__(self):
        self.db = Database()

    def add_expense(self, amount, category, description):
        return self.db.add_expense(amount, category, description)

    def remove_expense(self, index):
        expenses = self.db.get_expenses()
        expense_id = expenses[index][0]
        return self.db.remove_expense(expense_id)

    def get_expense_amount(self, index):
        expenses = self.db.get_expenses()
        expense_amount = expenses[index][1]
        return expense_amount

    def add_budget(self, amount):
        return self.db.add_budget(amount)

    def get_current_budget(self):
        return self.db.get_current_budget()

    def get_expenses(self):
        return [f"${exp[1]:.2f} - {exp[2]}: {exp[3]}" for exp in self.db.get_expenses()]

    def view_monthly_info(self):
        return self.db.view_monthly_info()

    def clear_data(self):
        self.db.clear()

    def close(self):
        return self.db.close()
