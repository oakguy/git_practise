#Write your function here
def reversed_list(lst1, lst2):
      #return True is lst1 is the same as lst2 reveresed
      #else return False
      #print(lst2 = sorted(lst2))
      if sorted(lst2) == lst1:
            return True
      else:
            return False
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))