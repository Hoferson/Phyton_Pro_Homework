def gen(func, start, stop):                     # 1
    num = start
    while num <= stop:
        temp = yield func(num)
        if temp is not None:
            break
        num += 1

    
def func(num):
    return num * 2

print(list(gen(func, 1, 10)))


def fibo():                                      # 2
    cache = [0, 1]

    def fibonacci(n):
        if len(cache) >= n:
            return cache[n-1]
        
        while len(cache)<n:
            temp = cache[-1] + cache[-2]
            cache.append(temp)

        return temp

    return fibonacci

x = fibo()
print(x(1))
print(x(2))
print(x(3))
print(x(4))
print(x(5))
print(x(6))
print(x(7))
print(x(8))

def function(func, items):                      # 3
    return sum(list(map(func, items)))
items = [1,2,3,4,5]
print(function(func, items))