
from sequences_and_series import *


def main():

    my_data = [45, 65, 76, 43, 45, 67, 89, 32, 65, 23]
    my_data.sort()
    print("sorted:", my_data)
    print("n:", len(my_data))

    print("range:", my_range(my_data))
    print("sum:", my_sum(my_data))

    print("mean:", mean(my_data))
    print("median:", median(my_data))
    print("mode(s):", mode(my_data))

    print("---------------------------")

    print("arithmetic:", list(arithmetic(10, 5, 3)))
    print("geometric:", list(geometric(10, 2, 2)))

    def foo(x):
        return (-1)**x*x
    print("sequence:", list(sequence(10, 1, foo)))

    print("---------------------------")

    x = 29
    if(prime(x)):
        print("prime: x is prime")

    print("primes:", list(primes(10)))
    print("factors:", factorize(36))

    print("---------------------------")

    print("fibs:", list(fibs(10)))


if __name__ == '__main__':
    main()
