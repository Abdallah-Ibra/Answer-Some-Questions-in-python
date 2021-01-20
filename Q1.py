############################### Question 1 ####################################
# Write python code that takes three inputs from the user
# and prints its mean (sum / number of entries)
# ----------------------------------------------
# ####### By: Abdallah Ibrahim #######
# ----------------------------------------------
##############################################################################

import os,sys

while True:
   os.system("title Get Average Program")
   print("""
   ------------------------------------------------
   | Wlecome Back!                                |
   | This Program to get The Average from 3 inputs|
   | Best Wishes!                                 |
   ------------------------------------------------
         """)

   print("""
 1. Start to get Average!
 00. exit
      
 "Insert '1' to start the program, insert '00' to exit" 
      
   """)

   try:
         
      i = str(input(" "))
      print()


      if i == "1": 
                  
         n1 = float(input(" Enter The first number: "))
         n2 = float(input(" Enter The second number: "))
         n3 = float(input(" Enter The third number: "))
         
         sum = n1 + n2 + n3

         balaha  = sum/3

         print()
         print(" => Average: {:.2f}".format(balaha))
         print("===================================================")
            

      elif i == "00":
         print(" See You Again!")
         break
         # exit(0)
         

      else:
         raise Exception
   except:
      if KeyboardInterrupt:
         sys.exit()
      else:    
         print(" Please Enter The right Input!")
         os.system("cls")
