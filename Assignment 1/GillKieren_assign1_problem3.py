#Kieren Singh Gill
#09/14/2020
#Python Fall 2020, Section 1
#GillKieren_assign1_problem3.py

#use variables to store mathematical expressions for converting units
ml = 250
tsp = ml / (1/0.202884)
tbsp = tsp / 3
cup = tbsp / 16
pint = cup / 2
quart = pint / 2
gallon = quart / 4
floz = ml / 29.5735

#add spacing behind the headings so that the values are aligned
#assign the formatted headings to variables
heading1 = format("ml:", "<16")
heading2 = format("tsp", "<16")
heading3 = format("tbsp:", "<16")
heading4 = format("cup(s):", "<16")
heading5 = format("pint(s):", "<16")
heading6 = format("quart(s):", "<16")
heading7 = format("gallon(s):", "<16")
heading8 = format("fl oz:", "<16")


#print the title, headings, and different conversions
print ("--------------------------------------------------------------")
print ("		mL to US Fluid Volume Units")
print ("--------------------------------------------------------------")
print ("        "+ heading1,ml)
print ("        "+ heading2,tsp)
print ("        "+ heading3,tbsp)
print ("        "+ heading4,cup)
print ("        "+ heading5,pint)
print ("        "+ heading6,quart)
print ("        "+ heading7,gallon)
print ("        "+ heading8,floz)
print ("--------------------------------------------------------------")
