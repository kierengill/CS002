budget = int(input("Enter budget for your party: "))
cost_slice = float(input("Cost per slice of pizza: "))
cost_pie = float(input("Cost per whole pizza pie (8 slices): "))
guests = int(input("How many people will be attending your party? "))

s=0
for x in range(1,guests + 1):
        y1=int(input("Enter number of slices for person #"+str(x)+": "))
        while y1 < 1:
                print("Not a valid entry, try again!")
                print()
                y1=int(input("Enter number of slices for person #"+str(x)+": "))
        
        s+=y1

leftover= budget - (((s//8)*cost_pie)+((s-((s//8)*8))*cost_slice))
positive_leftover=abs(leftover)


if leftover < 0:
        print("Your order cannot be completed.")
        print("You would need to purchase",s//8,"pies and",s-((s//8)*8),"slices")
        print("This would put you over budget by",'{0:.2f}'.format(positive_leftover))

else:
        print("You should purchase",s//8,"pies and",s-((s//8)*8),"slices")
        print("Your total cost will be:",'{0:.2f}'.format(((s//8)*cost_pie)+((s-((s//8)*8))*cost_slice)))


        if leftover > 0:
                print("You will still have",'{0:.2f}'.format(leftover),"left after your order.")
        elif leftover == 0:
                print("You will have no money left after your order.")
