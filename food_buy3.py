# Dictionary
d = {
    "alu": 7,
    "vegetable": 8,
    "dim": 10,
    "singara": 7,
    "egg_roll": 40,
    "beguni": 6,
    "pokora": 8,
    "onion": 6
}
print("Available items:", list(d.keys()))
a=int(input("kota jinish neben?\n"))
cart={}
# minimum a different items must be selected
while len(cart) < a:
    n=input("kon chop neben?\n").strip().lower()
    if n not in d:
        print(n, "hobe na dada.")
        continue
    if n in cart:
        print(n, "already neya hoye geche, onno item nao.")
        continue
    print(n, "hobe, dam ₹", d[n])
    m=int(input("kota nebe?\n"))
    cart[n]=m
# calculate total
total=0
for item, qty in cart.items():
    print(item)# kon chop neben seta
    print(qty)# sei chop kota neben seta
    total = total + qty * d[item]
print("\n--- BILL ---")
for item, qty in cart.items():
    print(item, "x", qty, "=", qty * d[item])
print("apnar mot dam holo ₹", total)