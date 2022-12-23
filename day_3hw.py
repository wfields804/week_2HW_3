# I am buildig this code from the ground up
#I went and re read if statements, and inputs to start
#Next I will go over the lecture and read about dictionaries
#I have read that for this excerise we start with a empty bracket 
#I tried to use a bunch of if statements but when a if statement runs it does not read the next line of code
#I think I need to use else: to continue the code.... maybe a for loop but I dont think so
#Else statement not working, elif always had a "expected expression" error idk why. Trying a series of independent if statments next
#I noticed for my dictoinary I could not list multiple categories under 1 dictionary example below
# grocery_list {"dairy:" "cheese, milk, ice cream, creamer"
#               "meats:" "turkey, chicken, beef, fish"}
#There was a example in the lecture plan that looked like this 
# people = {
    #'Max': 'blue',
    #'Lilly': 'brown',
    #'Barney': 'blue',
    #'Larney': 'brown',
    #'Ted': 'purple'}




dairy_list = {}

grocery = input("Type dairy to view products. ")
add_dairy_to_list = {}
view_list = print(dairy_list)
continue_shopping = grocery

if grocery == "dairy":
    input("cheese, milk, ice cream, or creamer ? ") 

if grocery != "dairy":
    input("Type dairy to view products. ")
    while grocery != "dairy":
        input("Error, please type dairy to start over ")
        if grocery == "dairy":
            input("Type dairy to view products.  ")
            break
    
if grocery == "cheese" or "milk" or "ice cream" or "creamer":
    if grocery == "cheese" or "milk" or "ice cream" or "creamer":
        input("add_dairy_to_list, continue_shopping, view_list or, quit   ")
if add_dairy_to_list == "cheese":
    dairy_list["cheese"]
if add_dairy_to_list == "milk":
    dairy_list["milk"]
if add_dairy_to_list == "ice cream":
    dairy_list["ice cream"]
if add_dairy_to_list =="creamer":
    add_dairy_to_list["creamer"]
if add_dairy_to_list == "add_dairy_to_list":
    input("added to list \n new item or quit")



#I gave it a try from using book and not internet
#I did not look at lecture, I wanted to create it from scratch. Models wont be there come interview day. 

#My idea was to have user pick an item from presented list

#after user picks 1 of the items, have output add to list, continue shopping, view list or quit

#If user added to list, I wanted the output to add item to list and then send user back to item list or quit


#If user continued shopping, have output send user back to item list or quit but not add item to list

#If user viewed list, have output show current list then send user back to item list

#Quit is quit

#I also had a list of meats to choose from, that would run same as dairy list. 
#But the if statements kept running out of the order I had in my head



# SSSSSSOOOOOOOOOOOOOO
# I think that this is a super-cool direction BUT it just so happens that this particular assignment we're 
# going to continue building on so it'll be easier to be a little more typical

# basic layout idea:

def shop():
    cart = {}
    while True:
        main = input('show/add/etc. . . ')
        if main == 'add':
            addq = input('whatchu want?')
            quan = input('how many?')
            cart[addq] = quan
            print(f'you bought stuff!  here\'s where you\'re at: {cart}')
        elif main == 'quit':
            print(cart)
            break





    








































    

