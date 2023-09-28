Depth First Search
<img src="https://i.namu.wiki/i/4f5E6SdLh7iASwEmqm8JdfJLmR-VP-BgbvLCp6cduilcsn91F8pk2a1Czmk_SlEFmtB3eq0mHO5wtLnSVROICRBNfxeM1e0tiMYRF2LFk2Y.gif">
- 분기가 발생했을 때, 한 분기를 **끝까지** 탐색한 다음 돌아와서 다른 분기를 탐색한다.
## DFS와 BFS 중에 어느 걸 사용해야할까?
1. 모든 node를 방문해야한다면
	- DFS, BFS 둘 다 좋다.
2. Node 방문 history를 기록해야한다면
	- DFS. 왜냐하면 BFS는 특정 node로 향하는 경로의 특징을 저장하지 못하기 때문.
3. 최단거리를 구해야 한다면
	- BFS

## 알고리즘 구현


#Algorithm 
### 참조
- https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
- https://annyeongworld.tistory.com/83