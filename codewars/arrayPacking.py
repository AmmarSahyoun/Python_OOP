"""  are given an array of up to four non-negative integers,  task is to pack these integers into one number
    The first element of the array occupies the first 8 bits of M;
    The second element occupies next 8 bits, and so on.
 """
def array_packing(arr):
    result = "".join(reversed([f"{n:08b}" for n in arr]))
    return int(result, 2)



a=[24, 85, 0]
print(array_packing(a))