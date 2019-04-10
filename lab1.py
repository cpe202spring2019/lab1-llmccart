
def max_list_iter(int_list):  # must use iteration not recursion
   max=0
   if int_list is None:
      raise ValueError
   if len(int_list)==0:
       return None
   else:
      for i in range(len(int_list)):
         if int_list[i]>max:
            max=int_list[i]
   return max
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      return ValueError
   if len(int_list)==1:
      return int_list
   temp = reverse_rec(int_list[1:])
   return temp.append(int_list[0])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list is None:
      return ValueError
   mid = (low+high)//2
   for i in range(len(int_list)):
      if target>int_list[mid]:
         return bin_search(target, mid+1, high, int_list)
      elif target==int_list[mid]:
         return mid
      elif target<int_list[mid]:
         return bin_search(target, low, mid-1, int_list)

