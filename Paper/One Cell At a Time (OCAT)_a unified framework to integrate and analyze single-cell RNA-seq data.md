[Wang, C.X., Zhang, L. & Wang, B. One Cell At a Time (OCAT): a unified framework to integrate and analyze single-cell RNA-seq data. _Genome Biol_ **23**, 102 (2022). https://doi.org/10.1186/s13059-022-02659-1](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02659-1)
- [[today-i-learned/Knowledge/Bioinformatics/scRNA-seq|scRNA-seq]] 연구에서, 서로 다른 데이터셋을 합쳐서 연구하면 [[Cell type]] 연구에 도움이 된다.
- 그러나 scRNA 데이터에서 발생하는 [[Batch Effect]]와 컴퓨터 자원의 소비문제 때문에 데이터셋을 합치는 것이 쉽지 않다.
- Batch Effect를 줄이기 위한 기존의 방법들은 어떤 문제점이 있었는가
	- Biological effect가 batch effect에게 orthogonal하게 발생한다는 가정에서 출발했는데, 이는 실제 현상과 다르다.
	- Mutual Nearest Neighbors{[[MNNs]]}를 이용한 시도의 경우 데이터가 커질수록 시간과 컴퓨터 자원을 많이 소비한다는 단점이 있다.
		- 차원축소를 통해 메모리소비를 줄이려고는 하지만, single cell의 크기가 커지면 다시 문제가 발생할 뿐이다.
	- [[Seurat]], [[Harmony]]와 같은 툴들은 각각 다른 방법으로 메모리소비율과 batch effect 제거라는 과제를 해결하려고 하지만, 여전히 데이터 크기가 절대적으로 커지면 소비가 늘어날 뿐이다.
- 연구팀은 OCAT라는 높은 메모리효율은 가지는 machine learning 기반의 방법을 소개한다.
	- 이 방법은 여러 scRNA-seq 데이터셋을 합칠 때 batch effect를 제거할 필요가 없다.
	- OCAT는 sparse encoding을 이용하여 서로 다른 scRNA-seq 데이터셋을 합친다.
	- OCAT는 다음과 같은 장점을 가진다.
		1. 각 데이터셋에서 가상의 "ghost" cell을 찾아내어 각 세포들 사이의 sparse bipartite graph를 생성한다.
			- "ghost" cell은 효율적인 시간수준(O(N))으로 최적화된 sparsified encoding 세포 데이터를 생성한다.
		2. 데이터셋의 세포들을 이 "ghost" cell과 연결시킨 다음, batch effect 수정이 필요한 세포와 그렇지 않은 세포들을 구별한다.
		3. OCAT sparse graph encoding은 cell feature representation으로 변환된다.
			- Cell feature representations는 기존에 잘 알려진 scRNA-seq 분석대상들로 differential gene expression analysis, trajectory inference, pseudotime inference, cell type inference 같은 연구에 활용할 수 있다.
# Result
## The OCAT framework overview
<img src="https://media.springernature.com/full/springer-static/image/art%3A10.1186%2Fs13059-022-02659-1/MediaObjects/13059_2022_2659_Fig1_HTML.png?as=webp" width=800>
_Schematic workflow of OCAT. When integrating multiple scRNA-seq datasets, OCAT first identifies “ghost” cells, centers of small cell neighborhoods, in each dataset. OCAT next constructs a bipartite graph connecting each cell to its most similar “ghost” cells. The edge weights connecting each cell’s closest “ghost” cells are treated as its OCAT sparse encoding. The OCAT sparse encoding can effectively correct the batch effect and facilitate various downstream analysis tasks, such as cell clustering, differential gene expression analysis, trajectory inference, and cell type inference_

- "Ghost" cell이란?
	- 이웃한 세포 사이의 중간 지점
	- K-means clustering 알고리즘을 통해 계산
	- Cluster label 없음
- OCAT가 그리는 bipartite graph
	- 데이터셋의 모든 single cell과 "ghost" cell 사이를 연결한다.
	- 유사도를 edge weight으로 활용해서 그린다.
	- 각 single cell에 대하여 가장 유사한 "ghost" cell하고만 연결시킨다.
	- Local Anchor Embedding([[LAE]]) 알고리즘을 활용하여 edge weight 최적화
- 어떻게 서로 다른 데이터셋의 single cell 데이터가 한 차원으로 묶이나?
	- "ghost" cell 사이의 message passing을 통해 세포 사이의 유사도를 확인
	- 이렇게 바뀐 weight이 각 세포들에 대한 spart encoding으로 작용함
- "ghost" cell의 숫자는 전체 유전자의 수보다 작다.
	- 따라서 OCAT의 [[Latent Representation]]은 매우 희소(sparse)하다.