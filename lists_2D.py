matrix_a = [[1, 2, 3],
            [5, 2, 6],
            [10, 4, 2],
            [7, 8, 9]]
print(type(matrix_a[1]))
print(matrix_a[1][2])

'''
returns a list containing sums of each row
'''
def sum_rows(matrix):
    result = []
    for row in matrix:
        total = 0
        for value in row:
            total += value
        result.append(total)
    return result

'''
returns a list containing sums of each column
'''


def sum_cols(matrix):
    num_cols = len(matrix[0])
    result = []
    for j in range(num_cols):
        total = 0
        for row in matrix:
            total += row[j]
        result.append(total)
    return result

def sum_cols_single_line(matrix_a):
    return [sum(row[j] for row in matrix_a) for j in range(len(matrix_a[0]))]
#def sum_cols(matrix):

def sum_cols_zip(matrix_a):
    print(list(zip(*matrix_a)))
    return sum_rows(list(zip(*matrix_a)))


'''
returns the sum of all elements of matrix
'''
#def sum_all(matrix):


print(f'sum_rows(matrix_a) = {sum_rows(matrix_a)}')
print(f'sum_cols(matrix_a) = {sum_cols(matrix_a)}')
print(f'sum_cols_single_line(matrix_a) = {sum_cols_single_line(matrix_a)}')
print(f'sum_cols_zip(matrix_a) = {sum_cols_zip(matrix_a)}')

list_a = [1, 2, 3]
list_b = [2*x for x in list_a]
print(f'list_a = {list_a}')
print(f'list_b = {list_b}')
list_c = [2*x for x in list_a if x != 2]
print(f'list_c = {list_c}')

zipped_lists = list(zip(list_a, list_b))
print(f'zipped_lists = {zipped_lists}')
# * - unzip
unzipped_lists = list(zip(*zipped_lists))
print(f'unzipped_lists = {unzipped_lists}')