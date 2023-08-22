def extreme_divisors(a:int, b:int):
    minV,maxV=0,0
    div:int=min(a,b)   #min is keyword 
    for i in range(2, div+1):
        if a%i==0 and b%i==0:
            if minV==0:
                minV=i
            else:
                maxV=i
    return minV, maxV

'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''
if __name__ == '__main__':
   '''String  , tuple(any type), range immutable'''

   #tuple
   t1=(1,"roo",3) 
   t2=(t1, 2)  
   print((t1+t2)[3])#third elem in list ->t1
   minv, maxv= extreme_divisors(24,8)   
   print("min n max value",minv, maxv)

   #range
   for i in range(10)[2:6]:
    print(i)         #2..5
   print(range(10)[2:6][2])    # get(0,1,2) 3rd no ->4
   print('========')
   for r in range(0,7,2):
      print(r)         # 0 2 4 6       <7
   
   '''Lists, dictionariese are mutable-> modified after creation
   sideeffect-> eg append ->mutates the existing list
   
   '''
   l1=[1,2,3]
   l2=[6,5,4]
   l3=l1+l2  #immutable
   print(l3)
   l1.extend(l2) #mutate add list
   print("Extended ",l1)
   l1.append(8)
   #l1.append(l2) #mutate add object
   print("Appended",l1)

   l1.insert(2,8) #insert at index
   print(l1)

   l2.sort
   print("sorted list", l2)

   # imp observation
   # test mutability-> 
   r1=[1,2,3]
   r2=[1,2,5,6]
   for e in r1:
      if e in r2:
         r1.remove(e)
   print(r1[0])
   print("Mutability  inconsistency ",r1)  # 2 should be removed but not removed bcz when internal iterator moves from r[0] to r[1] new list r=2,3 and r[1]=3 so 2 not processed 
      
   print([i*2 for i in r1 if i%2==0])  # remember to put in list
   print("get list of even nos in list",r2, ": ", list(e for e in r2 if e%2==0))

   #higher order functions
   
   for i in map(lambda x: x*x, [2,3,5]):
      print(i)

   for x in map(lambda x,y: x if x < y else y, [1,2,3], [2,3,4]):
      print(x, end=" ")
   print()

   s='my fav is - abcd '
   print(s.split(' '))
   print(s.count('abc'))
   print(s.find('ab')) #first occurence index
   print(s.index('a')) #not found raise exc

   print("dictionaries")
   dict={"jan":'1', "feb":'2',"mar":"3"}
   print(dict.values() if len(dict)!=0 else None)    #type dict_values
   print(list(dict.keys()))   #type convert dict.keys-> to list
   print(dict["jan"])
   print(dict.get("mar", None))
   print(dict.get("dec", None)) #none if absent
   for i in dict:
    print(dict[i], end =" ")


