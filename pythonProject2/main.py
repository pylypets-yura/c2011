coin1 = int(input())
coin2 = int(input())
number = int(input())

if coin1 > coin2:
    c = number // coin1
else:
    c = number // coin2
for i in range(c):
    if coin1 > coin2:
        n = c * coin1
        x = n % coin1
        if x > 0:
            i += 1
            c -= 1
        elif x == 0:
            t = c * coin1
            b = number - t
            a = b % coin2
            if a > 0 or a < 0:
                i += 1
                c -= 1
            elif a == 0:
                q = b / coin2
                f= c + q
                print(c)
                print(q)
                print(f)
                break
    elif coin2 > coin1:
        n = c * coin2
        x = n % coin2
        if x > 0:
            i += 1
            c -= 1
        elif x == 0:
            t = c * coin2
            b = number - t
            a = b % coin1
            if a > 0 or a < 0:
                i += 1
                c -= 1
            elif a == 0:
                q = b / coin1
                f = c + q
                print(c)
                print(q)
                print(f)
                break
