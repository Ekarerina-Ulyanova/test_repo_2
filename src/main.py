import tkinter as tk
from tkinter import messagebox
from budget_manager import BudgetManager

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Manager")
        
        self.budget_manager = BudgetManager()

        self.create_widgets()
        self.update_expense_list()

    def create_widgets(self):
        self.budget_label = tk.Label(self.root, text= f"Current Budget: ${self.budget_manager.get_current_budget():.2f}")
        self.budget_label.pack()

        self.budget_entry = tk.Entry(self.root)
        self.budget_entry.pack()
        self.budget_entry.insert(0, "")

        self.add_budget_button = tk.Button(self.root, text="Add Budget", command=self.add_budget)
        self.add_budget_button.pack()

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()
        self.amount_entry.insert(0, "")

        self.category_entry = tk.Entry(self.root)
        self.category_entry.pack()
        self.category_entry.insert(0, "")

        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack()
        self.description_entry.insert(0, "")

        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        self.expense_listbox = tk.Listbox(self.root)
        self.expense_listbox.pack()

        self.remove_button = tk.Button(self.root, text="Remove Expense", command=self.remove_expense)
        self.remove_button.pack()

        self.view_button = tk.Button(self.root, text="View Monthly Info", command=self.view_monthly_info)
        self.view_button.pack()

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            self.amount_entry.delete(0, tk.END)
            category = self.category_entry.get()
            self.category_entry.delete(0, tk.END)
            description = self.description_entry.get()
            self.description_entry.delete(0, tk.END)
            if amount <= self.budget_manager.get_current_budget():
                self.budget_manager.add_budget(-amount)
                self.update_budget_label()
                self.budget_manager.add_expense(amount, category, description)
                self.update_expense_list()
                messagebox.showinfo("Success", "Transaction added!")
            else:
                messagebox.showwarning("Error", "Transaction amount exceeds remaining budget.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def remove_expense(self):
        selected_index = self.expense_listbox.curselection()
        if selected_index:
            amount = self.budget_manager.get_expense_amount(selected_index[0])
            self.budget_manager.add_budget(amount)
            self.update_budget_label()
            self.budget_manager.remove_expense(selected_index[0])
            self.update_expense_list()
            messagebox.showinfo("Success", "Expense removed successfully!")
        else:
            messagebox.showwarning("Warning", "Select an expense to remove.")

    def add_budget(self):
        try:
            amount = float(self.budget_entry.get())
            self.budget_manager.add_budget(amount)
            self.update_budget_label()
            self.budget_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Budget updated successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            self.budget_entry.delete(0, tk.END)

    def view_monthly_info(self):
        info = self.budget_manager.view_monthly_info()
        messagebox.showinfo("Monthly Info", info)

    def update_expense_list(self):
        self.expense_listbox.delete(0, tk.END)
        for expense in self.budget_manager.get_expenses():
            self.expense_listbox.insert(tk.END, expense)

    def update_budget_label(self):
        budget = self.budget_manager.get_current_budget()
        self.budget_label.config(text=f"Current Budget: ${budget:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
