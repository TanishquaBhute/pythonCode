import time


class InsertionSort:

    def sort(self, lis, method='asc'):
        if method == 'asc':
            self.ascending_order(lis)
            return lis
        elif method == 'desc':
            self.descending_order(lis)
            return lis
        else:
            print("Invalid sorting method: 'asc' for Ascending and 'desc' for Descending ")


    def ascending_order(self,lis):
        start_time = time.time()
        for i in range(1, len(lis)):
            temp = lis[i]
            j = i-1
            while j >= 0 and lis[j] > temp:
                lis[j+1] = lis[j]
                j -= 1
            lis[j+1] = temp
        end_time = time.time()
        print(f"Ascending sort time: {end_time - start_time} sec")
        return lis

    def descending_order(self, lis):
        start_time = time.time()
        for i in range(1, len(lis)):
            temp = lis[i]
            j = i-1
            while j >= 0 and lis[j] < temp:
                lis[j+1] = lis[j]
                j -= 1
            lis[j+1] = temp
        end_time = time.time()
        print(f"Descending sort time: {end_time - start_time} sec")
        return lis


if __name__ == '__main__':
    p1 = InsertionSort()
    lis = [23, 5, 6, 12, 4, 34, 89, 56, 8, 9, 10, 40, 30, 0]
    print(f"Ascending sorted list: {p1.ascending_order(lis)}")
    print(f"Descending sorted list: {p1.descending_order(lis)}")
