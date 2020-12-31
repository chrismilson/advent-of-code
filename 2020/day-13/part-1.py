from math import ceil

if __name__ == "__main__":
    with open('./bus-notes.txt') as f:
        t_0 = int(f.readline())
        buses = list(
            map(
                int,
                filter(
                    lambda x: x.isdigit(),
                    f.readline().strip().split(',')
                )
            )
        )
    minWait = float('inf')
    minBus = -1

    for busId in buses:
        waitingTime = ceil(t_0 / busId) * busId - t_0
        if waitingTime < minWait:
            minWait = waitingTime
            minBus = busId

    result = minWait * minBus
    print(result)
