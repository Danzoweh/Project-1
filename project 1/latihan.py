class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product, quantity=1):
        self.cart.append({"product": product, "quantity": quantity})
        print(f"{quantity} x {product.name} added to cart.")

    def remove_product(self, product_name):
        for item in self.cart:
            if item['product'].name == product_name:
                self.cart.remove(item)
                print(f"{item['product'].name} removed from cart.")
                return
        print(f"{product_name} not found in the cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("Shopping Cart:")
        for item in self.cart:
            print(f"{item['quantity']} x {item['product']}")

    def calculate_total(self):
        total = 0
        for item in self.cart:
            total += item['product'].price * item['quantity']
        return total

# Menggunakan Kelas ShoppingCart
if __name__ == "__main__":
    # Membuat Produk
    apple = Product("Apple", 1.20)
    banana = Product("Banana", 0.80)
    orange = Product("Orange", 1.50)

    # Membuat Shopping Cart
    cart = ShoppingCart()

    # Menambahkan Produk ke Keranjang
    cart.add_product(apple, 3)
    cart.add_product(banana, 2)
    cart.add_product(orange, 12)

    # Melihat Isi Keranjang
    cart.view_cart()

    # Menghapus Produk dari Keranjang
    cart.remove_product("Banana")

    # Melihat Isi Keranjang Setelah Penghapusan
    cart.view_cart()

    # Menghitung Total Belanja
    total = cart.calculate_total()
    print(f"Total: ${total:.2f}")