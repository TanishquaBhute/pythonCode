import time


class BubbleSort:

    def ascending_order(self, lis):
        start_time = time.time()
        lis_length = len(lis)
        for i in range(lis_length-1):
            for j in range(0, lis_length-i-1):
                if lis[j] > lis[j+1]:
                    lis[j], lis[j+1] = lis[j+1], lis[j]
        end_time = time.time()
        print(f"Ascending sort time: {end_time - start_time} sec")
        return lis

    def descending_order(self, lis):
        start_time = time.time()
        lis_length = len(lis)
        for i in range(lis_length - 1):
            for j in range(0, lis_length-i-1):
                if lis[j] < lis[j + 1]:
                    lis[j], lis[j + 1] = lis[j + 1], lis[j]
        end_time = time.time()
        print(f"Descending sort time: {end_time - start_time} sec")
        return lis

    def sort(self, lis, method='asc'):
        if method == 'asc':
            self.ascending_order(lis)
            return lis
        elif method == 'desc':
            self.descending_order(lis)
            return lis
        else:
            print("Invalid sorting method: 'asc' for Ascending and 'desc' for Descending ")


if __name__ == '__main__':
    b1 = BubbleSort()
    lis = [21, 34, 3, 4, 56, 98, 43, 29, 24, 59, 80, 60]
    sorted_list1 = b1.ascending_order(lis)
    print(f"Sorted list in Ascending order: {sorted_list1}")

    sorted_list2 = b1.descending_order(lis)
    print(f"Sorted list in Descending order: {sorted_list2}")
