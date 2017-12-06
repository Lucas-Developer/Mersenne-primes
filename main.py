import primes
import time
import prime_list
import threading

THREAD_NUMBER = 50
lock = threading.Lock()
prime_array = []
threads = []

def checkPrime(exponent,factors):
    if primes.isPrimeLL(int(exponent),factors):
        with lock:
            prime_array.append(primes.mersennePrime(exponent))

def main():
    factors = prime_list.readPrimes()
    good_factors = prime_list.checkModulus(factors)
    for i in range(1,3500,THREAD_NUMBER):
        print(str(i))
        threads = []
        for j in range(THREAD_NUMBER):
            threads.append(threading.Thread(target = checkPrime, args = (i+j,good_factors)))
        for j in range(THREAD_NUMBER):
            threads[j].start()
        for j in range(THREAD_NUMBER):
            threads[j].join()
    for prime in prime_array:
        print(str(prime) + " is a Mersenne prime.\n")

start = time.clock()
main()
end = time.clock()
print("Time elapsed: " + str(end-start))
