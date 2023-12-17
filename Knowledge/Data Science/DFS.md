#Algorithm 
Depth First Search
- 분기가 발생했을 때, 한 분기를 **끝까지** 탐색한 다음 돌아와서 다른 분기를 탐색한다.
## DFS와 [[BFS]] 중에 어느 걸 사용해야할까?
1. 모든 node를 방문해야한다면
	- DFS, BFS 둘 다 좋다.
2. Node 방문 history를 기록해야한다면
	- DFS. 왜냐하면 BFS는 특정 node로 향하는 경로의 특징을 저장하지 못하기 때문.
3. 최단거리를 구해야 한다면
	- BFS


### 참조
- https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
- https://annyeongworld.tistory.com/83
- https://velog.io/@timointhebush/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-DFS-BFS-Python