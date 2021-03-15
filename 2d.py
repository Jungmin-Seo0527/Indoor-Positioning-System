import queue as Q
import sys
 
input = sys.stdin.readline
 
# n, m = map(int, input().split())
start = int(input())
n = 7
# adj = [[] for i in range (n+1)]
DIST = [1e9]*(n+1) # 최초 거리
m = [[] for i in range (n+1)]
exit_stie = [1,4,7] # 가장 가까운 탈출구
adj = [
    [],
     [[2, 1]],  # 1번의 (목적지, weight)를 딕셔너리로 넣어줘야함
     [[1,1], [3,1],],  # 2번의
     [[4,1], [2,1],], # 3번
     [[5,1],[3,1],], 
     [[6,1],[4,1],],
     [[7,1],[5,1],], 
     [[6,1],], 
    ]


# start 정점에서 가장 까까운 노드를 알려주는 함수
def get_Minimum_Voltex():
    size = len(exit_stie)
    minimum = exit_stie[0] # 첫번째 탈출구의 비용을 미니멈에 넣음.
    for i in range(1,size):
        if DIST[minimum] > DIST[exit_stie[i]]:
            minimum = exit_stie[i]
    return minimum

# 모든경로의 최단경로를 알려주는 함수.
def dijkstra(src):
 
    q = Q.PriorityQueue()
    q.put((0, src))
    DIST[src]=0
    m[src] = [0,-1]

    while not q.empty():
        pp = q.get() # pop과 동시에 
        here = pp[1] # 현재 위치
        dist = pp[0] # 현재 비용
        
        
        if DIST[here] < dist:
            continue

        for i in adj[here]:  # i[0] -> 다음목적의 노드 i[1] -> 다음목적지의 비용
            cost = dist + i[1] 
            if DIST[i[0]] > cost:
                DIST[i[0]] = cost
                q.put((cost, i[0]))
                m[i[0]] = [DIST[i[0]],here]
 
 
dijkstra(start)
print("가장 가까운 노드 : ",end='')
node = get_Minimum_Voltex()
print(node)

for i in range (1,n+1):
    if DIST[i] is 1e9:
        print("INF")
    else:
        print(DIST[i])


print('way')

print(m)
for i in range(1,n+1):
    if DIST[i] != 1e9:
        st = []
        n = m[i][1]
        st.append(i)
        while n != -1 :
            st.append(n)
            n = m[n][1]
        size = len(st)
        if size > 1:
            print(st[size-2:size-1])
        else:
            print('탈출구')
