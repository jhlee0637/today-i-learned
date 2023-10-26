# 알파폴드1
[알파폴드 리뷰와 해석](https://taehojo.github.io/alphafold/alphafold1.html)
- [Multiple Sequence Alignment(MSA, 다중서열정렬)](http://www.incodom.kr/Multiple_alignment) 데이터를 준비
- Deep Learning 알고리즘 중 Convolutional Neural Network(CNN) 알고리즘을 이용
	- 데이터에 대한 Distance Map을 이용
	- Distance Map이란 실제 단백질의 3차원 구조에 기반하여 아미노산 서열들 사이의 거리를 표현한 이미지
	- 실제 이미지를 기반으로 알고리즘을 학습시킴
- Gradient descent(경사하강법)을 통하여 실제 이미지와 예측된 이미지의 오차를 조절
# 알파폴드2
[알파폴드2 모델 분석](https://taehojo.github.io/alphafold/alphafold2.html)
[알파폴드 2 작동원리 / alphafodl2](https://blog.naver.com/economic_moat/222506288911)
[Alphafold2 논문 리뷰2 - 입력부분](https://happyhaelee.tistory.com/98)
[Alphafold2 논문리뷰3 Evoformer -  MSA representation](https://happyhaelee.tistory.com/97)
- Evoformer에 넣기 위한 두 개의 representation 준비
	- 알파폴드1과 유사하게 MSA representation을 먼저 준비함
	- 거기에 DB에서 검색된 query sequence와 유사한 sequence를 가진 단백질 template를 활용, template 구조를 pair representation으로 통합하여 준비함
- Evoformer
	- Deep transformer-like Network를 적용함
	- MSA representation과 Pair representation의 정보가 서로 교환되면서 개선
- Structure module
	- 개선된 두 개의 representation은 아직 3차원 단백질 구조가 아니라 2차원의 데이터임.
	- 단백질의 모든 잔기각 동일한 지점에서 동일한 방향성을 갖고 있다고 설정함(블랙홀 초기화)
	- Invariant Point Attention(IPA) 연산과 sequence representation을 이용하여 residue gas를 반복적으로 개선함. 
	- Resnet을 추가하여 side chain의 모든 원자에 대한 비틀림 각도를 예측하여 3차원 좌표로 만듦
# 로제타폴드
[구글 인력·컴퓨팅 없이 알파폴드2 재현한 로제타폴드, 어떻게 가능했나?...연구 주도한 백민경 박사 발표 내용](http://www.aitimes.com/news/articleView.html?idxno=140110)
- CNN이 아닌 트랜스포머(Transformer) 일종인 어텐션(Attention)을 도입 
- "CNN에서는 바로 옆 픽셀만이 중요한 정보를 담기에 여기에 비중을 둔다. 반면 단백질 구조 파악을 위해서는 멀리 떨어진 곳의 정보도 필요하다."
- 어텐션을 활용하면 전체 투입정보(input)를 보고 연관도에 따라 정보를 가져오는 양을 조절.
- “중간 과정에서부터 3차원 구조를 만들어가면서 서열정보와 2D 이미지 상호작용 정보를 업데이트했다. 단백질 서열과 구조 정보 간 타이트한 커넥션을 학습했다”
  즉, 성능 개선을 위한 결단으로 1, 2, 3차원 정보 간 연결을 강화한 것이다. 로제타폴드 이름인 ‘RoseTTA(Three-Track Attention)’도 여기에서 나왔다. 
- 단백질 구조 예측 관련 학계 전체적으로 주목하는 주제는 cryoEM 데이터 활용을 통한 단백질 멀티스테이트 구조 예측이다.  

[Alphafold2와 RoseTTA fold – 단백질 구조 예측](https://blog.ksaidev.com/alphafole2%EC%99%80-rosetta-fold-%EB%8B%A8%EB%B0%B1%EC%A7%88-%EA%B5%AC%EC%A1%B0-%EC%98%88%EC%B8%A1/)
