def ave(li):
    ave_ = sum(li) / len(li)
    return ave_


def median(li):
    sorted(li)
    if len(li) % 2 == 0:
        item1, item2 = len(li) / 2, (len(li) / 2) + 1
        l = [item1, item2]
        median_ = ave(l)
        return median_
    else:
        median_ = (len(li) // 2) + 1
        return median_


def standard_deviation(li):
    n = len(li)
    x = 0
    for i in range(len(li)):
        x += ((ave(li) - li[i]) ** 2)

    return (x * (1 / (n - 1))) ** (1 / 2)
