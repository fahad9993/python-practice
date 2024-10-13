# Function with unlimited POSITIONAL arguments
def add(*args):
    sum_n = 0
    for n in args:
        sum_n += n
    print(f"Sum: {sum_n}")


add(1, 2, 3, 4, 5)