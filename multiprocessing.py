# https://towardsdatascience.com/a-hands-on-guide-to-multiprocessing-in-python-48b59bfcc89e

import time
import math
import multiprocessing

def is_prime(n):
# https://www.geeksforgeeks.org/analysis-different-methods-find-prime-number-python/
# If the integer is less than equal to 1, it returns False.
# If the number is equal to 2, it will return True.
# If the number is greater than 2 and divisible by 2, then it will return False.
# Now, we have checked all the even numbers. Now, look for the odd numbers.
# If the given number is divisible by any of the numbers from 3 to the square root of the number skipping all the even numbers, the function will return False
# Else it will return True
    if n <= 1:
        return 'not a prime number'
    if n == 2:
        return 'prime number'
    if n > 2 and n % 2 == 0:
        return 'not a prime number'
    
    max_div = math.floor(math.sqrt(n))

    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return 'not a prime number'
    return 'prime number'

def _func(i):
    time.sleep(1)
    print('{} is {} number'.format(i, is_prime(i)))


if __name__ == '__main__':
    starttime = time.time()

    # With Process: 1.4353456497192383 seconds
    processes = []
    for i in range(1, 20):
        p = multiprocessing.Process(target=_func, args=(i,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    print('Using Process: Time taken = {} seconds'.format(time.time() - starttime))

    # With Pool: 3.249145269393921 seconds  
    # pool = multiprocessing.Pool()
    # pool.map(_func, range(1,20))
    # pool.close()
    # print('Using Pool: Time taken = {} seconds'.format(time.time() - starttime))

    

# Without multiprocessing: 19.022353410720825 seconds
# starttime = time.time()
# for i in range(1, 20):
#     _func(i)
# print('No Multiprocessing: Time taken = {} seconds'.format(time.time() - starttime))
