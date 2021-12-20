def DFS(v):
    if v > 7:
        return
    else:
        # 본연의 로직 수행
        print(v, end = " ")

        DFS(v*2)
        DFS(v*3)
        #위와 같이 본연의 록직을 수행하고 왼, 오를 호출하면 전위순회