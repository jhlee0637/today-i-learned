[Oxford Protein Informatics Group](https://www.blopig.com/blog/2023/09/current-strategies-to-predict-structures-of-multiple-protein-conformational-states/), 13 Sept 2023

- AlphaFold2(AF2)의 등장으로 대부분의 단백질 구조가 밝혀졌다고 판단되었다.
- 그러나 AF2는 단백질의 single structure만 예측하도록 훈련되었다.
- 단백질은 입체적인 구조([[Conformational Structure]])에 따라서 기능이 바뀌며, AF2는 이를 예측하지 못한다는 한계를 가진다.
- 이 글에서는 단백질의 입체구조를 예측하기 위해 활용되고 있는 bioinformatics 전략을 살펴볼 것이다.
## Adaption of AF2
- AF2의 알고리즘을 그대로 활용하되, 훈련에 사용되는 input 데이터를 바꾸는 방법.
- 