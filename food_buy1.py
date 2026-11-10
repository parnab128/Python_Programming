#do it in string
food=["Potato=₹5", "Vegetable=₹6", "Egg=₹10", "Singara=₹7", "Egg_roll=₹40", "Brinjal=₹6", "Pakora=₹8", "Onion=₹5"]
print(food)
a=int(input("Enter number of Potato: "))
b=int(input("Enter number of Vegetable: "))
c=int(input("Enter number of Egg: "))
d=int(input("Enter number of Singara: "))
e=int(input("Enter number of Egg_roll "))
f=int(input("Enter number of Brinjal: "))
g=int(input("Enter number of Pakora: "))
h=int(input("Enter number of Onion: "))
i=(a*5)+(b*6)+(c*10)+(d*7)+(e*40)+(f*6)+(g*8)+(h*5)
print("Total amount is: ₹",i)