import scipy
import numpy as np
import matplotlib.pyplot as plt



def acs(file):

    lines = file.read().splitlines()
    acs_x, acs_y, acs_z = [], [], []
    acs = []
    data = []
    for i in range(len(lines)):
        data.append(lines[i].split('\t'))

    for i in range(3, len(data) - 1):
        acs_x.append(int(data[i][5]))
        acs_y.append(int(data[i][6]))
        acs_z.append(int(data[i][7]))

    t = np.linspace(0, 96, len(acs_x))
    fig1 = plt.figure(figsize=(7, 7))

    ax = fig1.add_subplot(211)
    ax.plot(acs_x, 'r')
    ax.plot(acs_y, 'g')
    ax.plot(acs_z, 'b')

    n = 301
    acs_x = scipy.signal.medfilt(acs_x, kernel_size=n)
    acs_y = scipy.signal.medfilt(acs_y, kernel_size=n)
    acs_z = scipy.signal.medfilt(acs_z, kernel_size=n)

    # plt.show()


    for i in range(len(acs_x)):
        acs.append(np.array([acs_x[i], acs_y[i], acs_z[i]]))

    x_up = 400
    x_down = 1200

    y_up = 1800
    y_down = 2400

    z_up = 2800
    z_down = 3400

    g = 9.81
    s1, s2, s3, s, b = [], [], [], [], []

    for i in range(3):
        s1.append(round((acs[x_down][i] - acs[x_up][i]) / (2 * g), 3))
        s2.append(round((acs[y_down][i] - acs[y_up][i]) / (2 * g), 3))
        s3.append(round((acs[z_down][i] - acs[z_up][i]) / (2 * g), 3))

    s.append(s1)
    s.append(s2)
    s.append(s3)
    b.append((acs[x_up][0] + acs[x_down][0]) / 2)
    b.append((acs[y_up][1] + acs[y_down][1]) / 2)
    b.append((acs[z_up][2] + acs[z_down][2]) / 2)
    B_matrix = np.array(b)
    S_matrix = np.array(s)

    s_f = np.linalg.inv(S_matrix)
    b_f = - s_f @ B_matrix
    F_z = []

    for i in range(len(acs)):
        f = s_f @ acs[i] + b_f
        F_z.append(f)

    F_z = np.array(F_z)


    ax3 = fig1.add_subplot(212)
    ax3.plot(F_z[:, 0], 'r')
    ax3.plot(F_z[:, 1], 'g')
    ax3.plot(F_z[:, 2], 'b')


    return plt
