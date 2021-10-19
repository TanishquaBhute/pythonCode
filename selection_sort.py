import time


class SelectionSort:
    def sort(self, lis, method='asc'):
        if method == 'asc':
            self.ascending_order(lis)
            return lis
        elif method == 'desc':
            self.descending_order(lis)
            return lis
        else:
            print("Invalid sorting method: 'asc' for Ascending and 'desc' for Descending ")

    def ascending_order(self, lis):
        start_time = time.time()
        for i in range(len(lis)):
            minimum = lis[i]
            for j in range(i+1, len(lis)):
                if lis[j] < minimum:
                    minimum = lis[j]

        # temp = minimum
        # lis[lis.index(minimum)] = lis[i]
        # lis[i] = temp
            temp = lis.index(minimum)
            lis[i], lis[temp] = lis[temp], lis[i]
        end_time = time.time()
        print(f"Ascending sort time: {end_time - start_time} sec")
        return lis

    def descending_order(self,lis):
        start_time = time.time()
        for i in range(len(lis)):
            maximum = lis[i]
            for j in range(i + 1, len(lis)):
                if lis[j] > maximum:
                    maximum = lis[j]

            temp = lis.index(maximum)
            lis[i], lis[temp] = lis[temp], lis[i]
        end_time = time.time()
        print(f"Descending sort time: {end_time - start_time} sec")
        return lis


if __name__ == '__main__':
        s1= SelectionSort()
        lis = [23, 5, 6, 12, 4, 34, 89, 56, 8, 9, 10, 40, 30, 0]
        print(f"Ascending sorted list: {s1.ascending_order(lis)}")
        print(f"Descending sorted list: {s1.descending_order(lis)}")




# for current_element in lis:
#     #print(lis[lis.index(current_element)+1])
#     #next_element_index = lis.index(current_element)+1
#     # for next_element in lis[next_element_index:]:
#     #     if next_element < minimum:
#     #         minimum = next_element
#     #minimum = [next_element for next_element in lis[next_element_index:] if next_element < minimum]
#     try:
#         minimum = min(lis[lis.index(current_element)+1:])
#     except:
#         minimum = current_element
#     temp = minimum
#     lis[lis.index(minimum)] = current_element
#     lis[lis.index(current_element)] = temp
# print(lis)
