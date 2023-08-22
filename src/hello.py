from typing import Callable, List, Tuple
from operator import add
import numpy as np
print("hello")


def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))


def square(x: int) -> int:
    '''
    >>> square(10)
    100
    '''
    return x*x


def doMath(n: int):
    return square(n)


def summation(n: int, term):
    total, k = 0, 1
    while (k <= n):
        total = total + term(k)
        k = k+1
    return total


def adder(n: int):
    def add(m):  # lexical scoping -> the inner functions have access to the names in the environment where they are defined
        return m+n
    return add


def microservice_parent(p1: str, p2: str, p3: str):
    def compute_secret(arg_from_service: str):  # Nested Def
        return hash((p1, p2, p3, arg_from_service))
    return compute_secret


def demo_closure(x: int) -> Callable[[int], Callable[[int], int]]:
    def add(f: int):  # nested def
        return x+f
    return add


def higherOrder(func, x):  # accept and return function
    return (func(func(x)))


def div(y):
    return (y+5) // 3
# y+5 divide by 3


def repeat(f, x):
    while (f(x) != x):
        x = f(x)
    return x

# decorator


def trace(f):
    def traced(x):
        print("callling", f, "on arg", x)
        return f(x)
    return traced


def compose(f, g):
    def h(x):
        return f(g(x))
    return h


def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


def power(x, n):
    """Return x * x * x * ... * x for x repeated n times."""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product


@trace  # decorator to print value
def curried_pow(x):
    def h(y):
        return power(x, y)
    return h


def iter(guess: float, a: float) -> float:
    relative_error: Callable[[Tuple[float, float]], float] = lambda pair: abs(
        pair[1] - pair[0])/float(pair[0])
    update: Callable[[float], float] = lambda x: (x+a/x)/2
    if (relative_error((a, guess**2)) < 1e-5):
        return guess
    return iter(update(guess), a)


def compose1(f, g):
    return lambda x: f(g(x))

# add :: Num a => a -> a -> a
# add :: Num a => (a, a) -> a

# add :: a -> a -> a
# add :: a -> (a -> a)


def curry_add(x: int):

    def inner(y: int):
        return x + y
    return inner

# compose :: (a -> b) -> (b -> c) -> (a -> c)


def compose(f: Callable[[int], float]) -> Callable[[int], int]:
    def inner(g: Callable[[float], int]) -> Callable[[int], int]:
        return lambda x: g(f(x))
    return inner


def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last = n // 10
        last = n % 10
        return sum_digits(all_but_last) + last


def iterator(s: list[int] | list[float], value: int | float):
    count, index = 0, 0
    while (index < len(s)):
        if s[index] == value:
            count = count+1
            index = index + 1
        index += 1
    return count


def search(f):
    x = 0
    while not f(x):
        x += 1
    return x


def inverse(f):
    return lambda x: search(lambda y: f(y) == x)


if __name__ == '__main__':
    print(a)
    print('square is ', square(2))
    print("summation of sq: ", summation(3, square))
    print(summation(2, pi_term))
    print("square of 3", doMath(3))
    print("Func as return value using local def to add:", adder(2)(3))
    def cube(x): return x*x*x  # also an expression: evaluates to function
    print('cube of 3 using lambda: ', cube(3))

    launch_service = microservice_parent("Abhijit", "C-46", "31")
    print(launch_service("BHHPG..."))
    print(launch_service("XXHDD..."))
    print((lambda *outer: lambda *pair: hash((*outer, *pair)))
          ("Abhijit", "C-46", "31")("BHHPG..."))

    print("Relative Error", iter(1, 9))
    a = demo_closure(2)
    print("add", a(3))
    print("higherOrder", higherOrder(square, 3))
    # ans is 2 not 3 bcz f(x) is called twice
    print("Rpeat div", repeat(div, 5))

    m = curry2(add)
    add_2 = m(3)
    print('Result of curry with 2 args: ', add_2(2))
    print('Calling directly curry with 2 args: ', curry2(add)(3)(2))
    print(curried_pow(2)(3))

    lambda_compose = compose1(lambda x: x * x, lambda y: y + 1)  # compose(f,g)
    result = lambda_compose(12)
    print(f"the result of passing just 1 arg is: {curry_add(1)}")
    z = curry_add(1)
    print(z(2))

    def c1(f, g): return lambda x: f(g(x))
    print("compooooosse", c1(square, square)(2))

    from operator import add
    print((lambda y: lambda x: x+y)(2)(1))  # compose
    print((lambda f: lambda y: lambda x: f(x, y))(add)(2)(3))
    print((lambda f: lambda y: lambda x: f(x, y))(lambda x, y: x*y)(2)(3))
    print(compose(lambda x: float(x))(lambda y: int(y)))
    print((compose(lambda x: float(x))(lambda y: int(y)))(5))
    print(compose(lambda x: x - np.mean(x))
          (lambda y: y/np.std(y))(np.array([1., 2, 3., 4.])))
    # add :: Num a => a -> a -> a
    # add = \y -> \x -> x + y
    print("Find occrence")
    print(iterator([1, 2, 3, 1, 3, 4, 5, 521, 13, 3, 1, 9], 1))

    odds = [1, 5, 7, 11]
    div25 = [xy for xy in odds if 25 % xy == 0]
    print(div25)

    # aggregation
    num_divisors = 8
    divisors = [i for i in range(2, num_divisors) if num_divisors % i == 0]
    print(f"divisors of 8 ={divisors}")

    # Using divisors, we can compute all perfect numbers from 1 to 1000 with another list comprehension. (1 is typically considered to be a perfect number as well, but it does not qualify under our definition of divisors.)
    perfect_num = [n for n in range(1, 1000) if sum(divisors) == n]
    print(f"perfect num {perfect_num}")

    # find sqrt
    sqrtNum = inverse(square)
    print(sqrtNum(256))

    import string
    print('a' in string.ascii_lowercase)

    s = "hello"
    print(s[0])
    print('h' in s)
    print(s[0:2])
    print(s[0:])
    print(s[:2])
    print(s[1::2])
