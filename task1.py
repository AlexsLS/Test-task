def circular_path_verbose(n, m):
    arr = list(range(1, n + 1))
    print(f"\nКруговой массив (n={n}): {''.join(str(x) for x in arr)}")
    intervals = []
    path = []
    pos = 0
    while True:
        interval = []
        for i in range(m):
            interval.append(arr[(pos + i) % n])
        intervals.append(interval)
        path.append(arr[pos])
        end_pos = (pos + m - 1) % n
        if arr[end_pos] == 1:
            break
        pos = end_pos
    print("Интервалы:")
    for inter in intervals:
        print("".join(str(x) for x in inter))
    path_str = "".join(str(x) for x in path)
    print("Путь:", path_str)
    return path_str
print("Введите параметры для первого массива:")
n1 = int(input("n1: "))
m1 = int(input("m1: "))
print("\nВведите параметры для второго массива:")
n2 = int(input("n2: "))
m2 = int(input("m2: "))
print("\n---Результаты---")
path1 = circular_path_verbose(n1, m1)
path2 = circular_path_verbose(n2, m2)
print("\nОбщий путь:", path1 + path2)
