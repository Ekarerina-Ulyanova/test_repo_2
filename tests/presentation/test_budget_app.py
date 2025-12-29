import pytest
from main import BudgetApp
import tkinter as tk
from tkinter import messagebox

def mock_showinfo(title, message):
    pass
def mock_showwarning(title, message):
    pass
def mock_showerror(title, message):
    pass

@pytest.fixture
def app():
    root = tk.Tk()
    app = BudgetApp(root)
    yield app
    app.budget_manager.clear_data()
    root.destroy()

@pytest.fixture(autouse=True)
def override_messagebox():
    original_showinfo = messagebox.showinfo
    original_showwarning = messagebox.showwarning
    original_showerror = messagebox.showerror

    messagebox.showinfo = mock_showinfo
    messagebox.showwarning = mock_showwarning
    messagebox.showerror = mock_showerror

    yield

    messagebox.showinfo = original_showinfo
    messagebox.showwarning = original_showwarning
    messagebox.showerror = original_showerror

def test_add_budget(app):
    app.budget_entry.insert(0, "1000")
    app.add_budget()
    app.budget_entry.insert(0, "500")
    app.add_budget()
    assert app.budget_manager.get_current_budget() == 1500.0

def test_add_expense(app):
    app.budget_entry.insert(0, "1000")
    app.add_budget()
    app.amount_entry.insert(0, "200")
    app.category_entry.insert(0, "Food")
    app.description_entry.insert(0, "Groceries")
    app.add_expense()
    assert app.budget_manager.get_current_budget() == 800.0
    assert len(app.budget_manager.get_expenses()) == 1

def test_expense_more_than_in_budget(app):
    app.budget_entry.insert(0, "1000")
    app.add_budget()
    app.amount_entry.insert(0, "1200")
    app.category_entry.insert(0, "Car")
    app.description_entry.insert(0, "Rent for 3 days")
    app.add_expense()
    assert app.budget_manager.get_current_budget() == 1000.0
    assert len(app.budget_manager.get_expenses()) == 0

def test_remove_expense(app):
    app.budget_entry.insert(0, "1000")
    app.add_budget()
    app.amount_entry.insert(0, "200")
    app.category_entry.insert(0, "Food")
    app.description_entry.insert(0, "Groceries")
    app.add_expense()
    app.expense_listbox.selection_set(0)
    app.remove_expense()
    assert app.budget_manager.get_current_budget() == 1000.0
    assert len(app.budget_manager.get_expenses()) == 0

def test_view_monthly_info(app):
    app.budget_entry.insert(0, "1000")
    app.add_budget()
    app.amount_entry.insert(0, "200")
    app.category_entry.insert(0, "Food")
    app.description_entry.insert(0, "Groceries")
    app.add_expense()
    app.amount_entry.insert(0, "10")
    app.category_entry.insert(0, "Entertainment")
    app.description_entry.insert(0, "Theater")
    app.add_expense()
    info = app.budget_manager.view_monthly_info()
    assert "Total Expenses: $210.00" in info

if __name__ == "__main__":
    pytest.main()
