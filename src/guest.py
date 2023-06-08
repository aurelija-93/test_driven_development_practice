class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def has_cash(self, cash):
        return self.wallet >= cash
    
    def remove_cash(self, cash):
        if self.has_cash(cash):
            self.wallet -= cash

    def whoo(self):
        return "Whoo!"
    
    def boo(self):
        return "Boo!"