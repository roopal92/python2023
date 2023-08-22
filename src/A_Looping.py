name='Roopal'
def print_largest_odd(*args):
    nums = [int(x) for x in args]
    
    largest=0
    for num in nums:
        if(num%2!=0):
            largest=num
    print(largest if largest!=0 else 0)

def is_palind(s):
    answer=False
    #for keeping global count -optinal
    #global rec_times
    #rec_times = rec_times+1
    print(s) # at last will be blank
    if(len(s)<=1):
        return True
    else:
        answer= s[0]==s[-1] and is_palind(s[1:-1]) # compare first last and recurse for the rest by excluding first n last
        return answer   
    
if __name__ == '__main__':
    val=False
    print(type(val))  #get type
    print(isinstance(val,bool))  #check type

    print('abc'[0:len('abc')])
    print(3*'a')
    #range or dirct call 
    print('range(start:0,end,step:1) 1/2 arg same if start from 0')
    for i in range(0,3): 
        print(i)

    print('range 3 arg')
    for i in range(5,40,10):
        print(i)
    
    print('range with string')
    total=0
    for i in '123556':
        total = total +int(i)
        print('total',total)
    
    print(abs(-12321.12321))
    
    #recursion
    global rec_times 
    rec_times = 0
    print(is_palind("doggod"))
    print("Recursion total", rec_times)

    input_list = []
    for elem in range(int(input("Enter range: "))):
        arg = input(f"Enter {elem} arg: ")
        input_list.append(int(arg))
    print_largest_odd(*input_list)


