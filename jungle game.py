#The jungle game
#Valid animals = elephant - lion - dog - cat - mouse
# > more powerful - elephant >  lion > dog > cat > mouse but mouse > elephant
p1 = input (" please select your animal as player 1 : ")
p2 = input (" please select your animal as player 2 : ")
p3 = input (" please select your animal as player 3 : ")
# player 1 winner =
#playe 1 select elephant
if p1 == "elephant" and p2 == "lion" and p3 == "lion" :
 print("player 1 win")
elif p1 == "elephant" and p2 == "lion" and p3 == "dog" :
 print("player 1 win")
elif p1 == "elephant" and p2 == "lion" and p3 == "cat" :
 print("player 1 win")
elif p1 == "elephant" and p2 == "dog" and p3 == "lion" :
 print("player 1 win")
elif p1 == "elephant" and p2 == "dog" and p3 == "dog" :
 print("player 1 win")
elif p1 == "elephant" and p2 == "cat" and p3 == "lion" :
  print("player 1 win")
elif p1 == "elephant" and p2 == "cat" and p3 == "dog" :
   print("player 1 win")
elif p1 == "elephant" and p2 == "cat" and p3 == "cat" :
    print("player 1 win")

elif p1 == "lion" and p2 == "dog" and p3 == "dog" :
     print("player 1 win")
elif p1 == "lion" and p2 == "dog" and p3 == "cat" :
      print("player 1 win")
elif p1 == "lion" and p2 == "dog" and p3 == "mouse" :
      print("player 1 win")
elif p1 == "lion" and p2 == "cat" and p3 == "dog" :
      print("player 1 win")
elif p1 == "lion" and p2 == "cat" and p3 == "cat" :
      print("player 1 win")
elif p1 == "lion" and p2 == "cat" and p3 == "mouse" :
      print("player 1 win")
elif p1 == "lion" and p2 == "mouse" and p3 == "mouse" :
      print("player 1 win")
                  
elif p1 == "dog" and p2 == "cat" and p3 == "cat" :
      print("player 1 win")
elif p1 == "dog" and p2 == "cat" and p3 == "mouse" :
      print("player 1 win")                      
elif p1 == "dog" and p2 == "mouse" and p3 == "cat" :
      print("player 1 win")
elif p1 == "dog" and p2 == "mouse" and p3 == "mouse" :
      print("player 1 win")

elif p1 == "lion" and p2 == "mouse" and p3 == "elephant" :
    print ( "Player 1 win")
elif p1 == "dog" and p2 == "mouse" and p3 == "elephant" :
    print ( "Player 1 win")
elif p1 == "cat" and p2 == "mouse" and p3 == "elephant" :
    print ( "Player 1 win")
elif p1 == "lion" and p2 == "elephant" and p3 == "mouse" :
    print ( "Player 1 win")
elif p1 == "lion" and p2 == "mouse" and p3 == "elephant" :
    print ( "Player 1 win")
elif p1 == "dog" and p2 == "elephant" and p3 == "mouse" :
    print ( "Player 1 win")
elif p1 == "cat" and p2 == "elephant" and p3 == "mouse" :
    print ( "Player 1 win")
# player 2 win situations =
if p2 == "elephant" and p1 == "lion" and p3 == "lion" :
    print ( "Player 2 win")
elif p2 ==  "elephant" and p1 == "lion" and p3 == "dog" :
    print ( "Player 2 won ! ")
elif p2 ==  "elephant" and p1 == "lion" and p3 == "cat" :
    print ( "Player 2 win")
elif p2 ==  "elephant" and p1 == "dog" and p3 == "lion" :
    print ( "Player 2 win")
elif p2 ==  "elephant" and p1 == "dog" and p3 == "dog" :
    print ( "Player 2 win")
elif p2 ==  "elephant" and p1 == "dog" and p3 == "cat" :
    print ( "Player 2 win")
elif p2 ==  "elephant" and p1 == "cat" and p3 == "lion" :
    print ( "Player  win")
elif p2 ==  "elephant" and p1 == "cat" and p3 == "dog" :
    print ( "Player 1 win")
elif p2 ==  "elephant" and p1 == "cat" and p3 == "cat" :
    print ( "Player 2 win")
elif p2 ==  "lion" and p1 == "dog" and p3 == "dog" :
    print ( "Player 2 win")
elif p2 ==  "lion" and p1 == "dog" and p3 == "cat" :
    print ( "Player 2 win")
elif p2 ==  "lion" and p1 == "dog" and p3 == "mouse" :
    print ( "Player 2 win")
elif p2 ==  "lion" and p1 == "cat" and p3 == "dog" :
    print ( "Player 2 win")
elif p2 ==  "lion" and p1 == "cat" and p3 == "cat" :
    print ( "Player 2 win")
elif p2 ==  "lion" and p1 == "cat" and p3 == "mouse" :
    print ( "Player 2 win")
elif p2 ==  "lion" and p1 == "mouse" and p3 == "dog" :
    print ( "Player 2 win")
elif p2 ==  "lion" and p1 == "mouse" and p3 == "cat" :
    print ( "Player 2 win")
elif p2 ==  "lion" and p1 == "mouse" and p3 == "mouse" :
    print ( "Player 2 win")
elif p2 ==  "dog" and p1== "cat" and p3 == "cat" :
    print ( "Player 2 win")
elif p2 ==  "dog" and p1 == "cat" and p3 == "mouse" :
    print ( "Player 2 win")
elif p2 ==  "dog" and p1 == "mouse" and p3 == "cat" :
    print ( "Player 2 win")
elif p2 ==  "dog" and p1 == "mouse" and p3 == "mouse" :
    print ( "Player 2 win")
elif p2 == "lion" and p1 == "mouse" and p3 == "elephant" :
    print ( "Player 2 win")
elif p2 == "dog" and p1 == "mouse" and p3 == "elephant" :
    print ( "Player 2 win")
elif p2 == "cat" and p1 == "mouse" and p3 == "elephant" :
    print ( "Player 2 win")
elif p2 == "lion" and p1 == "elephant" and p3 == "mouse" :
    print ( "Player 2 win")
elif p2 == "lion" and p1 == "mouse" and p3 == "elephant" :
    print ( "Player 2 win")
elif p2 == "dog" and p1 == "elephant" and p3 == "mouse" :
    print ( "Player 2 win")
elif p2 == "cat" and p1 == "elephant" and p3 == "mouse" :
    print ( "Player 2 win")
# player 3 win situations =
if p3 == "elephant" and p2 == "lion" and p1 == "lion" :
    print ( "Player 3 win")
elif p3 ==  "elephant" and p2 == "lion" and p1 == "dog" :
    print ( "Player 3 win")
elif p3 ==  "elephant" and p2 == "lion" and p1 == "cat" :
    print ( "Player 3 win")
elif p3 ==  "elephant" and p2 == "dog" and p1 == "lion" :
    print ( "Player 3 win")
elif p3 ==  "elephant" and p2 == "dog" and p1 == "dog" :
    print ( "Player 3 win")
elif p3 ==  "elephant" and p2 == "dog" and p1 == "cat" :
    print ( "Player 3 win")
elif p3 ==  "elephant" and p2 == "cat" and p1 == "lion" :
    print ( "Player 3 win")
elif p3 ==  "elephant" and p2 == "cat" and p1 == "dog" :
    print ( "Player 3 win")
elif p3 ==  "elephant" and p2 == "cat" and p1 == "cat" :
    print ( "Player 3 win")
elif p3 ==  "lion" and p2 == "dog" and p1 == "dog" :
    print ( "Player 3 win")
elif p3 ==  "lion" and p2 == "dog" and p1 == "cat" :
    print ( "Player 3 win")
elif p3 ==  "lion" and p2 == "dog" and p1 == "mouse" :
    print ( "Player 3 win")
elif p3 ==  "lion" and p2 == "cat" and p1 == "dog" :
    print ( "Player 3 win")
elif p3 ==  "lion" and p2 == "cat" and p1 == "cat" :
    print ( "Player 3 win")
elif p3 ==  "lion" and p2 == "cat" and p1 == "mouse" :
    print ( "Player 3 win")
elif p3 ==  "lion" and p2 == "mouse" and p1 == "dog" :
    print ( "Player 3 win")
elif p3 ==  "lion" and p2 == "mouse" and p1 == "cat" :
    print ( "Player 3 win")
elif p3 ==  "lion" and p2 == "mouse" and p1 == "mouse" :
    print ( "Player 3 win")
elif p3 ==  "dog" and p2 == "cat" and p3 == "cat" :
    print ( "Player 3 win")
elif p3 ==  "dog" and p2 == "cat" and p1 == "mouse" :
    print ( "Player 3 win")
elif p3 ==  "dog" and p2 == "mouse" and p1 == "cat" :
    print ( "Player 3 win")
elif p3 ==  "dog" and p2 == "mouse" and p1 == "mouse" :
    print ( "Player 3 win")
elif p3 == "lion" and p2 == "mouse" and p1 == "elephant" :
    print ( "Player 3 win")
elif p3 == "dog" and p2 == "mouse" and p1 == "elephant" :
    print ( "Player 3 win")
elif p3 == "cat" and p2 == "mouse" and p1 == "elephant" :
    print ( "Player 3 win")
elif p3 == "lion" and p2 == "elephant" and p1 == "mouse" :
    print ( "Player 3 win")
elif p3 == "lion" and p2 == "mouse" and p1 == "elephant" :
    print ( "Player 3 win")
elif p3 == "dog" and p2 == "elephant" and p1 == "mouse" :
    print ( "Player 3 win")
elif p3 == "cat" and p2 == "elephant" and p1 == "mouse" :
    print ( "Player 3 win")
# mouse win :
elif p1 == "mouse" and p2 == "elephant" and p3 == "elephant" :
    print (" Player 1 win")
elif p2 == "mouse" and p1 == "elephant" and p3 == "elephant" :
    print (" Player 2 win")
elif p3 == "mouse" and p2 == "elephant" and p1 == "elephant" :
    print (" Player 3 win")
# Draw :
elif p1 == "elephant" and p2 == "elephant" and p3 == "elephant" :
    print ("equal")
elif p1 == "lion" and p2 == "lion" and p3 == "lion" :
     print ("equal")
elif p1 == "dog" and p2 == "dog" and p3 == "dog" :
    print ("equal")
elif p1 == "dog" and p2 == "dog" and p3 == "dog" :
    print ("equal")
elif p1 == "cat" and p2 == "cat" and p3 == "cat" :
    print ("equal")
elif p1 == "mouse" and p2 == "mouse" and p3 == "mouse" :
    print ("equal")
# Player 1 and 2 equal and player 3 remove :
elif p1 == "elephant" and p2 == "elephant" and p3 == "lion" :
    print ("player 1 and 2 draw and player 3 elimination")
elif p1 == "elephant" and p2 == "elephant" and p3 == "dog" :
    print ("player 1 and 2 equal and player 3 remove")
elif p1 == "elephant" and p2 == "elephant" and p3 == "cat" :
    print ("player 1 and 2 equal and player 3 remove")
elif p1 == "lion" and p2 == "lion" and p3 == "dog" :
    print ("player 1 and 2 equal and player 3 remove")
elif p1 == "lion" and p2 == "lion" and p3 == "cat" :
    print ("player 1 and 2 equal and player 3 remove")
elif p1 == "lion" and p2 == "lion" and p3 == "mouse" :
    print ("player 1 and 2 equal and player 3 remove")
elif p1 == "dog" and p2 == "dog" and p3 == "cat" :
    print ("player 1 and 2 equal and player 3 remove")
elif p1 == "dog" and p2 == "dog" and p3 == "mouse" :
    print ("player 1 and 2 equal and player 3 remove")
elif p1 == "cat" and p2 == "cat" and p3 == "mouse" :
    print ("player 1 and 2 equal and player 3 remove")
elif p1 == "cat" and p2 == "cat" and p3 == "mouse" :
    print ("player 1 and 2 equal and player 3 remove")
# player 1 and 3 equal and player 2 remove :
elif p1 == "elephant" and p3 == "elephant" and p2 == "lion" :
    print ("player 1 and 3 equal and player 2 remove")
elif p1 == "elephant" and p3 == "elephant" and p2 == "dog" :
    print ("player 1 and 3 equal and player 2 remove")
elif p1 == "elephant" and p3 == "elephant" and p2 == "cat" :
    print ("player 1 and 3 equal and player 2 remove")
elif p1 == "lion" and p3 == "lion" and p2 == "dog" :
    print ("player 1 and 3 equal and player 2 remove")
elif p1 == "lion" and p3 == "lion" and p2 == "cat" :
    print ("player 1 and 3 equal and player 2 remove")
elif p1 == "lion" and p3 == "lion" and p2 == "mouse" :
    print ("player 1 and 3 equal and player 2 remove")
elif p1 == "dog" and p3 == "dog" and p2 == "cat" :
    print ("player 1 and 3 equal and player 2 remove")
elif p1 == "dog" and p3 == "dog" and p2 == "mouse" :
    print ("player 1 and 3 equal and player 2 remove")
elif p1 == "cat" and p3 == "cat" and p2 == "mouse" :
    print ("player 1 and 3 equal and player 2 remove")
# player 2 and 3 equal and player 3 remove :
elif p2 == "elephant" and p3 == "elephant" and p1 == "lion" :
    print ("player 2 and 3 equal and player 1 remove")
elif p2 == "elephant" and p3 == "elephant" and p1 == "dog" :
    print ("player 2 and 3 equal and player 1 remove")
elif p2 == "elephant" and p3 == "elephant" and p1 == "cat" :
    print ("player 2 and 3 equal and player 1 remove")
elif p2 == "lion" and p3 == "lion" and p1 == "dog" :
    print ("player 2 and 3 equal and player 1 remove")
elif p2 == "lion" and p3 == "lion" and p1 == "cat" :
    print ("player 2 and 3 equal and player 1 remove")
elif p2 == "lion" and p3 == "lion" and p1 == "mouse" :
    print ("player 2 and 3 equal and player 1 remove")
elif p2 == "dog" and p3 == "dog" and p1 == "cat" :
     print ("player 2 and 3 equal and player 1 remove")
elif p2 == "dog" and p3 == "dog" and p1 == "mouse" :
    print ("player 2 and 3 equal and player 1 remove")
elif p2 == "cat" and p3 == "cat" and p1 == "mouse" :
    print ("player 2 and 3 equal and player 1 remove")
else :
    print ("invalid animal")
# Finaly finish...
            









 


