def selection_sort(l: list) -> None:
    """
    For every pass, swap min number with min index
    l = [5,4,3,1,2]
    Iteration 1: Swap 5 with 1 -> [1,4,3,5,2]
    Iteration 2: Swap 4 with 2 -> [1, 2, 3, 5, 4]
    Iteration 3: No Swap
    Iteration 4: Swap 5 with 4 --> [1,2,3,4,5]
    Iteration 5: No Swap
    """
    for i in range(len(l)):
        min_index = i
        print(f"Initial Min Index: {min_index}")
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        print(f"...Min Index: {min_index}")
        l[i], l[min_index] = l[min_index], l[i]
        print(f"List after swap: {l}")


if __name__ == "__main__":
    l = [5, 4, 3, 1, 2]
    selection_sort(l)
    print(f"After Selection Sort: {l}")
