[Picard M, Scott-Boyer MP, Bodein A, Périn O, Droit A. Integration strategies of multi-omics data for machine learning analysis. Comput Struct Biotechnol J. 2021 Jun 22;19:3735-3746. doi: 10.1016/j.csbj.2021.06.030. PMID: 34285775; PMCID: PMC8258788.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8258788/)
- 2021년 기준으로 mult-omics data integration 방법을 5가지로 분류함
	- early
	- mixed
	- intermediate
	- late
	- hierarchical
<img src="https://ars.els-cdn.com/content/image/1-s2.0-S2001037021002683-ga1_lrg.jpg" width=800>

# 1. introduction
### 왜 multi-omics 연구가 필요할까?
- 맞춤의학, 정밀의료의 부상
	- 개인의 임상데이터를 통해 진단하고 적절한 치료법을 제시
	- 임상데이터로 genomics, epigenomics, trasncriptiomics, proteomics, metabolomics 같은 데이터를 수집함
	- 과거에는 이러한 각각의 omics 데이터를 따로 관찰해서 진단에 활용하려고 했음
	- 그러나 대부분의 질병은 omics 데이터들을 서로 관통하면서 연결되어있음
	- 따라서 여러 omics 데이터를 합쳐서 통합적인 관점으로 보는 multi-omics 연구가 필요함
### Multi-omics 연구의 장단점은?
- 한 omics 데이터에서 부족한 부분을 다른 omics 데이터를 참고하여 메꾼다던가, 하나의 큰 시스템에 대한 그림을 얻어낸다던가 하는 장점이 있다.
- 그러나 적은 샘플에서 가져온 데이터만 있다는 점이나, 개개의 생물학 데이터가 갖고있는 오류를 넘어서서 데이터를 합쳐야 한다는 어려움들이 단점으로 남는다.
	- 특히 multiomics 연구에서 데이터를 합치는(integration) 작업이 정확하게 이루어지지 않으면, 오류 투성이로 합쳐진 데이터집합에서 결과를 제대로 얻는 것은 불가능하다.
### Data integration
- [Zitnik et al. (2019)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6242341/)은 integration의 방법을 크게 두 가지로 분류하였다.
	- Horizontal inegration: 동일 omics 여러 샘플
	- Vertical integration: 여러 omics 동일 샘플
- 이번 리뷰에서는 Vertical integration을 위주로 리뷰할 것이다.
		- Vertical integration의 방법을 수학적인 관점에서 bayesian, network-based, deep learning-based, kernel-based, matrix factorization-based로 나눠서 볼 것이다.
	- 또한 [Ritchie et al.(2015)](https://pubmed.ncbi.nlm.nih.gov/25582081/)의 분류방법에 따라 vertical integration(논문에서는 meta-dimensinal)을 concatenation-based, transformation-based, model-based로 나눠서 볼 것이다.
# 2. Challenges
- 생물학 데이터는 필연적으로 오류를 동반하고 있는데, 이렇게 깨끗하지 못한 여러 omics 데이터를 종합하여 특정한 패턴을 관찰한다는 것은 쉽지 않다.
- 또한 multi-omics 연구의 특성상 적은 샘플에서 많은 feature를 관찰해야 하는데, 이는 machine learing에서 가장 이상적이지 못한 상황으로 차원의 저주(the curse of dimensionality)라고 불리운다.
	- 이런 상황에서 ML을 통해 데이터를 훈련시키면 overfit된다.
- 생물학 omics 데이터들이 각각 너무 성격이 다르다는 점도 하나의 문제이다.
	- 유전자 발현 데이터의 경우 수만개의 variable이 있을 수 있지만, 대사물질 데이터는 기껏해서 몇천일 수가 있다.
	- 이렇게 서로 다른 데이터들 사이의 수, 종류, 연속성, 등의 차이를 극복하고 데이터들을 잘 integration 해야한다는 어려움이 있다.
- 데이터 간의 class imbalance 또한 ML 훈려에 악영향을 미친다.
	- 데이터에서 특정 class의 데이터만 기하급수적으로 많다면, 이를 바탕으로 훈련시키는 것이 부적절하다.
	- 왜냐하면 ML 훈련은 모든 class의 데이터 량이 엇비슷하다고 가정하고 훈련되기 때문이다.
	- 이를 해결하기 위한 방법으로 sampling, cost-sensitive learning과 같은 방법이 존재한다.
- Missing data 문제의 경우 해당 샘플을 지워버린다던가 혹은 Random Forest, K-Nearest Neighbor같은 방법이 있다.
# 3. Main integration strategies
### Integration 5가지 소개
- **Early integration**이란, 데이터들의 복잡도를 낮추지 않고, 단순히 둘 이상의 데이터들을 합친 뒤(wise concatenation) 그 결과물인 matrix를 ML모델에 넣는 것이다.
	- 현실적으로는 단순하게 합쳐진 데이터는 여전히 복잡하기 때문에 ML모델이 잘 돌아가지 않는다다
- **Mixed integration**이란 데이터들의 복잡도를 개별적으로 낮춰서 사용하는 것이다.
- **Intermediate integration**이란 여러 데이터들의 복잡도를 함께 낮춰서 사용하는 것이다.
- **Late integration**이란 정반대로 데이터를 합치지 않고 각각의 omics 데이터를 개별적으로 분석하는 것이다.
- **Hierarchical integration**이란 DNA-RNA-단백질로 이루어지는 시스템을 표현한 central dogma에 입각해서 omics 데이터 간의 조절 관계를 반영하여 합치는 것이다.
## 3.1 Dimensionality reduction for multi-omic integration
**Dimensionality reduction은 왜 필요할까?**
- Multi-omics 연구에 있어서 샘플들이 너무 많은 variable을 가질 경우 machine learning 기술 적용에 차질을 빚는다. 따라서 variable의 수를 줄여서 차원의 축소와 데이터셋의 noise 감소를 유도한다.
- 차원축소는 필수적이지는 않고, 위에서 얘기했던 5가지의 integration 방법에 모두 적용이 가능하다.
	- 다만 early integration와 intermediate integration의 경우 차원축소를 미리 적용하는 것이 정확도 향상에 기여한다.
- 차원축소를 위한 방법은 크게 두 가지가 있다:
	- Feature selection
	- Redundant varaibles and feature extraction
### 3.1.1. Feature Selection(FS)
- Feature를 줄이는 작업
- 그 결과 데이터의 복잡도, noise가 줄어들어서 데이터가 깔끔해진다.
- 데이터가 깔끔해지니까, ML 모델이 overfitting될 위험도 적어진다.
- 데이터가 깔끔해져서 해석하기도 편해진다.
- 너무 많은 variable이 삭제될 경우?
	- 데이터셋 사이에 feautre의 수가 다르면 좋지 않다
	- Feature Selection은 각 omics block이 동일한 수의 feature를 가지도록 할 수 있다
- Feature Selection은 세 가지로 나뉜다:
	- Filter-based Feature Selection
	- Wrapper-based Feature Selection
	- Embedded Feature Selection
### Filter-based Feature Selection
- ML 모델과 상관없이 적용 가능
- Feature 수를 줄일 수 있는 방향으로 관련된 variable을 추려내는 통계학적인 분석방법임
- **CFS, RCA** 같이 correlation 방법을 사용하거나,
- **ReliefF** 같이 distance 방법을 사용하거나,
- **mRMR** 같이 information gain 방법을 사용함
### Wrapper-based Feature Selection
- 서로 다른 feature 그룹을 사용하여 반복적으로 ML 모델을 학습시킨다.
- 이를 통해 모델의 전체 품질을 향상시키는 특성들을 선택한다.
- Recursive Feature Selection이 한 가지 예시이다.
	- 먼저 전체 variable을 대상으로 모델을 학습시킨다.
	- 그 다음 모델 퍼포먼스에 기여도가 떨어지는 variable을 차례대로 제거해간다.
	- 어느 ML 모델에나 적용 가능하다는 장점이 있지만, 데이터셋이 크다면 컴퓨터 성능에 따라 시간이 오래 걸린다는 단점이 있다.
### Embedded Feature Selection
- Classifier 모델 안에 feature selection 알고리즘이 넣어져있는 경우
- Tree-based feature selection과 regularization 방법이 있다.
	- Regularization 방법은 loss function과 penalization funtion을 결합한 방법이다.
		- Loss funtion은 모델이 주어진 데이터에 얼마나 잘 맞는지 확인하는 함수다
		- Penalization funtion은 복잡도(complexity)에 대하여 페널티를 부가하는 방식으로 feature 수를 적은 쪽으로 유도한