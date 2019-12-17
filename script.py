#Write your function here
def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    new_lst = lst[0:index] #sliced here
    new_lst.append(lst[index]*2) #inserted new value
    print(lst[index+1:])
    new_lst = new_lst + lst[index+1:] #added the remainder of the list
    return new_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
