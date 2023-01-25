import matplotlib.pyplot as plt

Q = 2000
V = [2, 6, 4, 8, 100, 5, 7, 23, 654, 5]
starting_point = [0 for _ in range(len(V))]
pos = [0 for _ in range(len(V))]
num_points = 0
points = [[] for _ in range(len(V))]


def update_pos():
    for i in range(len(pos)):
        pos[i] = (pos[i] + V[i]) % Q


def calculate_lattice():
    global num_points
    while pos != starting_point or num_points == 0:
        for i in range(len(points)):
            points[i].append(pos[i])
        num_points += 1
        update_pos()


def create_2D_plot():
    plt.title("Lattice of " + str(V) + " with mod " + str(Q))
    plt.text(Q / 2, -Q / 10, "Number of points=" + str(num_points), horizontalalignment='center')
    plt.xlim(0, Q)
    plt.ylim(0, Q)
    plt.plot(points[0], points[1], 'o')
    plt.show()


def create_3D_plot():
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(projection='3d')

    ax.set_xlim3d(0, Q)
    ax.set_ylim3d(0, Q)
    ax.set_zlim3d(0, Q)

    ax.scatter(points[0], points[1], points[2])
    plt.show()


def show_results():
    print("mod Q =", Q)
    print("Vector =", V)
    print("Number of points =", num_points)


if __name__ == '__main__':
    calculate_lattice()
    show_results()
    if len(V) == 2:
        create_2D_plot()
    elif len(V) == 3:
        create_3D_plot()
