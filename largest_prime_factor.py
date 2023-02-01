def find_prime(number):
    while number % 2 == 0:
        number = number //2
    prime_num_can1 = (number //2) + 2
    while prime_num_can1 > 2:
        if number % prime_num_can1 == 0 :
            if is_it_prime(prime_num_can1):
                return prime_num_can1
        prime_num_can1 -= 2

def is_it_prime(number):   
   for i in range(2,((number//2) + 1 )):
       if (number % i) == 0:
           return False
   else:
       return True


number = 78451

print(find_prime(number))
