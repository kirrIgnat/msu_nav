import scipy
import numpy as np
import matplotlib.pyplot as plt


def fun(x, f, a):
    S_a = np.array(([x[0], x[1], x[2]],
                    [x[3], x[4], x[5]],
                    [x[6], x[7], x[8]]))
    b = np.array(([x[9]], [x[10]], [x[11]]))
    D = np.array([S_a @ f[:, [0]] + b - a[:, [0]],
                  S_a @ f[:, [1]] + b - a[:, [1]],
                  S_a @ f[:, [2]] + b - a[:, [2]],
                  S_a @ f[:, [3]] + b - a[:, [3]],
                  S_a @ f[:, [4]] + b - a[:, [4]],
                  S_a @ f[:, [5]] + b - a[:, [5]]])
    X = []
    for el in D:
        for e in el:
            X.append(*e)
    return np.array(X)


def acs_sec(file):

    lines = file.read().splitlines()
    acs_x, acs_y, acs_z = [], [], []
    data = []

    for i in lines:
        data.append(i.split('\t'))

    for i in range(3, len(data) - 1):
        acs_x.append(int(data[i][5]))
        acs_y.append(int(data[i][6]))
        acs_z.append(int(data[i][7]))

    fig1 = plt.figure(figsize=(7, 7))
    ax = fig1.add_subplot(211)
    ax.plot(acs_x, 'r')
    ax.plot(acs_y, 'g')
    ax.plot(acs_z, 'b')

    n = 301
    acs_x = scipy.signal.medfilt(acs_x, kernel_size=n)
    acs_y = scipy.signal.medfilt(acs_y, kernel_size=n)
    acs_z = scipy.signal.medfilt(acs_z, kernel_size=n)


    x_up = 400
    x_down = 1200

    y_up = 1800
    y_down = 2400

    z_up = 2800
    z_down = 3400

    g = 9.81
    b_a = np.zeros((3, 1))
    s_a = np.zeros((3, 4))

    a_ = np.array(([acs_x[x_up], acs_y[x_up], acs_z[x_up]],
                   [acs_x[x_down], acs_y[x_down], acs_z[x_down]],
                   [acs_x[y_up], acs_y[y_up], acs_z[y_up]],
                   [acs_x[y_down], acs_y[y_down], acs_z[y_down]],
                   [acs_x[z_up], acs_y[z_up], acs_z[z_up]],
                   [acs_x[z_down], acs_y[z_down], acs_z[z_down]]))
    a_ = a_.transpose()

    f_z = -np.array(([g, 0, 0], [-g, 0, 0],
                     [0, g, 0], [0, -g, 0],
                     [0, 0, g], [0, 0, -g]))
    S = s_a[:3, :3]
    b = s_a[:, 3:]
    x0 = np.zeros(12)

    f_z = f_z.transpose()
    # print(f_z)
    # print(a_)
    # print('----------')
    res = scipy.optimize.least_squares(fun, x0, args=(f_z, a_))
    S_A = np.array([[res.x[0], res.x[1], res.x[2]],
                    [res.x[3], res.x[4], res.x[5]],
                    [res.x[6], res.x[7], res.x[8]]])
    b_A = np.array([[res.x[9]], [res.x[10]], [res.x[11]]])

    S_f = np.linalg.inv(S_A)
    # print(np.round(S_A, 2))
    b_f = -S_f @ b_A
    F_Z = np.zeros((3, len(acs_x)))
    A = []
    for i in range(len(acs_x)):
        A.append((acs_x[i], acs_y[i], acs_z[i]))
    A = np.array(A).transpose()
    for i in range(len(acs_x)):
        F_Z[0][i], F_Z[1][i], F_Z[2][i] = S_f @ A[:, [i]] + b_f
    ax3 = fig1.add_subplot(212)
    # print(F_Z[:, 0])
    ax3.plot(F_Z[0, :], 'r')
    ax3.plot(F_Z[1, :], 'g')
    ax3.plot(F_Z[2, :], 'b')


    return plt
