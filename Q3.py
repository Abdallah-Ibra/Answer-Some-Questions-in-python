############################# Question 3 ##################################
#  Write a function that takes a set of values ​​into a list (array) and returns the largest value in it

#  Write a function that takes a set of values ​​into a list (array) and returns its smallest value

#  Write a function that takes a set of values ​​in a list (array) and returns the sum of the values ​​in it

#  Write a function that takes a set of values ​​in (an array) and returns the median of values ​​in it

#  Then write another function that calls the last function and increase the mean by 10%

#  Then write another function that recalls all the functions above
# ----------------------------------------------
# ####### By: Abdallah Ibrahim #######
# ---------------------------------------------- 
##################################################################################
import os,sys
from functools import reduce


os.system("title No Cover Name!")
print("""
   -----------------------------------------------
   | Wlecome Back!                                 |
   |                                               |
   | Insert Element as much as You can,and I'll:   |
   |                                               |
   | - Give You The Largest Value from list.       |
   | - Give You The Smallest Value from list.      |
   | - Give You The Sum of Values from list.       |
   | - Give You The Average of the list.           |
   | - Give You The Average + '10%' of the list.   |
   |                                               |
   | Best Wishes!                                  |
   -----------------------------------------------
      """)

try:
      
   v = int(input("\n- Enter number of elements in list (The length of list): "))
   l = []

   for i in range(v):
      x = input(f"- Enter the element number {i+1} : ")
      l.append(float(x))

   print("\n- The Elements You entered =" ,l)


   def largest_value():
      """
      This Function for getting the largest value  
      """
      # print("=> The Largest Value: ",max(l))
      mx = reduce((lambda x,y: x if x>y else y),l)
      print("=> The Largest Value: ",int(mx))

   def smallest_value():
      """
      This Function for getting the smallest value
      """
      # print("=> The Smallest Value:",min(l))
      mn = reduce((lambda x,y: x if x<y else y),l)
      print("=> The Smallest Value:",int(mn))

   def sum_of_values():
      """
      This Function for getting the sum of elements into list
      """
      # print("=> Sum of elements in given list is: ",sum(l))
      sm = reduce((lambda x,y: x+y))
      print("=> Sum of elements in given list is: ",sm)
      

   def average():
      """
      This Function to get average of list
      """
      # get_avrg = sum(l)/v
      # print("=> Average: {:.2f}".format(get_avrg))
      av = reduce((lambda x,y: (x+y)/len(l)),l)
      print("=> Average: {:.2f}".format(av))
      

   def average_plus_ten_percent():
      """
      This Function to increase 10% to average function
      """
      # get_avrg = (sum(l)/v) * 0.1
      # print("=> Average with '10%' increament: {:.2f}".format(get_avrg))
      av = reduce((lambda x,y: (x+y)/len(l)),l)
      i_av = av * 0.1
      print("=> Average with '10%' increament: {:.2f}".format(i_av))


   def print_all_details():
      """
      This Function to print all fuctions before ^_^
      """
      print("\n====================================================\n")   
      largest_value()
      smallest_value()
      average()
      average_plus_ten_percent()
      products = reduce((lambda x,y: x*y),l)
      print("=> The Product of All Values: {:.2f}".format(products))   
      print("\n====================================================\n")   


   print_all_details()

except:
   if ValueError:
      "please Enter The Correct Value!"
   elif KeyboardInterrupt:  
      sys.exit()
   else:
      raise Exception