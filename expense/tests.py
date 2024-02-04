from django.test import TestCase
from .models import Expense


class ExpenseModelTest(TestCase):
    def setUp(self):
        # Create a sample Expense instance for testing
        self.test_expense = Expense.objects.create(
            customer_name="Test Customer",
            category="pedicure",
            income_spent="Income",
            amount=50.0,
            memo="Test Memo",
        )

    def test_model_total_calculation(self):
        # Test the total calculation in the save method for income
        new_expense_income = Expense.objects.create(
            customer_name="New Customer Income",
            category="manicure",
            income_spent="Income",
            amount=30.0,
            memo="New Memo Income",
        )
        self.assertEqual(
            new_expense_income.total, 30.0
        )  # Update this line with the expected total
