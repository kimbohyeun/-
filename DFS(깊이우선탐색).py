def dfs (graph, v, visited):
  visited[v]= True #현재 노드방문처리
  print(v,end='')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited) #현재 노드와 연결된 노드를 재귀적으로 방문 (재귀=스택)
graph = [
  [],
  [2,3,8]
] #값
visited = [False]*9
dfs(graph,1,visited)
