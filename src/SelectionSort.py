
def selection_sort(list):

   for i in range(len(list)):
      small=list[i]
      elem=i
      for j in range(i,len(list)):
         if list[j]<small:
            small=list[j]
            elem=j
      list[elem]=list[i]
      list[i]=small
   return list
  

if __name__ == '__main__':
   list= [12,43,2,5,3,21,87,34,65,6,1]
   print("sorted list",list, ":", selection_sort(list=list))
   