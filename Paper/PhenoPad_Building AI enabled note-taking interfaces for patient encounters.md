[Wang, J., Yang, J., Zhang, H. _et al._ PhenoPad: Building AI enabled note-taking interfaces for patient encounters. _npj Digit. Med._ **5**, 12 (2022). https://doi.org/10.1038/s41746-021-00555-9](https://www.nature.com/articles/s41746-021-00555-9#citeas)
# Abstract
- http://phenopad.ccm.sickkids.ca:8888/
- https://github.com/data-team-uhn/PhenoPad-UWP
- 음성, 자연어 처리, 필기인식 등의 AI 기술들을 활용하여 환자 중심의 임상 레포트 작성 앱을 개발.
- 수기와 음성으로 녹음된 내용을 디지털화하는 작업의 번거로움을 해결.
# Method
## Development of PhenoPad: System architecture
<img src="https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41746-021-00555-9/MediaObjects/41746_2021_555_Fig1_HTML.png?as=webp" width=800>

1. 임상학자가 수기로 PhenoPad에 메모를 작성한다.
2. 임상학자가 음성으로 메모를 작성한다.
3. 클라우드 서버 내 AI를 통해 메모를 분석하고 정보를 생성한다.
## Development of PhenoPad: Implementation of data analysis pipeline
- 음성인식
- 화자분리(Speaker Diarization)
	- VoxCeleb2 데이터셋을 이용하여 6000명의 음성에 대한 훈련을 시행
	- Embedding model은 [[LSTM]] recurrent network에 기반하여 훈련
		- Speech segment가 고정된 차원의 embedding space에서 map되도록 함
		- 이 embedding space에서는 동일한 화자 사이의 segment 위치가 가깝도록 위치하여 서로 다른 화자를 분리할 수 있게 한다.
- 의학용어 추출
	- [Neural Concept Recognizer(NCR)](https://ncr.ccm.sickkids.ca/curr/)을 이용하여 메모와 음성에서 의학용어를 추출
- 약어 명료화(Abbreviation disambiguation)
- 임상결정 지원
	- [PhenoTips](https://phenotips.com/)의 임상결정 지원 방법을 이용