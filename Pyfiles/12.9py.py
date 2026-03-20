def MyRange(start=0, end=100, step=1):
    if step == 0:
        raise ValueError("MyRange() step argument must not be zero")
    current = start

    if step > 0:
        while current < end:
            yield current
            current += step
    else:
        while current > end:
            yield current
            current += step 

if __name__ == "__main__":
    A = MyRange(0, 9, 1)
    try:
        while True:
            value = next(A)
            print(f"  next(A) = {value}")
    except StopIteration:
        print("end")

    
    
