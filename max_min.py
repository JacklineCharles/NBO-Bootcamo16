def find_max_min(num):
  #function to return max and min numbers in a list of numbers num
  if min(num)!=max(num):
    L_list=[]
    L_list.append(min(num))
    L_list.append(max(num))
    return L_list
  else:
    L_list=[]
    L_list.append(len(num))
    return L_list
print(find_max_min([2,3,4,5]))