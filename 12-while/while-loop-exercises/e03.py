# PyNative Loop exercises using 'while'
# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/


# -----------------------------------------------------------------------------
def e03(input_num: int):
    '''Exercise 3: Calculate the sum of all numbers from 1 to a given number.
       For example, if the user entered 10 the output should be 55
       (1+2+3+4+5+6+7+8+9+10)'''

    start: int = 1
    end:   int = input_num

    iter:        int  = start
    accumulator: int  = 0
    finished:    bool = (iter > end)

    while (not finished):
        accumulator = accumulator + iter
        print(f"Iterator: {iter}, Accumulator: {accumulator}")

        iter     = iter + 1
        finished = (iter > end)

    print(f"Sum is: {accumulator}")


# Main
# -----------------------------------------------------------------------------
# input_num: int = int(input("Enter number: "))
# e03(input_num)
e03(10)
# -----------------------------------------------------------------------------
