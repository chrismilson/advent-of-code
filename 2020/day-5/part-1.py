if __name__ == "__main__":
    seatIDs = []

    with open('./boarding-passes.txt') as f:
        for code in f:
            seatID = int(
                ''.join(
                    '1' if c in 'BR' else '0'
                    for c in code.strip()
                ),
                base=2
            )
            # row, col = seatID >> 3, seatID & 7
            seatIDs.append(seatID)

    print(max(seatIDs))
