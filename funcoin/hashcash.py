from hashlib import sha256
from timeit.timit import timer_decorator


@timer_decorator
def find_zero():
    x = 5
    y = 0
    hash = None

    while True:
        hash = sha256(f"{x*y}".encode()).hexdigest()
        last_digit = hash[-1]
        if last_digit == "0":
            break
        y += 1

    print(f"The solution is y={y}. With hash of: {hash}")


find_zero()
