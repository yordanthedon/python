# 1. входни данни -> цяло число n
n = int(input())

# всички числа от 1111 до 9999

for thousand in range(1, 10):  # хилядни
    for hundred in range(1, 10):  # стотици
        for ten in range(1, 10):  # десетици
            for unit in range(1, 10):  # единици
                # проверка дали е специално
                # 1. хилядните са делител на n
                # 2. стотици са делител на n
                # 3. десетици са делител на n
                # 4. единици са делите на n
                if n % thousand == 0 and n % hundred == 0 and n % ten == 0 and n % unit == 0:
                    print(f"{thousand}{hundred}{ten}{unit}", end=' ')