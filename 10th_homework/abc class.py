import abc


class Abstract_int_prime_check(abc.ABC):                    # 7
    
    @abc.abstractmethod
    def int_prime_check(number):
        if type(number) == int:
            for num in range(0, number):
                if number % num == 0:
                    continue
                else:
                    return False
                
            return True
        
class int_prime_check(Abstract_int_prime_check):
    
    def int_prime_check(number):
        if type(number) == int:
            for num in range(2, number):
                if number % num == 0:
                    return False
                else:
                    continue
                
            return True
        
print(int_prime_check.int_prime_check(17))