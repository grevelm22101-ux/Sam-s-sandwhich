def meat_selection():
    meat_list=["Salami","Chicken","Italian Meatball","Steak","No Meat"]
    count=0
    print("We have the following meat options:")
    while count < len(meat_list): #prints out each item on the list
        print(count+1," ", bread_list[count])
        count+=1
    meat_selected=int(input("What meat did you want? Enter a number"))
    return meat_list[meat_selected - 1] #returns back a string

def bread_selection():
    bread_list = ["White", "Brown", "Italian", "Granary"]
    count=0
    print("We have the following breads:")
    while count < len(bread_list): #prints out each item on the list
        print(count+1," ", bread_list[count])
        count += 1
    bread_selected=int(input("Which bread did you want? Enter a number"))
    return bread_list[bread_selected - 1] #returns back a string

#main program
print("Welcome to Sam's Sandwhich Shop")
bread_choice=bread_selection() #creating a variable that calls up the bread function and returns their choice
print(f"Your selecred bread: {bread_choice}")
meat_choice=meat_selection()
print(f"Your selecred meat: {meat_choice}")