"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, pay_calc_string, pay):
        self.pay_calc_string = pay_calc_string
        self.pay = pay

    def get_pay(self):
        return self.pay

    def __str__(self):
        return self.pay_calc_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie works on a monthly salary of 4000.  Their total pay is 4000.", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.', 2500)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.', 3800)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.', 4410)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.', 3500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.', 4200)
