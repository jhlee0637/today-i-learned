https://academic.oup.com/bioinformatics/article/39/2/btad021/6986971
- Review 논문
- Omcis data에 maching learning(ML) 기술이 필요한 이유는?
	- Data set의 크기가 크다
	- 이 큰 data set을 전부 인간이 일일이 정리하고 통합적인 관점에서 분석하는 것은 무리다
- 현재(2023년 초)까지 생물학에서 ML을 이용하여 여러 논문이 발표되었다.
	- Cancer Cell LIne Encyclopedia
	- Microbiome research
- ML이 이상적으로 작동하기 위해서는 대량에 샘플에서 적은 수의 feature들을 뽑아내 모델을 훈련시켜야 한다.
	- Omic data의 문제는 한 샘플에서 feature가 너무 많다는 것이다.
		- 예를 들어 종양샘플을 RNAseq한 데이터를 사용하려고 할 때, 20,000개에 달하는 유전자를 모두 feature로 잡아버리게 된. 단 하나의 샘플인데!
	- 물론 이렇게 여러 feature들을 한꺼번에 봐서 통합적인 관점에서 보는 것이 omic 분석의 핵심이다.
	- 하지만 여전히 살펴봐야하는 feature들이 너무 많은데 샘플 수는 이에 미치지 못한다는 점, 그렇게 때문에 효과적인 ML 훈련 및 모델 생성이 어렵다는 점이 난관이다.
- 해당 리뷰는 scoping review의 방식으로 리뷰를 진행했다.
	- 따라서 다른 연구자들의 방식이 더 효과적이었는지, 가장 좋은 방법이 무엇인지 비교하지 않음
	- 다른 연구자들의 방식들을 나열하기만 함
# 1. What is multi-omic data in practice? 
## 1.1. Which types of -omics features made up the ‘data dimensions’? 
<img src="https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/bioinformatics/39/2/10.1093_bioinformatics_btad021/1/btad021f2.jpeg?Expires=1696441666&Signature=HTyf33ZsKx-RGcUitMwyt4gakbJa8~Ep6MUmpPWF4R2mExn-WwNEaB8-caE0IgTJVx0LxC1TF7qNnc98qsYSDULj~8-W56jQ-xzsR0X2hjlQJdLq7iBGSfE8HVLKzKBRxOaSD5LshIll0HqK4wEJjbZRBrLTbOrbpUfs9GPjmKT64Px8qA-yAEpR5tnm7lJbWa~p~sx3lZ~MH99dTqnD0MvqR1GlJM7KIQ-o3cfW-B5QYFR5ax~ZtyakaLOltkslnQt7e~h53gF-EW6MEssmjhCeBxDOFB40GPgHnhPxmgHvcbuEcq6JD3-ut6STfCKuEwm~uFOlK2zptSxAAgW01w__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA" width="800">    

*(a) Number of uses of each -omics category in the reviewed papers.*    
*(b) Number of -omics used per paper in the reviewed papers.*    
*(c) The number of appearances -omics pairs across papers.*     

- 사람들은 Omics 분석인 만큼 주로 4개 정도의 서로 다른 데이터들을 함께 분석했다.
- Transcriptomics를 포함하는 경우가 가장 많았고 그 뒤로 epigenomics, genomics 데이터를 쓰는 경우가 따랐다.
- TCGA database의 등장으로 이런 경향이 두드러진다고 생각했으나, TCGA DB를 참조하지 않는 논문들도 비슷한 조합의 경향을 따랐다.
## 1.2. How is the data structured: how many features versus samples?
- 위에서 말했듯이 omic data의 경우 샘플마다 살펴봐야하는 특성의 개수가 샘플의 수 보다 훨씬 많다.
- 각 논문들이 omics 분석엣 사용하는 특성의 수가 샘플의 수 보다 7~8배 정도 많았다.
	- 중간값으로 따졌을 때 특성의 수가 33,415이고 샘플의 수가 447
	- 평균값으로 따졌을 때 특성의 수가 73,996이 샘플의 수가 1767
- TCGA DB의 등장, omics 분석의 어려움의 특성 상 온라인 토론이 활발하다는 점에서 자연스럽게 데이터 공유가 많아졌다.
	- 이를 이점으로 삼아 다양한 ML 기술들이 테스트 되는 환경이 구축될 수 있었다.
# 2. What analysis has been done on multi-omics data? 
## 2.1. Which ML techniques were used?
- Data integration은 비단 omics data 뿐만 아니라 여러 상황에서 데이터들을 합쳐야 할 때 필요하다.
- Data integration을 위해서 machine learning이 사용되기도 하는데, bioinformatics와 관련없는 그룹들도 data integration을 수행한다.
- 그렇다면 일반적인 데이터 사이언스 연구자 그룹과 multiomics data를 연구하는 그룹 사이에서 data integration을 목적으로 사용하는 machine learning 기술에 차이가 있을까?
<img src="https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/bioinformatics/39/2/10.1093_bioinformatics_btad021/1/btad021f4.jpeg?Expires=1696441617&Signature=zk231bVQ1rG39cc1An3JJlaNOm0iJgRd-0cYURpp7dfFNwRN4UrGoXMeSMkHDC4qBK8urijWQDE1MO1Q32SVs3QXL38QPqRqQybMQCmx6-WpCaeKjqqUxgdq6VMHYPvaFUHgBFNqU2ji21T3OkGYn8k8JFY-Xy0hHWrhUM35TdcAcDyIwwj7z3RM0iFTQyj8tmTC3gbRzn2ZfnMI07r5Dx-WaUx7tcznIuMH-BgsgYqnS~jymyuqu0l3RLyXEVz4AEBN~Sdnnp5k3asOiVAaQGkBihn5s75S6UuFgGar6B2rdz1OqYnrCP~0OeGSeR8D0BIrSGQB6wOUVg~OyEXBUA__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA" width="800">    

*(a) Number of ML techniques being used more than once in the reviewed papers.*
*The publications on ‘machine learning AND multi-omics AND integration’ are plotted in green, while the publications on ‘machine learning AND integration’ are plotted in purple.*    
*Number in the reviewed multi-omics ML papers of ML goals (b) and labels used for classification (c)*

- Multiomics 그룹의 경우 Autoencoder, Cox PH 기술을 많이 이용했다.
- 반면에 일반 ML 그룹은 Random forest와 SVM 기술 사용에서 큰 차이를 보였다.
## 2.2. What were the goals of the ML application?
- Multiomics 그룹이 ML을 이용한 주 목적은 첫번째는 classification, 두번째는 dimensionality reduction이었다.
- Classfication을 통하여 질병을 subtype별로 분리하기, 환자의 생존 예측을 라벨(5년이상, 5년이하) 별로 분리하는 경우에 쓰였다.
	- 수명 문제에 관해서 얘기하자면, 정확하게 몇 년 남았다는 식으로 분류하는 경우 이는 회귀문제가 된다. 그러나 이 회귀문제를 기준을 정하고 구간을 나눠서 '이산화'(discretize)하여서, 몇가지 편의를 도모할 수 있다.
## 2.3 What were the targets/labels of classification tasks?
- Classification의 경우 환자의 생존 예측이 제일 많았다.
# 3. Can we explain trends using an analysis of the citation of papers since 2015?    
![](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/bioinformatics/39/2/10.1093_bioinformatics_btad021/1/m_btad021f5.jpeg?Expires=1695325471&Signature=Q8ufkAm9rlkrhHe8ZIXi9qTNWHJWP93HEEQU-n0enRc~jJ624LLlODN6P3jkuU2YT4yoou~-migr~noHI9hFtAkXYORhMdQ7feJFTTVxyXcmh5QMVQZPyG-mnTLYngXg-LvNdGueGBD73Vpuxh5356vl9DAlje12M6ZR-pOHyyoxRKNhcIYeSebvJKAX9Swpk9-VXMZvRRkuYjWzwwJB-Tb6x3k~aZG2S~NBPtCUYWSHByZ7OQPloeXS1Cz5u7yu~5UUnTNmSoTcjafCV9xKJ4dbFKpsAcBrxyNjbWrBZIckQo3TtHUg4uIF0OBFWVEs2DE1HzXsDEiVenPVIc17Gg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)    

*Number of citations per year, of papers published in different years*    

- 2018년 [Deep Learning-Based Multi-Omics Integration Robustly Predicts Survival in Liver Cancer](https://pubmed.ncbi.nlm.nih.gov/28982688/) 논문이 발표된 이후, multiomics 연구에서 ML 기술을 이용한 논문이 급격하게 늘어났다.
# 4. Discussion
<img src="https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/bioinformatics/39/2/10.1093_bioinformatics_btad021/1/btad021f6.jpeg?Expires=1696301496&Signature=4mKcdi8ADjARTc0jzXDH9FQ1VH8VF7URMK4ZzJXdzlAhK-~7oWZ-osXgX0tbdhS9QWEf3~UBhDlu7EN5P8XW56xhFot2-gESjIBqvcC14d8hgs8Fun~sn1S4GkK8Y-KbXevop20uPMG20kzE4Sf3UPtmyM4ZNRzhhKTNgH1wte2Lt8VP89NSfftjallHiwgyhUq79nrUpCrUsyVaKdWa0iIc0jnwPngSHA0rHUqNvTAM~NblAghzEMhOxA0Y6v4-s0vnZwrAIcS69yBDZjaVBQ--w1YXsORw72GDrK5PrHQ5VDOMfN6jtQI8KQnD3DtYzA-x-D42cod2V6d3bpbBEQ__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA" width="800">    

*Shapes in datasets. Features (*$P$*) Samples (*$n$*)*    
*(a) A dataset where* $n$ ≫ $P$*, the ideal ‘shape’ for many ML techniques.*    
*(b) In multi-omics analyses, researchers face very wide datasets, where* $n$ ≪ $P$.    
*(c) Feature selection and extraction are often used to reduce the number of features.*    
*In feature selection, a subset of the original features is kept. In feature extraction, features are merged and transformed into a smaller number of new ones*

- 다시 말하지만 샘플($n$)의 수가 feature($P$)의 수보다 많은 상황이 ML에서 가장 이상적이다. 하지만 Multiomics data는 정반대의 성향을 지닌다.
- 확인해야 하는 feature($P$)의 수가 엄청 많은 경우를 '높은 차원을 가진다'라고 표현하는데, 이때 발생하는 문제는 바로 희소(sparsity)이다. (혹은 sparse data라고 표현할 수도 있겠다.)
- 이러한 sparse data를 가지고 실제로 ML 모델을 훈련시키려고 하면 잘 안된다는 단점이 있다. 각 샘플의 feature을 ML모델이 제대로 잡아내지 못한다. 이를 차원의 저주(curse of dimensionality)라고 부른다.
- 그렇기 때문에 ML 연구에서는 이러한 sprase data에 대하여 여러가지 전략을 시도하여 모델 훈련이 잘 되도록 유도한다.
## 4.1 Reducing the number of features (P)
- Sparse data가 가진 차원의 저주 문제를 풀기 위한 시도 중 하나로는, feature($P$)의 수를 줄이려는 시도가 있다. (feature을 줄이는 것 만이 유일한 전략은 아니다.)
- feature를 줄이는 방법에도 여러가지가 있는데...
	- feature들 중에서도 ML 훈련에 사용하기 좋은 경향성이 뚜렷한 feature들만 **취사선택**하는 방법이라던가,
	- 알고리즘을 활용하여 여러 feature들을 **압축**하는 방법이라던가,
	- 혹은 위 두 가지를 아예 한꺼번에 적용하는 방법이 있다.
## 4.2 Feature selection
- 자신이 어떤 목적으로, 어떤 방향으로 ML 모델을 생성하고 싶은지 미리 알고 있고, 모델을 구성하는 요소에 대한 사전지식이 충분한 경우, 이러한 지식을 활용하여 모델을 최적화 할 수 있다.
- Omics 분석에서 생물학적으로 봤을 때 비교적 확률이 낮은 feature($P$)를 의도적으로 제거하면 ML 모델의 최적화에 큰 이득을 줄 수 있다.
	- 예를 들어, SNPs와 대사물질 7백만개로 이루어진 feature들을 65개의 feature로 줄인 [논문](http://ieeexplore.ieee.org/abstract/document/8416980/)이 있다. 논문에서는 feature를 줄이기 위하여 다양한 기준을 사용했는데, 그 중에는 대사물질 농도와 특별하게 연관성이 높은 SNPs만 차출하는 기준도 있었다. 
	- 일반적으로는 유전자들 중에서도 활성빈도(activity level)이 낮은 유전자를 걸러내는 식으로 feature selection이 이루어진다.
	- 후성유전체학 데이터의 경우에는 관련성 높은 유전자가 인접한 지역이나 여러 메틸화부위를 둘러싼 지역만 따로 고려하는 식으로 feature selection이 이루어진다.
- Omics 분석에서 Cox PH 모델(생존율 분석을 위한 모델)과 feature selection을 함께 사용하는 경우가 많이 보였다.
	- Cox PH 모델이란 선형회귀를 활용하여 특정 변수(약물, 유전자 등 수명에 영향을 끼칠 수 있는 것)에 의한 시간에 따른 생존율을 예측하는 모델이다.
	- Cox PH 모델은 일반적인 ML 연구에서는 인기가 없지만 multiomics 분석에서 전체에서 두 번째로 가장 많이 사용될 정도로 인기가 많았다.
		- 이는 TCGA database에서 생존율 데이터에 접근이 가능하다는 점과 multiomics data 분석에 feature selection이 필수불가결해지면서 채택빈도가 늘어난 것으로 보인다.
	- Feature selection을 통해 나온 결과들을 비교할 수 있기 때문에, 어느 변수(feature)들이 생존율에 더 영향력이 있는지 판가름하기 좋다.
	- 게다가 일부 생존율 데이터는 몇 가지 이유로 불완전한데(예를 들어 환자가 아직까지 생존 중이라 변수와의 관계가 계속해서 갱신 중이라던가, 혹은 임상데이터가 접근 불가능하게 바뀌었다던가...), Cox PH 모델의 경우 불완전한 데이터에 대해서도 적용이 가능하므로, feature selection을 통해 몇 안되는 불완전한 데이터(샘플 사이즈가 작다) 마저도 활용할 수 있다. 
## 4.3 Feature extraction
- Feature selection을 통해서 꽤 많은 feature($P$)들이 필터링됐을 것이라고 생각하지만, 대부분의 multiomics data의 경우 여전히 feature의 수가 sample에 비해 너무 많다.
- 이때 feature의 수를 더 줄이는 방법 중 하나가 feature extraction이다.
	- 이는 기존의 feature들을 연구자가 설정한 다른 feature로 압축하는 것을 의미한다.
	- 압축하는 과정에서 일부 feature들과 관련성이 떨어지는 것을 감안해야 한다. 
- Feature extraction가 사용되는 예시는 여러가지가 있는데, Principal component analysis (PCA)와 Autoencoder가 있다.
	- PCA의 경우 기존의 feature들을 최대한 많이 정확하게 설명할 수 있으면서도 차원이 한 단계 낮춘 plot을 그린다.
	- Autoencoder는 neural networks다.
		- Autoencoder는 여러 layer로 이루어진 데이터들을 input으로 받는데, 이 중 가장 작은 bottleneck을 가진 layer에서 feature를 뽑아내서 기준으로 잡는다.
		-  Autoencoder는 Cox PH와 마찬가지로 일반적인 ML연구 그룹보다는 multiomics연구 그룹에서 사용하는 빈도가 훨씬 높았다.
## 4.4 Increasing the number of samples (_n_)
- 위에서는 feature($P$)를 줄이는 방법에 대해서 고민했다.
- 그치만 샘플($n$)의 수를 늘리는 것 또한 omic 데이터가 가진 문제를 해결하는 전략 중 하나일 수 있다.
- 많은 omic 연구 그룹이 TCGA와 같은 public multiomics DB에서 얻은 데이터를 활용(혹은 의지)했다..
	- TCGA는 10,000개가 넘는 샘플과 33개의 암종류에 대한 데이터를 보유하고 있다.([2015](https://pubmed.ncbi.nlm.nih.gov/25691825/))
	- TCGA의 데이터는 다루기도 쉽고 연구자의 목적에 따라서 필요한 자료만 가져와서 홀용할 수도 있다.
	- 다만 문제점은 TCGA는 암 데이터에 치중한 데이터들이라는 점이다.
		- 암은 물질대사가 제대로 조절되지 못하거나 대사경로의 신호전달이 고장났을 때 발생한다.
		- 이러한 환경에서 얻은 데이터를 암 외의 multiomics 분석에 적용하는 것은 문제가 있을 수 밖에 없다.
- 따라서 multiomics 분석에서 TCGA 데이터를 맹목적으로 활용하는 것은 지양해야할 것이다.
	- 다만 여전히 TCGA가 다른 DB들의 특징이나 경향성을 나타낼 수 있다는 점도 상기해야할 것이다.    
	  <img src="https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/bioinformatics/39/2/10.1093_bioinformatics_btad021/1/m_btad021f3.jpeg?Expires=1695325471&Signature=aNd-OCRNyN3BEK5KCwrPh2Tw0ZyRCc0~hfaIBtpkspZ~yo2A11UqjWm5UFBFfvU3OHckdoQyvZ5nEVmj3OpByWMpT7vt3jL6DeJgvc6dYSKcaH37bNMUX4lox8rKtufzuaL2Zu~yN-RSOftov0zpmaclDRXyPlEFbprSuCNO9sDo7e-W01apuAvTDZHNbeCsbCaTMYYCGm12S6JlVMEaWL~WBem4VsWgFidiZ52hWiCzpMKnaygXRal7KBzO4XKy4ntHi7zE64aP62RF3EWTB2pzqsSNgFxPpHTO~q~FFcyuV-9OtI5y3vGJuQoAfzdtDPb~Uf0nU1tGTBZ6wXuTTQ__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA" width=400>    
- multiomics 분석에서 샘플 수에 대해서 더 얘기하자면, 샘플 수가 무조건 많다고 분석에 활용이 가능한 것도 아니다.
	- omic 데이터를 모아놓고 봤더니 overlapping되는 부분이 없어서 다 활용하지 못하는 경우도 있다.
	- 실제로 [2018년 논문](https://www.frontiersin.org/articles/10.3389/fgene.2018.00477/full)에서는 copy number alteration과 gene expression 데이터에 대한 407개의 샘플을 모았으나, 두 항목이 모두 조사된 샘플을 190개 밖에 없어서 190개만 활용해서 분석한 경우가 있다.
## 4.5 After reshaping the data
- Autoencoder, Cox PH는 ML을 활용하여 multiomics 분석을 하는 bioinformatics 그룹들이 가장 많이 쓴 기술이었으며, 둘 다 feature extraction을 통한 차원축소를 통해 모델의 정확성을 높이고자 했다.
- 다른 기술들은 classification, clustering, regression, inferring networks와 같은 용도의 기술들이었다.
## 4.6 New ML developments of potential use in multi-omics
- 2017~2018년도 이후로 ML 기술에서 여러 발전이 있었지만 이에 대한 multiomics 분석에 적용은 아직 많이 진척되지 않았다.