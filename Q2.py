############################### Question 2 ####################################
#  Write a program that takes a tag from the user and prints for him
#  the evaluation of this mark according to the attached table

#  For example, if the user entered his mark 50, he would print an F

#  If he entered 80, he would print with-

#  If he entered 150, he prints an invalid mark

#  Invalid mark> 100 or negative

#  A + 97 - 100%
#  A 93-96%
#  A 90 - 92%
#  B + 87 - 89%
#  B 83 - 86%
#  B 80 - 82%
#  C + 77 - 79%
#  C 73-76%
#  C- 70 - 72%
#  D + 67 - 69%
#  D 63 - 66%
#  D- 60 - 62%   
#  F 0 - 59%
# ----------------------------------------------
# ####### By: Abdallah Ibrahim #######
# ----------------------------------------------
##############################################################################
import sys,os

while True:
   
   os.system("title Give Me Rating!")
   print("""
   ------------------------------------------------
   | Wlecome Back!                                 |
   | Give Me Your Mark, I'll told Your rate quickly|
   | Best Wishes!                                  |
   ------------------------------------------------
         """)
      
   try:
         
      insert_your_mark = float(input(" Enter Your mark(without '%' sign): "))


      if insert_your_mark < 100 and insert_your_mark >= 97 :
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: A+")
      elif insert_your_mark <= 96 and insert_your_mark >= 93:
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: A")
      elif insert_your_mark <= 92 and insert_your_mark >= 90:
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: A-")
      elif insert_your_mark <= 89 and insert_your_mark >= 87:
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: B+")
      elif insert_your_mark <= 86 and insert_your_mark >= 83:
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: B")
      elif insert_your_mark <= 82 and insert_your_mark >= 80:
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: B-")
      elif insert_your_mark <= 79 and insert_your_mark >= 77:
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: C+")
      elif insert_your_mark <= 76 and insert_your_mark >= 73:
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: C")
      elif insert_your_mark <= 72 and insert_your_mark >= 70:
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: C-")
      elif insert_your_mark <= 69 and insert_your_mark >= 67:
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: D+")
      elif insert_your_mark <= 66 and insert_your_mark >= 63:
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: D")
      elif insert_your_mark <= 62 and insert_your_mark >= 60:
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: D")
      elif insert_your_mark <= 59 and insert_your_mark >= 0:
         print(f" Your mark: {insert_your_mark}%")
         print(" Your Rating: F")
      else:
         print(" Invalid mark!")
      break
   except:
      if KeyboardInterrupt:
         sys.exit()
      else:      
         print("Please Enter a valid mark..\n")
         os.system("cls")
      