# solution 1
import copy
data_1 = data
data_2 = copy.deepcopy(data_1)

for i in range(5):
    for i in range(1, 9):
        for j in range(1, 9):
            data_2[i][j] = (data_1[i][j-1] + data_1[i][j+1] + data_1[i-1][j] + data_1[i+1][j])/4.
    data_1, data_2 = data_2, data_1
plot_image(data_2)