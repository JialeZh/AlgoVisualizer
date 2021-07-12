import time

def mergeSort(data, start, mid, end, drawData, timeTick):
    a = start
    b = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if a > mid:
            tempArray.append(data[b])
            b+=1
        elif b > end:
            tempArray.append(data[a])
            a+=1
        elif data[a] < data[b]:
            tempArray.append(data[a])
            a+=1
        else:
            tempArray.append(data[b])
            b+=1

    for a in range(len(tempArray)):
        data[start] = tempArray[a]
        start += 1

def merge(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge(data, start, mid, drawData, timeTick)
        merge(data, mid+1, end, drawData, timeTick)

        mergeSort(data, start, mid, end, drawData, timeTick)

        drawData(data, ['#BF01FB' if x >= start and x < mid else '#F7E806' if x == mid 
                        else '#4204CC' if x > mid and x <=end else '#0CA8F6' for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, ['#0CA8F6' for x in range(len(data))])
    
