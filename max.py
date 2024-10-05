class a:
    def buy(self):
        print("Buying a product")
class b:
    def buy(self):
        print("Buying a product1")
class c(b,  a):
    def buy(self):
        print("hi")  # Corrected: Removed the parentheses

x = c()
x.buy()