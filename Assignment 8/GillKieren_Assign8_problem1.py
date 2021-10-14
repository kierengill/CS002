#Kieren Singh Gill
#11/10/2020
#Python Fall 2020, Section 1
#GillKieren_Assign8_problem1.py


#create a list of product names
#create a list of product costs
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = ["0.99", "1.29", "1.49"]
product_quantity = ["10","5","20"]


#prompt user to search for a product or quit the program
product_search = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")

#create a while loop
#while product_search is not equal to 'q'
#the loop will run
while product_search != 'q':

    #search feature
    if product_search == 's':
        #prompt user to input a product name
        item = input("Enter a product name: ")
        #if user input is in the list of product names
        #let them know the price per unit and quantity
        if item in product_names:
            index = product_names.index(item)            
            print('We sell "'+item+'" at',product_costs[index],'per unit')
            print('We currently have',product_quantity[index],'in stock')
            print()
        #otherwise
        #let them know that we don't sell the item
        else:
            print('Sorry, we don\'t sell "'+item+'"')
            print()

    #list feature
    elif product_search == 'l':
        #print the heading of the list table
        #the headings are left and right justified
        print("Product".ljust(15),"Price".ljust(6), "Quantity")
        #create a for loop
        #the loop will iterate across the range of the length of the list
            #so it iterates throughout the entire list
        for index in range(len(product_names)):
            #get the product name, cost and quantity for the same index number in each respective list
            product = product_names[index]
            cost = product_costs[index]
            quantity = product_quantity[index]
            #print them out in a line, left and right justify accordingly
            print(product.ljust(15), cost.ljust(6), quantity.rjust(8))
        print()

    #add product feature
    elif product_search == 'a':
        #prompt user to enter a new product name
        new_product = input("Enter a new product name: ")

        #as long as the user enters a name that already exists in the product_names list
        #reprompt user
        while new_product in product_names:
            print("Sorry, we already sell that product. Try again.")
            new_product = input("Enter a new product name: ")
        #prompt user to enter a new product cost
        new_product_cost = input("Enter a product cost: ")
        #as long the new cost is not positive
        #reprompt user
        while float(new_product_cost) <= 0:
            print("Invalid cost. Try again.")
            new_product_cost = input("Enter a product cost: ")
        #prompt user to enter a new quantity
        new_product_quantity = input("How many of these products do we have? ")
        #as long as the new quantity isn't numeric
        #reprompt user
        while not new_product_quantity.isnumeric():
            print("Invalid quantity. Try again.")
            new_product_quantity = input("How many of these products do we have? ")
        #as long as the new quantity isn't positive
        #reprompt user
        while int(new_product_quantity) <= 0:
            print("Invalid quantity. Try again.")
            new_product_quantity = input("How many of these products do we have? ")
            while not new_product_quantity.isnumeric():
                print("Invalid quantity. Try again.")
                new_product_quantity = input("How many of these products do we have? ")

        #append the new product name, new cost, and new quantity to their respective lists
        #let user know a new product is added
        product_names.append(new_product)
        product_costs.append('%.2f'%(float(new_product_cost)))
        product_quantity.append(new_product_quantity)
        print("Product added!")
        print()


    #remove product feature
    elif product_search == 'r':
        #prompt user to enter product to remove
        remove_product = input("Enter a product name: ")

        #if user input is in the list "product_names"
        #find the index of the element in the list
        #remove the product from the "product_names" list
        #remove the respective cost and quantity of the product by using the product's index
        #let user know product is removed
        if remove_product in product_names:
            index=product_names.index(remove_product)
            product_names.remove(remove_product)
            product_costs.remove(product_costs[index])
            product_quantity.remove(product_quantity[index])
            print("Product removed!")
            print()
        #if user input isn't in the list of product names
        #let them know
        else:
            print("Product doesn't exist. Can't remove.")
            print()


    #update product feature
    elif product_search == 'u':
        #prompt user to enter a product name
        update = input("Enter a product name: ")

        #if input is in the list of product names
        if update in product_names:
            #find the index of the element in the list
            index = product_names.index(update)
            #ask user what they would like to update
            what_to_update = input("What would you like to update? \n(n)ame, (c)ost or (q)uantity: ")
            #if the user enters an invalid option
            #let them know
            #reprompt them
            while what_to_update not in ['n','c','q']:
                print("Invalid option")
                what_to_update = input("What would you like to update? \n(n)ame, (c)ost or (q)uantity: ")
            #if user enters 'n'
            #prompt user to enter a new name
            #if name is a duplicate, let user know and reprompt user
            #update the product name in the list using its element index
            #let user know that product name has been updated
            if what_to_update == 'n':
                update_product = input("Enter a new name: ")
                while update_product in product_names:
                    print("Duplicate name!")
                    update_product = input("Enter a new product name: ")

                product_names[index] = update_product
                print("Product name has been updated")
            #if user enters 'c'
            #prompt user to enter a new cost
            #as long as cost isn't positive, repropmt user
            #update the product cost in the list using its element index
            #let user know that product cost has been updated
            elif what_to_update == 'c':
                update_cost = input("Enter a new cost: ")
                while float(update_cost) <= 0:
                    print("Invalid cost!")
                    update_cost = input("Enter a new cost: ")

                product_costs[index] = '%.2f'%(float(update_cost))
                print("Product cost has been updated")                
            #if user enters 'q'
            #prompt user to enter a new quantity
            #as long as quantity isn't positive or numeric, repropmt user
            #update the product quantity in the list using its element index
            #let user know that product quantity has been updated
            elif what_to_update == 'q':
                update_quantity = input("Enter a new quantity: ")
                while not update_quantity.isnumeric():
                    print("Invalid quantity!")
                    update_quantity = input("How many of these products do we have? ")            
                while int(update_quantity) <= 0:
                    print("Invalid quantity!")
                    update_quantity = input("How many of these products do we have? ")
                    while not update_quantity.isnumeric():
                        print("Invalid quantity!")
                        update_quantity = input("How many of these products do we have? ")
        
                product_quantity[index] = update_quantity
                print("Product quantity has been updated")          
            
            print()
        #if the input isn't in the list of product names
        #let user know
        else:
            print("Product doesn't exist. Can't update.")
            print()

    #report feature
    elif product_search == 'e':
        #find the most expensive cost in the product cost list using the max function
            #values are in string, but the max function will still yield a result
            #max function will sort using the string character's ascii values
        #find the cheapest cost in the cost list using the min function
            #values are in string but the min function will still give a result
            #it will sort using ascii values
        #find the most expensive and cheapest products
        #by using the index of the most expensive and cheapest cost
        expensive_cost = max(product_costs)
        cheapest_cost = min(product_costs)
        expensive_index = product_costs.index(expensive_cost)
        cheapest_index = product_costs.index(cheapest_cost)
        expensive_product = product_names[expensive_index]
        cheapest_product = product_names[cheapest_index]
        #create a counter for the total
        total=0
        #create a for loop
        #for loop will iterate across the entire list of product costs
        #for each iteration, multiply the product cost with the quantity of the product
        #and add the subtotal to the total counter
        for i in range(len(product_costs)):
            subtotal = float(product_costs[i])*int(product_quantity[i])
            total += subtotal
        #let user know the most expensive product, cheapest product, and the total value of all products
        print("Most expensive product:".ljust(30), expensive_cost,"("+expensive_product+")")
        print("Least expensive product:".ljust(30), cheapest_cost,"("+cheapest_product+")")
        print("Total value of all products:".ljust(30), '%.2f'%total)
        print()


    #if the user enters an invalid option
    #let them know and reprompt them
    else:
        print("Invalid option, try again")
        print()

    product_search = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")


#if user quits enters 'q', the loop will end
#when loop ends, print "See you soon!"
print("See you soon!")
