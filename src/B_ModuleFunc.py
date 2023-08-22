import A_Looping
from NumberToWords import convert_to_words,name

if __name__ == '__main__':
    #import module
    print(A_Looping.is_palind("dood"))
    print(A_Looping.name)
    print(convert_to_words(301))
    print(name) #not good practice to import like this 
    name="Roopal"
    print(name)   #overshadow