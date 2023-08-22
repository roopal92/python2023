def isbinary(n, length):
   result = ''
   while(n>0):
      result= str(n%2) + result
      n=n//2
   for i in range(length-len(result)):
      result = '0'+result
   return result

def powerset(list):
   power_set =[]
   for i in range(2**len(list) ):
      binary= isbinary(i, len(list))
      result=[]
      for j in range(len(list)):
         if binary[j] =='1':
            result.append(list[j])
      power_set.append(result)
   return power_set

if __name__ == '__main__':
   result= isbinary(21, 5)
   print(result)
   print(powerset(['3','4','5']))
