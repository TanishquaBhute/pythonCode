from bubble_sort import BubbleSort
from selection_sort import SelectionSort
from insertion_sort import InsertionSort
bubble = BubbleSort()
lis = list(range(1, 1001))
bubble.sort(lis, 'asc')
print(f"Ascending sorted list : {lis}")
bubble.sort(lis, 'desc')
print(f"Descending sorted list :{lis}")
bubble.sort(lis, 'selection')

selection = SelectionSort()
selection.sort(lis, 'asc')
print(f"Ascending sorted list : {lis}")
selection.sort(lis, 'desc')
print(f"Descending sorted list :{lis}")
selection.sort(lis, 'selection')

insertion = InsertionSort()
insertion.sort(lis, 'asc')
print(f"Ascending sorted list : {lis}")
insertion.sort(lis, 'desc')
print(f"Descending sorted list :{lis}")
insertion.sort(lis, 'selection')



