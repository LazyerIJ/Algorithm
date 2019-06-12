"""bj_1149.py

https://www.acmicpc.net/problem/1149
"""
def get_min_price(num, prices):
    """get_min_price

    :param housenum:house count
    :param prices:prices(red, blue, yellow) at each count
    """
    min_prices = list([prices.pop(0)])
    for idx, (r,g,b) in enumerate(prices):
        idx = idx + 1
        min_r = r + min(min_prices[idx-1][1], min_prices[idx-1][2])
        min_g = g + min(min_prices[idx-1][0], min_prices[idx-1][2])
        min_b = b + min(min_prices[idx-1][0], min_prices[idx-1][1])
        min_prices.append([min_r, min_g, min_b])

    return min(min_prices[-1])

if __name__ == '__main__':
    COLOR_PRICES = []
    HOUSENUM = int(input())
    for house in range(HOUSENUM):
        str_to_int = map(int, input().split(" "))
        COLOR_PRICES.append(list(str_to_int))
    print(get_min_price(HOUSENUM, COLOR_PRICES))
