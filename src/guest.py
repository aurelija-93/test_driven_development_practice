class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def has_cash(self, cash):
        return self.wallet >= cash
    
    def remove_cash(self, cash):
        if self.has_cash(cash):
            self.wallet -= cash