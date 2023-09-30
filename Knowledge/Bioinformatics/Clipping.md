# Clipping
- Clipping이란 sequencing을 통해 얻은 read의 앞 부분과 뒷 부분의 정확도가 떨어지기 때문에, 이를 [[Alignment]] 단계에서 생략하고 정확도가 높은 중간 부분만 alingment에 활용하는 기술이다.
- 예를 들어 1000 base 길이의 read를 얻었다고 했을 때, aligment 과정에 clipping 옵션이 활용되면 1000 base 중 중간의 700 base만 alignment에 활용될 것이다.
- 장점은 정확도가 높은 부분만 alignment 과정에 활용한다는 점이다.
	- 이를 통해 low-quality base call이 많은 데이터도 alignment 정확도를 높일 수 있다.
- Clipping의 종류는 Soft Clipping과 Hard Clipping 두 종류가 있다.
# Soft Clipping

# Hard Clipping

#Soft_Clipping #Hard_Clipping
# 참조
- https://medium.com/@lwy730050619/soft-clipping-vs-hard-clipping-in-read-alignment-bd0c96f47426