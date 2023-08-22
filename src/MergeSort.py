def merge(l1,l2):

   length=l2 if len(l1)>len(l2) else l1
   

def merge_sort(list):
   if len(list)==2:  #if list is len <2 elem return as is
      return list[:]
   else:
      mid =len(list)//2
      left=merge_sort(list[:mid])
      right=merge_sort(list=list[mid:len(list)])
      return merge(left,right)
  

if __name__ == '__main__':
   list= [12,43,2,5,3,21,87,34,65,6,1]
   print("sorted list",list, ":", merge_sort(list=list))
   