print("Hello, World!")

for k in range(1, 1001):
    while k < 1001:
        while k < 100:
            while k < 10:
                if k ** 1 == k:
                    print(k, end=',')
                k += 1
                break
            if k == ((k % 10) ** 2) + ((k // 10) ** 2):
                print(k, end=',')
            k += 1
            break
        if k == ((k % 100) ** 3 + (k // 100) ** 3) + ((k - k // 100 - k % 100) / 10 ** 3):
            print(k, end=',')
        k += 1
        break
