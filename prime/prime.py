def is_prime(num):
     if num == 2 or num == 3: 
         return True
     if num < 2 or not num % 2 : 
         return False 
     for i in range (3, int(num ** 0.5)+ 1, 2):
         if not num % i:
             return False
         return True
     
if __name__ == '__main__':
    primes = [str(i) for i in range(100) if is_prime(i) ]
    print('\n', ','.join(primes))