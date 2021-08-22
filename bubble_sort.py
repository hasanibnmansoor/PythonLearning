def bubble_sort(l: list) -> None:
    """
    Method 1:
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    ------------------------------------------
    Method 2: Optimized #1
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                has_swapped = True
    ------------------------------------------
    Method 3: Optimized #2
    has_swapped = True
    n = 0
    while has_swapped:
        has_swapped = False
        for i in range(len(l) - n - 1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                has_swapped = True
        n += 1
    """
    has_swapped = True
    n = 0
    while has_swapped:
        has_swapped = False
        for i in range(len(l) - n - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                has_swapped = True
        n += 1


if __name__ == "__main__":
    li = [1, 6, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, 6]
    bubble_sort(li)
    print(f"After Bubble Sort: {li}")
