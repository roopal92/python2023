class CustomSet:
    
    def __init__(self):
      self.val=[]    #instance variable or data attribute -> created when class in instantiated and contains values for each instance like s and c

    def add(self, a):
       if a not in self.val:
         self.val.append(a)

    def remove(self ,a):
       try:
         self.val.remove(a)
       except ValueError as e:
         print(str(a) + ' not found')   
    
    def __str__(self) -> str:
       result='' #else will show CTE inside for loop
       for e in self.val:
          result= result+str(e)+ ','          
       return result[:-1]  #added -1 just to remove the last ,
    
class Person:
   def __init__(self, name) -> None:  # called automatically at initialisation
      self.name=name    

   def __str__(self) -> str: #called automatically at the time of print
      return self.name

if __name__ == '__main__':
   s=CustomSet()  #user defined-> hashable
   s.add(12)
   s.add(3)
   s.remove(4)
   print(str(s)) #will automatically call __Str__

   c=CustomSet()
   c.add(4)
   c.add(9)
   print(c)  #will automatically call __Str__

   p=Person("Roopal")
   print(p)
   p1=Person("Rahul")
   plist=[p,p1]
   for person in plist:
      print(person)
   plist.sort() #TODO what param has to be passed
   for person in plist:
      print(person)