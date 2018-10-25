for i in range(int(input())):
    P = int(input())
    places = []
    for j in range(P):
        places.append(len(input().split()))
    best = min(places)
    results = []
    for k in range(places.count(best)):
        results.append(places.index(best))
        places[results[-1]] = 0
        results[-1] += 1
    print(*results)
    try:
        input()
    except:
        exit(0) 