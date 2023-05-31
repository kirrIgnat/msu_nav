import scipy
import numpy as np
import matplotlib.pyplot as plt


def fun(x, Fi, fi):
    S_w = np.array(([x[0], x[1], x[2]],
                    [x[3], x[4], x[5]],
                    [x[6], x[7], x[8]]))
    D = []
    for i in range(6):
        D.append(S_w @ Fi[:, i] - fi[:, i])
    D = np.array(D)
    X = []
    for el in D:
        for j in el:
            X.append(j)
    return np.array(X)


def dus_sec(file):
    lines = file.read().splitlines()
    gyro1, gyro2, gyro3 = [], [], []
    data = []
    for i in range(len(lines)):
        data.append(lines[i].split('\t'))

    for i in range(3, len(data) - 1):
        gyro1.append(int(data[i][8]))
        gyro2.append(int(data[i][9]))
        gyro3.append(int(data[i][10]))

    fig2 = plt.figure(figsize=(7, 7))
    ax1 = fig2.add_subplot(211)
    ax1.plot(gyro1, 'r')
    ax1.plot(gyro2, 'g')
    ax1.plot(gyro3, 'b')

    dt = (56 * 60 + 13 + 0.226 - 53 * 60 - 52 - 0.499) / len(gyro3)
    # print(dt)
    gyro1 = np.array(gyro1)
    gyro2 = np.array(gyro2)
    gyro3 = np.array(gyro3)

    b_w = np.array([gyro1[1], gyro2[1], gyro3[1]])
    gyro1 = gyro1 - b_w[0] * np.ones(np.shape(gyro1))
    gyro2 = gyro2 - b_w[1] * np.ones(np.shape(gyro1))
    gyro3 = gyro3 - b_w[2] * np.ones(np.shape(gyro1))

    gyro1 = scipy.signal.medfilt(gyro1, kernel_size=3)
    gyro2 = scipy.signal.medfilt(gyro2, kernel_size=3)
    gyro3 = scipy.signal.medfilt(gyro3, kernel_size=3)
    phi = np.zeros((3, 6))
    delt = 125

    for i in range(1200, 1200 + delt):
        phi[0][0] += gyro1[i] * dt
    for i in range(1880, 1880 + delt):
        phi[0][3] += gyro1[i] * dt
    for i in range(3035, 3035 + delt):
        phi[1][1] += gyro2[i] * dt
    for i in range(3770, 3770 + delt):
        phi[1][4] += gyro2[i] * dt
    for i in range(5020, 5020 + delt):
        phi[2][2] += gyro3[i] * dt
    for i in range(5625, 5625 + delt):
        phi[2][5] += gyro3[i] * dt
    phi = np.round(phi, 1)

    Phi = np.hstack((np.eye(3), -np.eye(3))) * np.pi
    x0 = np.zeros(9)

    res = scipy.optimize.least_squares(fun, x0, args=(Phi, phi))
    S_w = np.array([[res.x[0], res.x[1], res.x[2]],
                    [res.x[3], res.x[4], res.x[5]],
                    [res.x[6], res.x[7], res.x[8]]])
    # print(S_w)
    s_o = np.linalg.inv(S_w)
    b_o = -s_o @ b_w

    gyr = []
    for i in range(len(gyro1)):
        gyr.append(np.array([gyro1[i], gyro2[i], gyro3[i]]))

    O_z = []
    for i in range(len(gyr)):
        o = s_o @ gyr[i]
        O_z.append(o)
    O_z = np.array(O_z)

    ax3 = fig2.add_subplot(212)

    ax3.plot(O_z[:, 0], 'r')
    ax3.plot(O_z[:, 1], 'g')
    ax3.plot(O_z[:, 2], 'b')
    phi = phi * 0


    for i in range(1200, 1200 + delt):
        phi[0][0] += O_z[i][0] * dt
    for i in range(1880, 1880 + delt):
        phi[0][3] += O_z[i][0] * dt
    for i in range(3035, 3035 + delt):
        phi[1][1] += O_z[i][1] * dt
    for i in range(3770, 3770 + delt):
        phi[1][4] += O_z[i][1] * dt
    for i in range(5020, 5020 + delt):
        phi[2][2] += O_z[i][2] * dt
    for i in range(5625, 5625 + delt):
        phi[2][5] += O_z[i][2] * dt
    # print(np.round(phi * 180 / np.pi))

    plt.plot(gyro1, 'r')
    plt.plot(gyro2, 'g')
    plt.plot(gyro3, 'b')

    return plt
