# -*- coding: utf-8 -*-

import numpy as np
# import matplotlib.pyplot as plt

input_data = np.array([[0, 0, 0], [1, 0, 1], [0, 1, 1], [1, 1, 0]])
data_number = input_data.shape[0]

init_weight = np.random.rand(3, 3)

epochs = 10000
alpha = 0.1

w111 = init_weight[0, 0]
w112 = init_weight[0, 1]
b11 = init_weight[0, 2]
w121 = init_weight[1, 0]
w122 = init_weight[1, 1]
b12 = init_weight[1, 2]
w211 = init_weight[2, 0]
w212 = init_weight[2, 1]
b21 = init_weight[2, 2]


def S(z):
    return 1 / (1 + np.exp(-z))


# for t in range(epochs):
#     for i in range(data_number):
#         Z11 = b11 + w111 * input_data[i, 0] + w112 * input_data[i, 1]
#         Z12 = b12 + w121 * input_data[i, 0] + w122 * input_data[i, 1]
#         O11 = S(Z11)
#         O12 = S(Z12)
#         Z21 = b21 + w211 * O11 + w212 * O12
#         O21 = S(Z21)
#         error = (input_data[i, 2] - O21) ** 2
#
#         dw111 = 2 * (O21 - input_data[i, 2]) * S(Z21) * (1 - S(Z21)) * w211 * S(Z11) * (1 - S(Z11)) * input_data[i, 0]
#         dw112 = 2 * (O21 - input_data[i, 2]) * S(Z21) * (1 - S(Z21)) * w211 * S(Z11) * (1 - S(Z11)) * input_data[i, 1]
#         db11 = 2 * (O21 - input_data[i, 2]) * S(Z21) * (1 - S(Z21)) * w211 * S(Z11) * (1 - S(Z11))
#         dw121 = 2 * (O21 - input_data[i, 2]) * S(Z21) * (1 - S(Z21)) * w212 * S(Z12) * (1 - S(Z12)) * input_data[i, 0]
#         dw122 = 2 * (O21 - input_data[i, 2]) * S(Z21) * (1 - S(Z21)) * w212 * S(Z12) * (1 - S(Z12)) * input_data[i, 1]
#         db12 = 2 * (O21 - input_data[i, 2]) * S(Z21) * (1 - S(Z21)) * w212 * S(Z12) * (1 - S(Z12))
#         dw211 = 2 * (O21 - input_data[i, 2]) * S(Z21) * (1 - S(Z21)) * O11
#         dw212 = 2 * (O21 - input_data[i, 2]) * S(Z21) * (1 - S(Z21)) * O12
#         db21 = 2 * (O21 - input_data[i, 2]) * S(Z21) * (1 - S(Z21))
#
#         w111 = w111 - alpha * (dw111)
#         w112 = w112 - alpha * (dw112)
#         b11 = b11 - alpha * (db11)
#         w121 = w121 - alpha * (dw121)
#         w122 = w122 - alpha * (dw122)
#         b12 = b12 - alpha * (db12)
#         w211 = w211 - alpha * (dw211)
#         w212 = w212 - alpha * (dw212)
#         b21 = b21 - alpha * (db21)
#     # plt.scatter(t, error)
#
# x1 = np.array([0, 0, 1, 1])
# x2 = np.array([0, 1, 0, 1])
#
# Z11 = b11 + w111 * x1 + w112 * x2
# Z12 = b12 + w121 * x1 + w122 * x2
# O11 = S(Z11)
# O12 = S(Z12)
# Z21 = b21 + w211 * O11 + w212 * O12
# O21 = S(Z21)
# print(O21)

for i in range(5):
    print(init_weight)
