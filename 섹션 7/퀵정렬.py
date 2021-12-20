def Qsort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[rt], arr[pos] = arr[pos], arr[rt]
        Qsort(lt, pos-1)
        Qsort(pos +1, rt)




if __name__ == "__main__":
    arr = [23, 11, 45, 36, 15, 67, 33, 21]
    print("Before Sort : ", end='')
    print(arr)

    Qsort(0, 7)
    print()

    print("After sort : ", end='')
    print(arr)