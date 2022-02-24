# ---------------------------------------------
def loop_02() -> list[int]:
    """Return a list of 10 ints"""

    count:    int  = 0
    finished: bool = (count > 9)
    result:   list[int] = []

    while not finished:

        # Body
        result.append(count)

        # Update finishing condition
        count = count + 1
        finished = (count > 9)

    return result

# Main
# ---------------------------------------------
num_list: list[int] = loop_02()
print(num_list)

# ---------------------------------------------