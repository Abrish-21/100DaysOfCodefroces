def minWidth(arr, height):
    width = 0
    for i in arr:
        if i <= height:
            width +=1
        else:
            width += 2
    return width
friends, height = map(int, input().split())
arr = list(map(int, input().split()))
print(minWidth(arr,height))