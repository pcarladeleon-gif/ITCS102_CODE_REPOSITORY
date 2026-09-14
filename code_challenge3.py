#Global Freight Calculator

Name = input("Please Input Your Name:  " )
print("De Leon")

item_type = input("What is the type of items:  "  )
print("Special Halo-Halo ,Pansit Bihon Noodles ,Plain Rice  ")

fragile = bool(input("Is it fragile? True or False?  "  ))
print("True")

weight = float(input("How heavy is it?  "  ))
print("47")

distance = float(input("How far do it need to travel?  "  ))
print("145")

express = bool(input("It is rushed? True or False  "  ))
express = eval(input("It is rushed? True or False  "  ))
print("False")

international = bool(input("Is it international? True or False?  "  ))
international = eval(input("Is it international? True or False?  "  ))p
print("True")


base_cost = (weight * 2.50) + (distance * 0.15)


#Free Shipping

if weight <= 2 and distance <= 100 and express == False and international == False:
	print("Free Shipping  ")
	output = 0

#International Express

elif express == True and international == True:
	print("express and international is applied")
	output = (base_cost * 1.40) + 50

#Express of Heavy International

elif express == True or international == True and weight >= 20 and weight <=29.9:
	print("Heavy and Express/International applied")
	output = (base_cost * 1.20) + 25

#Oversized
elif weight >= 30 or distance > 1000:
	print("Oversized package is applied")
	output = base_cost + 30

else:
	print( " base_cost ")
	output = base_cost

print("The total amount due is", output)


# Typing false turns it into true, but pressing enter changes it back to false.