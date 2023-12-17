---
layout: post
title: "네이버AI 부스트캠프 Pre-course 01. Historial review"
subtitle: "Deep Learning 개요 및 historical review"
date: 2022-06-28
author: "Lee Je Hee"
URL: "/2022/06/28/NaverAIBoostCamp_PreCourse_01/"
published: False
tags:
 - AI
 - MachineLearning
 - DeepLearning
 - Naver
---
# What make you a good deep learner?
Deep learning을 잘 이용하는 사용자가 되기 위해서는 다음 세 가지 요소를 갖춰야 한다.

1. Implementation Skills: 툴을 이용하여 DL를 실제로 잘 구현해야 한다.
   
2. Math Skills: 수학적 지식을 잘 갖추고 있어야 한다 (특히 선형대수, 확률)
   
3. Knowing Papers: 최신 연구 트렌드 논문들을 많이 알고 익혀야 한다.

# 인공지능 - 머신러닝 - 딥러닝의 관계
'인공지능'이란 **인간의 지능을 모방**하는 목표로 한다.

'머신러닝'이란 **데이터에 기반하여 컴퓨터를 훈련**시켜 인간의 지능을 모방하는 것을 목표로 한다.

'딥러닝'이란 **신경망(neural networks)을 이용**하여 데이터에 기반해 컴퓨터를 훈련시키고, 인간의 지능을 모방한다.

# 딥러닝의 주요 요소 4가지
딥러닝을 공부할 때, 딥러닝 논문을 살펴볼 때 항상 이 4가지에 입각해서 (혹은 파악하려고 노력하면서?) 공부하는게 좋다.

1. 데이터
	- 어떤 문제를 풀 지에 따라 주어지는 데이터에 따라 달라지게 된다.
	  
2. 모델: 주어진 데이터를 label로 바꿔주는, 학습하고자 하는 모델
   
3. Loss function: 머신러닝 혹은 딥러닝 모델의 출력값과 사용자가 원하는 출력값의 오차를 의미 ([출처](https://didu-story.tistory.com/27))
	- 목표로 하는 task에 따라 loss function은 달라진다.
	- Loss function이 줄어드는게 '항상' 좋은 것은 아니기 때문에, 이를 잘 이해하고 있는 것이 중요하
	  
4. 알고리즘: 손실(loss)를 최소화하도록 파라미터(parameters)를 조정해줌

# Historical Review
[Deep Learning's Most Important Ideas - A Brief Historical Review (2020-07-29)](https://dennybritz.com/blog/deep-learning-most-important-ideas/)에서 발췌

시기 별로 deep learning에서 중요한 역할을 한 발표들을 살펴본다.

## 2012 - AlexNet
- 처음으로 딥러닝을 활용하여 ILSVRC(ImageNet Large Scale Visual Recognition Challenge) 대회에서 우승
- 이후 deep learning이 대회에서 상위권을 휩쓸기 시작함

## 2013 - DQN (Deep Q-Network)
<iframe width="560" height="315" src="https://www.youtube.com/embed/V1eYniJ0Rnk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
- 알파고를 만든 DeepMind의 강화학습(reinforcement learning) 알고리즘

## 2014 - Encoder/Decoder
- 신경망을 이용하여 외국어를 번역해줌.
- 단어의 연속이 주어지면 이를 다른 외국어의 연속으로 뱉어준다.

## 2014 - Adam Optimizer
- 많은 사람들이 2020년에 adam optimizer로 사용함
- 이는 Adam optimize의 결과가 상당히 좋다는 것을 의미함

## 2015 - Generative Adversarial Network(GAN)
- 이미지를 만들어내는 방법
- 데이터셋 2개를 만들어서 사용한다

## 2015 - Residual Network
- Deep learning이 가지고 있던 '학습이 너무 깊어지면 정확도가 떨어지던 문제'를 개선함
- 단계를 깊게해도 정확도가 높아지기 시작함

## 2017 - Transformer

## 2018  - Bidirectional Encoder Representations from Transformers(BERT)
- Fine-tuned NLP modles
- Pre-training 선행된 뒤 Fine-Tuning을 수행

## 2019 - BIG Language Models
- GPT-3
- Fine-tuning 강화
- 1억 7천 5백만개의 파라미터를 활용한 언어모델

## 2020 - Self Supervised Learning
- 분류문제를 풀 때 주어진 데이터 뿐만 아니라 label되지 않은 이미지들을 활용하여 학습에 같이 사용
- SimCLR (a simple framework for contrastive learning of visual representations)
- 2020년에는 아예 데이터셋을 컴퓨터가 스스로 만들어서 활용하기도 함