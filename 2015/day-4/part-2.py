from hashlib import md5


def naturals():
    i = 1
    while True:
        yield i
        i += 1


def findZeros(base, numZeros):
    target = "0" * numZeros

    for i in naturals():
        numHash = md5((base + str(i)).encode())
        if numHash.hexdigest().startswith(target):
            return i


if __name__ == "__main__":
    example = "abcdef"
    base = "yzbqklnj"

    result = findZeros(base, 6)
    print(result)
