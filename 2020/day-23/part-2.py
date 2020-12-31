class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def doMoves(initialState, numMoves):
    # We need some information to do the move:
    # - What is the index of the destination cup?
    n = len(initialState)
    head = ListNode(0)
    curr = head
    allNodes = {}

    for val in initialState:
        curr.next = ListNode(val)
        curr = curr.next
        allNodes[val] = curr

    curr.next = head.next
    curr = curr.next

    for _ in range(numMoves):
        moving = set()
        auxHead = curr.next
        aux = curr
        for _ in range(3):
            moving.add(aux.next.val)
            aux = aux.next
        curr.next = aux.next
        dest = curr.val - 1
        dest = ((dest - 1) % n) + 1
        while dest in moving:
            dest -= 1
            dest = ((dest - 1) % n) + 1
        allNodes[dest].next, aux.next = auxHead, allNodes[dest].next
        curr = curr.next
    result = []
    for _ in initialState:
        result.append(curr.val)
        curr = curr.next
    return result


if __name__ == "__main__":
    # My input
    initial = "326519478"
    # The example
    # initial = "389125467"

    state = list(map(int, initial)) + \
        list(range(int(max(initial)) + 1, int(1e6) + 1))
    numMoves = int(1e7)
    state = doMoves(state, numMoves)

    i = state.index(1)
    a, b = state[i+1:i+3]
    result = a * b

    print(result)
