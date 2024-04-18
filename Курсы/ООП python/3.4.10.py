class MaxPooling:
    def __init__(self, step = (2,2), size = (2,2)):
        self.step = step
        self.size = size

    def __call__(self, matrix,*args, **kwargs):
        if len(matrix) != len(matrix[0]):
            raise ValueError("Неверный формат для первого параметра matrix.")
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if type(matrix[i][j]) != int :
                    raise ValueError("Неверный формат для первого параметра matrix.")
        lst_max=[]
        new_lst = []
        for i in range(self.size[0]**2):
            lst_max.append(matrix[i])
        new_lst.append(max(lst_max))



