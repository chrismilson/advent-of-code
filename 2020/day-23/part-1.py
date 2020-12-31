def doMove(currentState):
    # We need some information to do the move:
    # - What is the index of the destination cup?
    j = max(
        range(4, len(currentState)),
        key=lambda x: (currentState[x] - currentState[0]) % 10
    )

    return currentState[4:j+1] + currentState[1:4] + currentState[j+1:] + [currentState[0]]


if __name__ == "__main__":
    # My input
    initial = "326519478"
    # The example
    # initial = "389125467"

    state = list(map(int, initial))
    numMoves = 100
    for _ in range(numMoves):
        state = doMove(state)
    i = state.index(1)
    result = ''.join(map(str, state[i+1:] + state[:i]))

    print(result)
