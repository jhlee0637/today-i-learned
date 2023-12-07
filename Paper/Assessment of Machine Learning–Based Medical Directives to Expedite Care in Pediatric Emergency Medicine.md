[Singh D, Nagaraj S, Mashouri P, Drysdale E, Fischer J, Goldenberg A, Brudno M. Assessment of Machine Learning-Based Medical Directives to Expedite Care in Pediatric Emergency Medicine. JAMA Netw Open. 2022 Mar 1;5(3):e222599. doi: 10.1001/jamanetworkopen.2022.2599. PMID: 35294539; PMCID: PMC8928004.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8928004/)
# Overcrowding in emergency departments (EDs)
- 응급실 과밀화
- 응급실이 과밀화될 경우 의료전문가(Health Care Practitioner, HCP)들은 긴급하지 않은 환자들에 대한 정밀한 진단을 위하여 여러 검사실로 환자들을 보낸다.
- 환자들은 검사실-응급실을 돌아다니며 체류시간이 늘어나고, 응급실 과밀화로 이어지게 된다.

# Nursing Medical Directives
- 응급실 과밀화를 해소하기 위한 방안 중 하나로, 의사가 아닌 간호사가 지침에 따라 환자들을 평가하여, 의료전문가들에 앞서서 환자들을 선별한다.
- 그러나 이러한 지침은 성인환자를 중심으로 작성되어 아동환자에게 적합하지 않다는 단점을 가진다.
- 또한 이 지침은 사람의 판단에 의거하기 때문에 전산회된 workflow에 비해 비효율적이라는 점을 보여왔다.
# Machine Learning (ML)–Based Medical Directives (MLMDs)
- 연구진은 이 문제를 해결하기 위해 머신러닝 기반의 자동화된 의료지침서를 개발하였다.
- 이를 통해 응급실 내 과밀화를 막고 전통적인 의료지침의 한계를 극복할 수 있으리라 기대한다.
- MLMDs는 환자를 평가하고 의료전문가(HCP)에 앞서서 필요한 검사들과 진단결과를 평가한다.
<img src="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8928004/bin/jamanetwopen-e222599-g001.jpg" width=800>
_Approach to Autonomously Ordering Tests in an Emergency Department (ED) Using Machine Learning Medical Directives (MLMDs)_

# Method
## Data Selection
- 토론토 소아과병원 SickKIds 응급실의 77,219명의 기록을 활용
	- Training 55%
	- Validation 15%
	- Held-out Test 30%
- [[Time Series]]로 데이터를 정렬하여 모델 훈련 및 평가에 사용함
	- 이는 응급실 내에서 진단의 과정이 시간 순차적으로 일어나기 때문
	- 22.3% 이상의 환자들이 한번 이상이라도 받은 검사들을 case로 포함시켜서 모델을 생성했다.
- Model Input Features
	- heart rate, respiratory rate, oxygen saturation, blood pressure, body temperature, patient weight and age, presenting symptoms, Canadian Triage and Acuity Scale score, date and time of triage, preferred language, distance from hospital to home address, and free-text triage notes
	- 응급환자 분류표(triage note)
		- Python QucikUMLS18 module을 활용하여 코드를 추출한 뒤 활용
	- 총 6513개의 model features를 이용 
## Model Training
- [[Logistic Regression]]
	- [[Ridge Regularization]] penalty를 사용
- [[Random Forest]]
	- [[Random Grid Search]]를 사용
	- 훈련데이터에 대한 5-fold cross validation을 통해 적합한 parameters 선
- [[Neural Network]]
	- Fully connected feed forward deep artificial neural network (NN) models
		- 5개의 레이어를 사용
		- 4개의 레이어는 Rectified Linear Unit([[ReLU]]) 활성화 함수를 사용
		- 1개의 레이어는 Sigmoid 활성화 함수를 사용
	- Stochastic Gradient Descent를 활용하여 최적화
	- Learning rate $10^{-4}$
	- Weight decay $10^{-6}$
	- Momentum 0.9
	- [[Ridge Regularization]] 사용하여 훈련
## Model Evaluation
- Area Under the Receiver Operator Curve ([[AUROC]]) 평가기법을 활용하였다.
- 최종 output은 두 가지 요소를 반영했다.
	1. 진단이 존재하는가?
	2. 의료전문가가 관련된 검사를 요청했나?
	- 이는 실제 의료전문가들이 negative 진단결과도 적극적으로 활용한다는 점을 고려했기 때문이다.
- Decision threshold
	- False Positive의 수를 제한하고, 높은 PPVs 값을 얻기 위해 결정임계값을 설정
## Model Explainability
- Shapley Additive Explanations([[SHAP]]) 값을 활용하여, 각 feature가 model을 구성하는데 얼마나 영향력을 끼쳤는지 정량했다.
- 이를 통해 임상진단과 모델의 진단이 얼마나 일맥상통하는지 확인해볼 수 있었다.
## Statistical Analysis
- 성별에 따른 편향성을 조사하기 위해 [[Pearson χ2 test]]를 통해 성별과 나이에 따른 통계를 조사했다.