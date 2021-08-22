from time import perf_counter, perf_counter_ns


class MyList:
    def __init__(self, arr: list):
        self.arr = arr

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(" + "[" + ", ".join(map(str, self.arr)) + "])"
        )

    def __partition(self, start: int, end: int) -> int:
        pivot = self.arr[start]
        low = start + 1
        high = end
        while low <= high:
            if self.arr[low] <= pivot:
                low += 1
            if self.arr[high] >= pivot:
                high -= 1
            if low <= high:
                self.arr[high], self.arr[low] = self.arr[low], self.arr[high]
            else:
                break
        self.arr[start], self.arr[high] = self.arr[high], self.arr[start]
        return high

    def quicksort(self, start: int = None, end: int = None) -> None:
        if start is None:
            start = 0
        if end is None:
            end = len(self.arr) - 1

        if start >= end:
            return
        p = self.__partition(start, end)
        self.quicksort(start, p - 1)
        self.quicksort(p + 1, end)


if __name__ == "__main__":
    q = MyList([6, 9, 8, 7, 6, 6, 5, 4, 3, 2, 1, 6])
    print(f"Before Quick Sort: {q}")
    q.quicksort()
    print(f"After Quick Sort: {q}")
