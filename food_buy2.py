#Dictionary
d={
    "alu":7,
    "vegetable":8,
    "dim":10,
    "singara":7,
    "egg_roll":40,
    "beguni":6,
    "pokora":8,
    "onion":6
}
print("Available items:", list(d.keys()))
n=input("kon chop nebe?\n")
if n in d:
    print(n, "hobe, dam ₹", d.get(n))
else:
    print(n, "hobe na dada.")
    exit(0)
m=int(input("kota nebe?\n"))
total=m*d.get(n)
print("apnar mot dam holo ₹",total)