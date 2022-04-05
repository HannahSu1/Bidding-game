from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo 
print(logo)

next_one_flag = "Yes"
dic = {}

while next_one_flag == "Yes":

    name = input("Print your name:") 
    price = input("Add your bid price:")
    dic[name] = int(price)
    
    next_one_flag = input("If other users who want to bid: Type 'Yes' or 'No'.")
    if next_one_flag == "Yes":
        clear()
    elif next_one_flag == "No":
        clear()
        winner_name = max(dic, key=dic.get)
        print(f"The winner is {winner_name}")
                 
