def count_of_leaf(arr: list) -> int:
    count = 0
    for item in arr:
        if not isinstance(item, list):
            count += 1
        else:
            count += count_of_leaf(item)
    return count


def flatten_list_recursive(arr: list) -> None:
    flattened = []
    for item in arr:
        if not isinstance(item, list):
            flattened.append(item)
        else:
            flattened.extend(flatten_list_recursive(item))
    return flattened


def flatten_list_iterative(arr: list) -> None:
    flattened = []

    while arr:
        if not isinstance(arr[0], list):
            flattened.append(arr.pop(0))
        else:
            l = arr.pop(0)
            arr = l + arr
    return flattened



if __name__ == "__main__":
    nested_list = [
        1,
        [2, 3, 4],
        [5, 6, [7, 8, [9, 10]]],
        11,
        [12, 13, [14, 15, 16, [17, [18, 19, [20, 21, [22, 23, [24, [25, [26]]]]]]]]],
    ]
    print(f"Length of Nested List: {len(nested_list)}")
    print(f"Number of Leaf elements: {count_of_leaf(nested_list)}")
    print(f"Flattened List: {flatten_list_recursive(nested_list)}")
    print(f"Flattened List: {flatten_list_iterative(nested_list)}")
