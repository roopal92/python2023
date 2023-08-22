
def isbinary(list, search, low, high):
   if(low>high or low==high):
      return False
   mid=(low+high) //2
   if search == list[mid]:
      return True
   if search< list[mid]:
      return isbinary(list,  search, low,mid-1)
   else:
      return isbinary(list, search, mid+1,high)
  

if __name__ == '__main__':
   list= [2,3,4,6,7,8]
   print("element found",isbinary(list, search=3, low=0, high=len(list)))
   print("element found",isbinary(list, search=8, low=0, high=len(list)))
   print("element found",isbinary(list, search=5, low=0, high=len(list)))
   print("element found",isbinary(list, search=11, low=0, high=len(list)))   
   print("element found",isbinary(list, search=1, low=0, high=len(list)))
   