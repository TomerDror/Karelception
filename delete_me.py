def nand(bit1, bit2):
    return not (bit1 and bit2)

def find_numbers_with_true_nand(n):
    print("output:" )
    for num in range(n):
        binary_num = bin(num)[2:]
        length = len(binary_num)
        valid = True
        for i in range(0, length - 1, 2):
            bit1 = int(binary_num[length - i - 1])
            bit2 = int(binary_num[length - i - 2])
            if not nand(bit1, bit2):
                valid = False
                break
        if valid:
            print(num, end=" ")

# Test with n = 16
find_numbers_with_true_nand(int(input("enter input: ")))

