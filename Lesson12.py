grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [
    [-1, 0],  # go up
    [0, -1],  # go left
    [1, 0],  # go down
    [0, 1],
]  # go right

delta_name = ["^", "<", "v", ">"]


def search(grid, init, goal, cost):
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    g = 0
    x, y = init

    open = [[g, x, y]]

    found = False
    resign = False
    count = 0

    while found is False and resign is False:
        if len(open) == 0:
            resign - True
            return "Fail"

        else:
            open.sort()
            open.reverse()
            next = open.pop()

            g, x, y = next
            expand[x][y] = count
            count += 1

            if [x, y] == goal:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    # Check out of bound
                    if (
                        x2 >= 0
                        and x2 < len(grid)
                        and y2 >= 0
                        and y2 < len(grid[0])
                    ):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
    # ----------------------------------------

    for i in range(len(grid)):
        print(expand[i])

    policy = [[" " for row in range(len(grid[0]))] for col in range(len(grid))]
    x, y = goal
    policy[x][y] = "*"

    while x != init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        policy[x2][y2] = delta_name[action[x][y]]
        x, y = x2, y2

    for i in range(len(grid)):
        print(policy[i])

    return expand


search(grid, init, goal, cost)
