from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    # TODO - you fill in here.
    def add(a,b):
        return a if b==0 else add(a^b, (a&b) << 1)
    
    running_sum=0
    while x: #examines each bit of x
        print(running_sum)
        if x & 1:
            running_sum=add(running_sum, y)
        x, y = x >> 1, y <<1
    return running_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
