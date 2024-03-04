import time
import math
def squareroot(num, ms):
    sec = ms / 1000
    time.sleep(sec)
    return math.sqrt(num)
num=int(input())
ms=int(input())
result = squareroot(num,ms)
print(f"Square root of {num} after {ms} milliseconds is {result}")
