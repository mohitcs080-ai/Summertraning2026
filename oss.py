import tkinter as tk
from tkinter import messagebox


# ============================================================
# PRODUCT DATA
# ============================================================

products = [
    ("Laptop", 50000),
    ("Mobile", 20000),
    ("Apple", 10000),
    ("Headphones", 2000),
    ("Smart Watch", 3000),
    ("Keyboard", 1500),
    ("Mouse", 800),
    ("Monitor", 12000),
    ("Tablet", 25000)
]

cart = []


# ============================================================
# COLORS
# ============================================================

BG_COLOR = "#EAF2F8"
HEADER_COLOR = "#1F4E78"
CARD_COLOR = "#FFFFFF"
BUTTON_COLOR = "#2874A6"
BUTTON_HOVER = "#1A5276"
TEXT_COLOR = "#17202A"
PRICE_COLOR = "#229954"
DANGER_COLOR = "#C0392B"


# ============================================================
# BUTTON HOVER EFFECT
# ============================================================

def button_hover(button, normal_color, hover_color):

    button.bind(
        "<Enter>",
        lambda event: button.config(bg=hover_color)
    )

    button.bind(
        "<Leave>",
        lambda event: button.config(bg=normal_color)
    )


# ============================================================
# ADD PRODUCT TO CART
# ============================================================

def add_to_cart(product):

    cart.append(product)

    messagebox.showinfo(
        "Shopping Cart",
        f"{product[0]} added to cart successfully!"
    )


# ============================================================
# CREATE PRODUCT CARD
# ============================================================

def create_product_card(name, price):

    card = tk.Frame(
        product_frame,
        bg=CARD_COLOR,
        relief="raised",
        bd=2,
        width=300,
        height=190
    )

    card.pack(
        side="left",
        padx=10,
        pady=10
    )

    card.pack_propagate(False)

    # Product icon
    icon = "💻"

    if name == "Mobile":
        icon = "📱"
    elif name == "Headphones":
        icon = "🎧"
    elif name == "Smart Watch":
        icon = "⌚"
    elif name == "Keyboard":
        icon = "⌨️"
    elif name == "Mouse":
        icon = "🖱️"
    elif name == "Monitor":
        icon = "🖥️"
    elif name == "Tablet":
        icon = "📱"

    tk.Label(
        card,
        text=icon,
        font=("Arial", 35),
        bg=CARD_COLOR
    ).pack(pady=5)

    tk.Label(
        card,
        text=name,
        font=("Arial", 14, "bold"),
        bg=CARD_COLOR,
        fg=TEXT_COLOR
    ).pack()

    tk.Label(
        card,
        text=f"₹{price:,}",
        font=("Arial", 13, "bold"),
        bg=CARD_COLOR,
        fg=PRICE_COLOR
    ).pack(pady=5)

    add_button = tk.Button(
        card,
        text="Add to Cart",
        font=("Arial", 10, "bold"),
        bg=BUTTON_COLOR,
        fg="white",
        activebackground=BUTTON_HOVER,
        activeforeground="blue",
        relief="flat",
        cursor="hand2",
        command=lambda p=(name, price): add_to_cart(p)
    )

    add_button.pack(pady=5)

    button_hover(
        add_button,
        BUTTON_COLOR,
        BUTTON_HOVER
    )


# ============================================================
# DISPLAY ALL PRODUCTS
# ============================================================

def show_all_products():

    search_entry.delete(0, tk.END)

    for widget in product_frame.winfo_children():
        widget.destroy()

    for name, price in products:
        create_product_card(name, price)


# ============================================================
# SEARCH PRODUCTS
# ============================================================

def search_products():

    search_text = search_entry.get().strip().lower()

    for widget in product_frame.winfo_children():
        widget.destroy()

    if search_text == "":
        show_all_products()
        return

    found = False

    for name, price in products:

        if search_text in name.lower():

            create_product_card(name, price)

            found = True

    if not found:

        tk.Label(
            product_frame,
            text="❌ No product found!",
            font=("Arial", 18, "bold"),
            bg=BG_COLOR,
            fg=DANGER_COLOR
        ).pack(pady=50)


# ============================================================
# REMOVE PRODUCT FROM CART
# ============================================================

def remove_from_cart(index, cart_window):

    del cart[index]

    cart_window.destroy()

    show_cart()


# ============================================================
# PLACE ORDER
# ============================================================

def place_order(cart_window):

    if not cart:

        messagebox.showwarning(
            "Empty Cart",
            "Your shopping cart is empty!"
        )

        return

    total = sum(
        price for name, price in cart
    )

    result = messagebox.askyesno(
        "Confirm Order",
        f"Total Amount: ₹{total:,}\n\n"
        "Do you want to place this order?"
    )

    if result:

        cart.clear()

        messagebox.showinfo(
            "Order Successful",
            "🎉 Order placed successfully!\n\n"
            "Thank you for shopping with us!"
        )

        cart_window.destroy()


# ============================================================
# SHOW SHOPPING CART
# ============================================================

def show_cart():

    cart_window = tk.Toplevel(root)

    cart_window.title("Shopping Cart")

    cart_window.geometry("1550x1550")

    cart_window.configure(
        bg=BG_COLOR
    )

    cart_window.resizable(False, False)

    # Header
    tk.Label(
        cart_window,
        text="🛒 MY SHOPPING CART",
        font=("Arial", 2, "bold"),
        bg=HEADER_COLOR,
        fg="white",
        pady=15
    ).pack(fill="x")

    # Empty cart
    if not cart:

        tk.Label(
            cart_window,
            text="Your cart is empty!",
            font=("Arial", 18, "bold"),
            bg=BG_COLOR,
            fg=DANGER_COLOR
        ).pack(pady=80)

        close_button = tk.Button(
            cart_window,
            text="Close",
            width=20,
            bg=BUTTON_COLOR,
            fg="white",
            font=("Arial", 11, "bold"),
            command=cart_window.destroy
        )

        close_button.pack()

        button_hover(
            close_button,
            BUTTON_COLOR,
            BUTTON_HOVER
        )

        return

    # Items frame
    items_frame = tk.Frame(
        cart_window,
        bg=BG_COLOR
    )

    items_frame.pack(
        fill="both",
        expand=False,
        padx=20,
        pady=20
    )

    total = 0

    for index, (name, price) in enumerate(cart):

        item_frame = tk.Frame(
            items_frame,
            bg=CARD_COLOR,
            relief="raised",
            bd=1,
            padx=10,
            pady=10
        )

        item_frame.pack(
            fill="x",
            pady=5
        )

        tk.Label(
            item_frame,
            text=name,
            font=("Arial", 12, "bold"),
            bg=CARD_COLOR,
            fg=TEXT_COLOR
        ).pack(
            side="left"
        )

        tk.Label(
            item_frame,
            text=f"₹{price:,}",
            font=("Arial", 12, "bold"),
            bg=CARD_COLOR,
            fg=PRICE_COLOR
        ).pack(
            side="left",
            padx=50
        )

        remove_button = tk.Button(
            item_frame,
            text="Remove",
            bg=DANGER_COLOR,
            fg="white",
            font=("Arial", 9, "bold"),
            relief="flat",
            cursor="hand2",
            command=lambda i=index:
                remove_from_cart(i, cart_window)
        )

        remove_button.pack(side="right")

        total += price

    # Total
    tk.Label(
        cart_window,
        text=f"TOTAL: ₹{total:,}",
        font=("Arial", 20, "bold"),
        bg=BG_COLOR,
        fg=PRICE_COLOR
    ).pack(pady=10)

    # Place Order
    order_button = tk.Button(
        cart_window,
        text="💳 PLACE ORDER",
        width=25,
        height=2,
        bg=BUTTON_COLOR,
        fg="white",
        font=("Arial", 12, "bold"),
        relief="flat",
        cursor="hand2",
        command=lambda:
            place_order(cart_window)
    )

    order_button.pack(pady=5)

    button_hover(
        order_button,
        BUTTON_COLOR,
        BUTTON_HOVER
    )

    # Close
    close_button = tk.Button(
        cart_window,
        text="Close",
        width=25,
        bg="#7F8C8D",
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        command=cart_window.destroy
    )

    close_button.pack(pady=5)


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Online Shopping System"
)

root.geometry(
    "1400x240"
)

root.configure(
    bg=BG_COLOR
)

root.resizable(
    False,
    True
)


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    root,
    bg=HEADER_COLOR,
    height=100
)

header.pack(
    fill="x"
)

tk.Label(
    header,
    text="🛒 ONLINE SHOPPING SYSTEM",
    font=("Arial", 28, "bold"),
    bg=HEADER_COLOR,
    fg="white"
).pack(pady=25)


# ============================================================
# SEARCH SECTION
# ============================================================

search_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

search_frame.pack(
    pady=20
)

search_entry = tk.Entry(
    search_frame,
    width=40,
    font=("Arial", 14),
    relief="solid",
    bd=1
)

search_entry.pack(
    side="left",
    padx=5,
    ipady=8
)


search_button = tk.Button(
    search_frame,
    text="🔍 Search",
    width=12,
    height=2,
    bg=BUTTON_COLOR,
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    command=search_products
)

search_button.pack(
    side="left",
    padx=5
)

button_hover(
    search_button,
    BUTTON_COLOR,
    BUTTON_HOVER
)


all_button = tk.Button(
    search_frame,
    text="Show All",
    width=12,
    height=2,
    bg="#5D6D7E",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    command=show_all_products
)

all_button.pack(
    side="left",
    padx=5
)


# ============================================================
# PRODUCT SECTION
# ============================================================

tk.Label(
    root,
    text="Available Products",
    font=("Arial", 20, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
).pack()


product_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

product_frame.pack(
    pady=10
)


# Display products
show_all_products()


# ============================================================
# VIEW CART BUTTON
# ============================================================

cart_button = tk.Button(
    root,
    text="🛒 VIEW CART",
    width=30,
    height=2,
    bg="#27AE60",
    fg="white",
    font=("Arial", 13, "bold"),
    relief="flat",
    cursor="hand2",
    command=show_cart
)

cart_button.pack(
    pady=20
)

button_hover(
    cart_button,
    "#27AE60",
    "#1E8449"
)


# ============================================================
# FOOTER
# ============================================================

tk.Label(
    root,
    text="Online Shopping System | Developed using Python & Tkinter",
    font=("Arial", 10),
    bg=BG_COLOR,
    fg="#566573"
).pack(
    side="bottom",
    pady=10
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()

