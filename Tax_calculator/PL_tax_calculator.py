"""Poland Net Income Calculator

This script calculates the net income for employees in Poland based on gross salary.
Deductions include social security contributions (ZUS), health insurance, and income tax.
The calculation follows Polish tax regulations as of the current year.
"""

import customtkinter as c_tkinter

class TaxCalculator:
    def __init__(self):
        """Initialize the GUI window and its components."""
        self.window = c_tkinter.CTk()
        self.window.title("Poland Net Income Calculator")
        self.window.geometry("320x350")
        self.window.resizable(False, False)

        self.padding = {'padx': 15, 'pady': 10}

        # Gross salary input
        self.income_label = c_tkinter.CTkLabel(self.window, text="Gross Salary:")
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = c_tkinter.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Net income output
        self.result_label = c_tkinter.CTkLabel(self.window, text="Net Income:")
        self.result_label.grid(row=1, column=0, **self.padding)
        self.result_entry = c_tkinter.CTkEntry(self.window)
        self.result_entry.insert(0, '0')
        self.result_entry.grid(row=1, column=1, **self.padding)

        # Social security contributions (ZUS) output
        self.zus_label = c_tkinter.CTkLabel(self.window, text="ZUS Deductions:")
        self.zus_label.grid(row=2, column=0, **self.padding)
        self.zus_entry = c_tkinter.CTkEntry(self.window)
        self.zus_entry.insert(0, '0')
        self.zus_entry.grid(row=2, column=1, **self.padding)

        # Health insurance output
        self.health_label = c_tkinter.CTkLabel(self.window, text="Health Insurance:")
        self.health_label.grid(row=3, column=0, **self.padding)
        self.health_entry = c_tkinter.CTkEntry(self.window)
        self.health_entry.insert(0, '0')
        self.health_entry.grid(row=3, column=1, **self.padding)

        # Income tax output
        self.tax_label = c_tkinter.CTkLabel(self.window, text="Income Tax:")
        self.tax_label.grid(row=4, column=0, **self.padding)
        self.tax_entry = c_tkinter.CTkEntry(self.window)
        self.tax_entry.insert(0, '0')
        self.tax_entry.grid(row=4, column=1, **self.padding)

        # Calculate button
        self.calculate_btn = c_tkinter.CTkButton(self.window, text="Calculate", command=self.calculate_net_income)
        self.calculate_btn.grid(row=5, column=1, **self.padding)

    def update_result(self, entry, text):
        """Clear the existing content of the entry and insert new text."""
        entry.delete(0, c_tkinter.END)
        entry.insert(0, text)

    def calculate_net_income(self):
        """Calculate the net income based on Polish tax regulations."""
        try:
            income = float(self.income_entry.get())
            if income <= 0:
                raise ValueError("Income must be positive.")

            # Social security contributions (ZUS) calculations
            pension = income * 0.0976  # Retirement contribution
            disability = income * 0.015  # Disability contribution
            sickness = income * 0.0245  # Sickness contribution
            zus_total = pension + disability + sickness

            # Health insurance calculation
            health_insurance_base = income - zus_total
            health_insurance = health_insurance_base * 0.09

            # Income tax (PIT) calculations
            tax_free_allowance = 300  # Monthly allowance in PLN
            deductible_health = health_insurance_base * 0.0775
            taxable_income = max(0, health_insurance_base - tax_free_allowance)
            income_tax = (taxable_income * 0.12 if taxable_income <= 10000 
                          else 10000 * 0.12 + (taxable_income - 10000) * 0.32)
            income_tax -= deductible_health
            income_tax = max(0, income_tax)

            # Final net income calculation
            net_income = income - zus_total - health_insurance - income_tax

            # Update results in the GUI
            self.update_result(self.result_entry, f"{net_income:,.2f} PLN")
            self.update_result(self.zus_entry, f"{zus_total:,.2f} PLN")
            self.update_result(self.health_entry, f"{health_insurance:,.2f} PLN")
            self.update_result(self.tax_entry, f"{income_tax:,.2f} PLN")
        except ValueError as e:
            self.update_result(self.result_entry, str(e))

    def run(self):
        """Run the main GUI loop."""
        self.window.mainloop()

if __name__ == "__main__":
    tc = TaxCalculator()
    tc.run()