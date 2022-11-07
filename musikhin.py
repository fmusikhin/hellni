def taynayakomnata(a):
    while a.isdigit() == False:
        a = input("a=")
    else:
        a = int(a)
    return a
def massivka(n,m):
    a = {}
    for i in range(n):
        for j in range(m):
            a[i, j] = taynayakomnata(input())
    for i in range(n):
        print(*[a[i, j] for j in range(m)])
    return a

def sum_matrices(matrix1, matrix2):
    result = []
    for sublist in zip(matrix1, matrix2):
        temp = []
        for numbers in zip(sublist[n-1], sublist[m-1]):
            temp.append(sum(numbers))
        result.append(temp)
    return result
print("Введите количество строк n ")
n = taynayakomnata(input())
print("Ведите количество столбцов m")
m = taynayakomnata(input())
print("Введите элементы массива А")
matrix1 = massivka(n,m)
print("Введите количество строк n1 ")
n1 = taynayakomnata(input())
print("Ведите количество столбцов m1")
m1 = taynayakomnata(input())
print("Введите элементы массива B")
matrix2 = massivka(n1,m1)
result = sum_matrices(matrix1, matrix2)
print(result)














def main():
    def matrix_generator(rows, columns):
        main_list = []
        for i in range(rows):
            main_list.append([random.randint(1, 65323) for i in range(columns)])
        return main_list

    def sum_matrices(matrix1, matrix2):
        result = []
        for sublist in zip(matrix1, matrix2):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            result.append(temp)
        return result

    def print_matrix(out, matrix):
        print(out)
        for i in matrix:
            print(i)
        print('')

    matrix1 = matrix_generator(3, 3)
    matrix2 = matrix_generator(3, 3)
    result = sum_matrices(matrix1, matrix2)

    for i in (('Первая матрица', matrix1), ('Вторая матрица', matrix2), ('Результирущая матрица', result)):
        print_matrix(i[0], i[1])


main()