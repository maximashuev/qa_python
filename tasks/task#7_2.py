"""
Folow the steps bellow: -Create a new dictionary called prices using {} format like the example above.
Put these values in your prices dictionary:
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
●

●


"""
prices={
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
# Loop through each key in prices. For each key, print out the key along with its price and stock information. Print the answer in the following format:
# apple
# price: 2
# stock: 0
for i,j in prices.items():
    print(i+"\n"+"price:",j,"\n","stock:",stock[i],"\n")

# ●	Let's determine how much money you would make if you sold all of your food.
#     ○	Create a variable called total and set it to zero.
#     ○	Loop through the prices dictionaries.For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
#     ○	Finally, outside your loop, print total.
total=0
for i,j in prices.items():
    print(j*stock[i])
    total+=(j*stock[i])
print(total)