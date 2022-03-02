from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    # Optimal
    print(bin(x)) 
    x ^= x >> 32
    print(bin(x))
    x ^= x >> 16
    x ^= x >> 8
    print(x)
    x ^= x >> 4
    x ^= x >> 2
    print(x)
    x ^= x >> 1
    return x & 0x1


    # one optimization to brute force
    # result = 0
    # while x:
    #     result ^= 1
    #     x &= x-1 # Drops the lowest set bit of x
    # return result
    

    # Brute Force solution
    # one_bits = 0
    # while x:
    #     one_bits ^= x & 1
    #     x>>=1
    # return one_bits


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
