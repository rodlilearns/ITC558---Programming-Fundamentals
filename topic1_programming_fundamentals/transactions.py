# Topic 1 Excercise 3
# Calculate stock transaction details

class stock_transaction_details:
    def __init__(self, shares, purchase_price, purchase_commission, sale_price, sale_commission):
        self.shares = shares
        self.purchase_price = purchase_price
        self.purchase_commission = purchase_commission
        self.sale_price = sale_price
        self.sale_commission = sale_commission

    def purchase_amount(self):
        return self.shares * self.purchase_price
    
    def purchase_commission_amount(self):
        return self.purchase_amount() * self.purchase_commission / 100
    
    def sale_amount(self):
        return self.shares * self.sale_price
    
    def sale_commission_amount(self):
        return self.sale_amount() * self.sale_commission / 100
    
    def net_profit(self):
        return self.sale_amount() - self.sale_commission_amount() - self.purchase_amount() - self.purchase_commission_amount()
    

# Create an instance of Stock class with purchase and sale details
transaction_1 = stock_transaction_details(shares=500, purchase_price=25.04, purchase_commission=2.3, sale_price=36.06, sale_commission=2.1)

# Display results
print("Money paid for the stock: ", transaction_1.purchase_amount())
print("Commission paid on purchase: ", transaction_1.purchase_commission_amount())
print("Sale price: ", transaction_1.sale_amount())
print("Sale commission: ", transaction_1.sale_commission_amount())
print("Net profit: ", transaction_1.net_profit())

