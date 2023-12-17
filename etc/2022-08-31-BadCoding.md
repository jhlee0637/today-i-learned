---
layout: post
title: "[8월] 코딩습관개선 "
subtitle: "8월 코딩 회고"
date: 2022-08-31
author: "Lee Je Hee"
URL: "/2022/08/31/BadCoding/"
published: False
tags:
 - Python
---
공부를 하면서 코딩습관 개선점을 적어본다

# enumerate 사용하기
https://www.daleseo.com/python-enumerate/

# replace 사용하기
https://ctdlog.tistory.com/38
replace를 정말 잘 안 쓴다

# 최대공약수 최소공배수 약수 배수
https://slowsure.tistory.com/128
https://namu.wiki/w/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98%20%EC%B2%B4#s-3

# 2진법 3진법 5진법 10진법
https://velog.io/@code_angler/파이썬-진수변환2진법-3진법-5진법-10진법n진법

### 내 방식 (2진법의 경우)
```python
bi=""
while True:
    if num>=1:
        bi+=str(num%2)
        num=int(num/2)
    else:
        break
bi=bi[::-1]
print (bi)
```

# rjust 한동안 까먹고 안 쓰고 있었다
https://school.programmers.co.kr/learn/courses/30/lessons/17681?language=python3