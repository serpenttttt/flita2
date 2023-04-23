import numpy as np
import graphviz

match input("Directed = yes, not directed = no\n"):
    case 'yes':
        dot = graphviz.Digraph()
    case 'no':
        dot = graphviz.Graph()
    case _:
        print("Unknown command")
        exit('-1')

# Считываем матрицу из файла
matrix_of_incedence = []
nodes = 0
with open("matrix.txt") as matrix_file:
    for string in matrix_file:
        nodes = nodes + 1
        row = string.split()
        matrix_of_incedence.append(row)

# Добавляем вершины
for i in range(nodes):
    dot.node(str(i+1))

# Записали матрицу
arr = np.array(matrix_of_incedence, str)
# Оттранспонировали ее
matrix = arr.transpose()

print(matrix)

# Добавляем ребра
set_edges = []
for string_of_nodes in matrix:
    one_node = True
    for i in range(len(string_of_nodes)):
        for j in range(i + 1, len(string_of_nodes)):
            if string_of_nodes[i] == string_of_nodes[j] == '1':
                set_edges.append(str(i+1) + str(j+1))
                one_node = False
    if one_node:
        for i in range(len(string_of_nodes)):
            if string_of_nodes[i] == '1':
                set_edges.append(str(i+1) + str(i+1))

dot.edges(list(set_edges))

# Выводим пользователю граф
dot.render('doctest-output/round-table.gv', view=True)
