

def binary_diff(int1, int2):

    diff = int1 ^ int2
    # print('{0:032b}'.format(int1))
    # print('{0:032b}'.format(int2))
    # print('{0:032b}'.format(diff))

    diff = '{0:032b}'.format(diff)
    return diff.count('0') / 32


def complement(num):

    return num ^ 4294967295


def main():
    int1 = int(input('Enter a number: '))
    int2 = int(input('Enter another number: '))
    compatibility = binary_diff(int1, int2)
    comp1 = complement(int1)
    comp2 = complement(int2)

    print('{:.2f}'.format(compatibility * 100) + '% Compatibility')
    print('{:3d}'.format(int1), 'should avoid', '{0:032b}'.format(comp1))
    print('{:3d}'.format(int2), 'should avoid', '{0:032b}'.format(comp2))

if __name__ == '__main__':
    main()
