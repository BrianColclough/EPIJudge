from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    mask_size = 16
    bit_mask = 0xFFFF
    return(PRECOMPUTED_REVERSE[x & bit_mask] << (3*mask_size)
          | PRECOMPUTED_REVERSE[(x>>mask_size) & bit_mask] <<
          (2* mask_size) | PRECOMPUTED_REVERSE[(x>>(2*mask_size)) &bit_mask] << mask_size
          | PRECOMPUTED_REVERSE[(x>>(3*mask_size)) & bit_mask])
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
