def roundFloat(A):
    if A > 0:
        B = int(A + 0.5)
        return B
    else:
        B = int(A - 0.5)
        return B

def main():
    A = float(input("input a floating-point number: "))
    print(roundFloat(A))
    

