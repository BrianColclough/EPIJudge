from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    # Extract the i-th and j-th bits, and see if they differ
    if (x>>i) & 1 != (x>>j)&1: 
        # i-th and j-th bits differ. We will swap them by flipping their values.
        #select the bits to flip with bit_mask. Since x^1 = 0 whtn x = 1 and 1 when x = 0
        # we can perform the flip XOR
        bit_mask = (1<<i) | (1<<j) #this combines the two binarys with 1's in the
        # position of both i and j and zeros everywhere else
        x ^= bit_mask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
