# ---------------------------------------------
def find_num3(num_list: list[int]) -> bool:
    """Return True if find number 3 in list."""

    index:        int  = 0
    found:        bool = False
    out_of_range: bool = (index == len(num_list))
    finished:     bool = found or out_of_range

    while not finished:

        # Body
        num   = num_list[index]
        found = (num == 3)

        # Update finishing condition
        index        = index + 1
        out_of_range = (index == len(num_list))
        finished     = found or out_of_range

    return found

# Main
# ---------------------------------------------
num_list: list[int] = [0, 1, 2, 3, 4, 5]
result:   bool      = find_num3(num_list)
print(result)
# ---------------------------------------------