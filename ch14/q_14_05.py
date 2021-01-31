import collections

k = int(input())

d = [float('inf')]*k
q = collections.deque()
q.append(1)
d[1] = 0
while q:
    cur = q.popleft()
    nxt1 = (cur+1)%k
    nxt2 = (cur*10)%k
    if d[cur]+1 < d[nxt1]:
        d[nxt1] = d[cur]+1
        q.append(nxt1)
    if d[cur] < d[nxt2]:
        d[nxt2] = d[cur]
        q.appendleft(nxt2)
print(d[0]+1) 

#=> https://atcoder.jp/contests/arc084/submissions/19833409