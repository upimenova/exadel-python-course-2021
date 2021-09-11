for k in range(1, 1001):
    while k < 10:
        if k == k ** 1:
            print(k, end=',')
            break
        else:
            break
    while 10 <= k < 100:
        if k == ((k % 10) ** 2) + ((k // 10) ** 2):
            print(k, end=',')
            break
        else:
            break
    while 100 <= k < 1000:
        if k == ((k % 10) ** 3 + (k // 100) ** 3) + ((k - k // 100 * 100 - k % 10) / 10) ** 3:
            print(k, end=',')
            break
        else:
            break
