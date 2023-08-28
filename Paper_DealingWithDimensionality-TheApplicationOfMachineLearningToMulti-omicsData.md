https://academic.oup.com/bioinformatics/article/39/2/btad021/6986971
- Review 논문
- Omcis data에 maching learning(ML) 기술이 필요한 이유는?
	- Data set의 크기가 크다
	- 이 큰 data set을 전부 인간이 일일이 정리하고 통합적인 관점에서 분석하는 것은 무리다
- 현재(2023년 초)까지 생물학에서 ML을 이용하여 여러 논문이 발표되었다.
	- Cancer Cell LIne Encyclopedia
	- Microbiome research
- ML이 이상적으로 작동하기 위해서는 대량에 샘플에서 적은 수의 특징들을 뽑아내 모델을 훈련시켜야 한다.
	- Omic data의 문제는 한 샘플에서 특징이 너무 많다는 것이다.
		- 예를 들어 종양샘플을 RNAseq한 데이터를 사용하려고 할 때, 20,000개에 달하는 유전자를 모두 특징으로 잡아버리게 된. 단 하나의 샘플인데!
	- 물론 이렇게 여러 특징들을 한꺼번에 봐서 통합적인 관점에서 보는 것이 omic 분석의 핵심이다.
	- 하지만 여전히 살펴봐야하는 특징들이 너무 많은데 샘플 수는 이에 미치지 못한다는 점, 그렇게 때문에 효과적인 ML 훈련 및 모델 생성이 어렵다는 점이 난관이다.
- 해당 리뷰는 scoping review의 방식으로 리뷰를 진행했다.
	- 따라서 다른 연구자들의 방식이 더 효과적이었는지, 가장 좋은 방법이 무엇인지 비교하지 않음
	- 다른 연구자들의 방식들을 나열하기만 함
# 1. What is multi-omic data in practice? 
## 1.1. Which types of -omics features made up the ‘data dimensions’? 
![](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/bioinformatics/39/2/10.1093_bioinformatics_btad021/1/m_btad021f2.jpeg?Expires=1695325471&Signature=S9uUAUwLQ4wlNymsFTWYZ-0qhUAt1CHHqHi0ZXIp8g2e6Bqgg6w2DVPInp~N9aVtPR5cyUqRcyUusDBFkcvkSoLXE6x2X7bUsTX9ZTVQHxH3IIds9emJPmT4PJUzG12Ksg4e3PZ5CWFggCE9LuD0RMURdMz4c7EOvNKcK7swCtWhkRN~Sf2X~Glnyam1iYsAknGp9fJcDQyGEpu7mlvG4ZgBLpMCOWQK8S9CRB~N7PMgKxkNx2VW3gqAnsfimdCDR3edFJQLTkq8s5uTWPX3MUw-NXnQNKMfZnh1WT4Q-oAczFMEQ7dIxM4NVuEGFWR5UYju~R0dWBcdLfSoR3ZvXg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)    
*(**a**) Number of uses of each -omics category in the reviewed papers.    
(**b**) Number of -omics used per paper in the reviewed papers.    
(**c**) The number of appearances -omics pairs across papers*     
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
## 2.1. 	Which ML techniques were used?
- Data integration은 비단 omics data 뿐만 아니라 여러 상황에서 데이터들을 합쳐야 할 때 필요하다.
- Data integration을 위해서 machine learning이 사용되기도 하는데, bioinformatics와 관련없는 그룹들도 data integration을 수행한다.
- 그렇다면 일반적인 데이터 사이언스 연구자 그룹과 multiomics data를 연구하는 그룹 사이에서 data integration을 목적으로 사용하는 machine learning 기술에 차이가 있을까?
![](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/bioinformatics/39/2/10.1093_bioinformatics_btad021/1/m_btad021f4.jpeg?Expires=1695325471&Signature=DoNbs3HY~Hdy9o4XZexDARs-uhdK5VIXYnekLl6e02so0K9P1BtWv5uW7SdwLtEvJ1rtKdx2saZJf6gy2qNBnIKKReTCGmmh6UqBAAsChAGfJQgPfRu0-82Hoh8Lor5tAXkQ1Pb1xn05G34MXw2e3tz1BqUKFI8F9T6iPgTmzR9JolZvAfltX1-ps~UkgCGFvD24gHLYI-4dNDkgGOAxS3tUC4PJEr2pXuLTQL~rhh6uzgZI3cdtwti5Xie8M48SC5ifJsl3ZgRqbNHoLL2foTI~mIQrtXUSlRWQzW~24OlnU0DMd0ndR2aYqXj6CKd0uhLy53hUIF~IbMKIPZwVGw__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)    
*(**a**) Number of ML techniques being used more than once in the reviewed papers. The publications on ‘machine learning AND multi-omics AND integration’ are plotted in green, while the publications on ‘machine learning AND integration’ are plotted in purple.    
Number in the reviewed multi-omics ML papers of ML goals (**b**) and labels used for classification (**c**)*
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