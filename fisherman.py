print("Do you want to buy fish from the fisherman?")
print("Lets do it!")
#Ask the user for the weight pounds
weight_pounds =float(input("How many pounds of fish did you catch man?"))
#Convert to kilograms
weight_kms = weight_pounds * 0.4536
#Calculate the price of thr fish
price = weight_kms * 2
# Check price
if price > 8:
       print("Good job man!" , 
              weight_pounds , "The amount of pounds you gained is great." , 
             "Yor gift is a hook")
elif price == 2 :
       print("Not bad " , weight_pounds , "This is uor pounds" , "Keep working")
else :
       print("Sorry man,", weight_pounds,"Pounds not enough.", "You should be fired.","Try again.")
       #Try agian
       print("the price of your fish $",price)
       weight_pounds =float(input("How many pounds of fish did you catch man?"))
       weight_kms = weight_pounds * 0.4536
       price = weight_kms * 2
#The final price
       print("the price of your fish $",price)






