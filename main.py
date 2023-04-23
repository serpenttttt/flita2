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
set_edges = set()
for string_of_nodes in matrix:
    for i in range(len(string_of_nodes)):
        for j in range(len(string_of_nodes)):
            if j < len(string_of_nodes):
                if (j + 1) < len(string_of_nodes) and string_of_nodes[i] == string_of_nodes[j + 1] == '1' and i + 1 != j + 2:
                    set_edges.add(str(i+1) + str(j+2))
                else:
                    count = 0
                    for k in string_of_nodes:
                        if k == '1':
                            count = count + 1
                    if string_of_nodes[j] == '1' and count == 1:
                        set_edges.add(str(j + 1) + str(j + 1))

print(list(set_edges))

dot.edges(list(set_edges))

print(dot.source)

# Выводим пользователю граф
dot.render('doctest-output/round-table.gv', view=True)
