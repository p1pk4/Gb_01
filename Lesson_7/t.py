# class Matrix:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return str(self.x, self.y)

#     def __add__(self, other):
#         result_list = []
#         for i, k in zip(self.x, other.y):
#             result_list.append(i + k)
#             return Matrix(result_list)
        
        

# x = Matrix([1, 2, 3, 4],[4, 5, 6, 7])
# y = Matrix([4, 5, 6, 7],[4, 5, 6, 7])
# print(x + y)





class Matrix:
    
    def __init__(self, list1, list2):#, list_of_lists):
        self.list1 = list1
        self.list2 = list2
        # self.list_of_lists = list_of_lists
        # print(list1, list2)

    def __add__(self, other):
        
        return Matrix(self.list1 + other.list1, self.list2 + other.list2)
        
    
        
    def __str__(self):
        return f"Это матрицы {self.list1}, {self.list2}"
        
list1 = Matrix([1, 2, 3, 4, 5], [5, 6, 7, 8, 9])
list2 = Matrix([10, 11, 12, 13, 14], [15, 16, 17, 18, 19])
print(list1 + list2)

# new_matrix = Matrix()
# new_matrix()
# list1 = Matrix(3, 5)
# list2 = Matrix(7, 5)




