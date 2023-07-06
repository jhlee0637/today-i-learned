https://adnoctum.tistory.com/332
https://velog.io/@cualquier/%EA%B7%80%EB%AC%B4%EA%B0%80%EC%84%A4-%EB%8C%80%EB%A6%BD%EA%B0%80%EC%84%A4%EC%9D%80-%EB%AD%98%EA%B9%8C
https://angeloyeo.github.io/2020/03/29/p_value.html


귀무가설(null hypothesis)이 맞다고 전제할 때, 통계값(statistics)이 실제 관측된 값 이상일 확률
The probability that the test statistic is equal to or greater than the observed value, assuming the null hypothesis is true, is called the p-value. 

p-value는 귀무가설이 맞다고 가정했을 때, 관측된 데이터나 그보다 극단적인 데이터가 나타날 확률을 의미한다. 
The p-value represents the probability of observing the data or more extreme data, given that the null hypothesis is true. 

즉, 가설검정의 과정에서 전체 데이터가 아니라 sampling된 데이터를 가지고 검정을 할 때, 그 통계값이 얼마나 믿을 수 있는가에 대한 것이다.
In other words, when conducting hypothesis testing using a sample of data instead of the entire population, the p-value indicates the level of confidence we can have in the test statistic. It represents how much we can trust the statistical value obtained from the sample data to make inferences about the population as a whole.

-

교수님의 연구실에 10,000개의 샘플로 이루어진 데이터가 있다고 하자. 이 모집단 데이터는 정규분포의 모습을 하고 있고, 평균 값은 100이다. 이때, 교수님이 우리에게 모집단 데이터와 평균값에 대한 내용을 숨기고 무작위로 고른 샘플 100개를 주고는 모집단의 평균값을 추측해보라고 한다.
Let's say you have a dataset consisting of 10,000 samples in your professor's research lab. This population data follows a normal distribution, with a mean value of 100. Now, your professor has randomly selected a sample of 100 data points from the population and provided them to you, without revealing any information about the population data or the mean value. Your task is to estimate the population mean based on this sample.

10,000개의 샘플이 정규분포를 그리고 있기 때문에, 데이터의 샘플 값은 0부터 200까지 다양하다. 만약 교수님이 주신 샘플 100개의 값이 전부 150 이상이었다면, 우리가 구한 평균값은 150 이상이 될 것이다. 이는 모집단의 평균값 100을 상회하므로, 우리가 받은 샘플들은 모집단의 모습을 반영하지 못한다고 할 수 있다.
Since the 10,000 samples follow a normal distribution, the sample values can range from 0 to 200, exhibiting various values in between. If all the 100 values provided by your professor were 150 or higher, the mean value you calculate would be greater than 150. This would imply that the estimated mean exceeds the population mean of 100, suggesting that the sample you received does not accurately reflect the characteristics of the population.

어떤 방식으로도 10,000개의 샘플에서 무작위로 뽑은 100개의 평균값이 모집단과 동일하게 100일 가능성은 적다. 그렇다면 98이라면? 95라면? 93이라면? 우리는 그 평균값은 믿을 수 있을까?
Using any method, it is unlikely that the average of 100 randomly selected samples out of 10,000 will be identical to the population. So, what about 98? What about 95? What about 93? Can we trust those average values?

이번에는 다르게 생각해보자. 10,000개로 이루어진 모집단에서 무작위하게 뽑은 100개의 샘플의 평균값이 95라는 사실을 알았다. 우리는 모집단에 대하여 아는 사실이 없다. 이번에는 교수님도 모른다. 다만 우리는 95라는 값이 모집단의 평균값과 정확하게 일치하지 않는다는 사실을 알고있다. 그렇다면 모집단의 평균값은 100일까 90일까?
Let's consider a different scenario this time. We know the average of 100 randomly selected samples from a population of 10,000 is 95. We have no information about the population. Even the professor is unaware of it. However, we do know that the value of 95 does not precisely match the population mean. So, would the population mean be 100 or 90?
-

가설검증이라는 것은 전체 데이터의 일부만을 추출하여 평균을 내고, 그 평균이 전체 데이터의 평균을 잘 반영한다는 가정 하에 전체 데이터의 평균을 구하는 작업인데, 아무리 무작위 추출을 잘 한다 하더라도 추출된 데이터의 평균은 전체 데이터의 평균에서 멀어질 수 있게 된다. 따라서, 내가 추출한 이 데이터의 평균이 원래의 전체 데이터의 평균과 얼마나 다른 값인지를 알 수 있는 방법이 필요하게 된다. 이와 같은 문제 때문에 나온 값이 p-value 이다.
Hypothesis testing involves taking a subset of the entire data, calculating the average under the assumption that it reflects the mean of the entire dataset. However, no matter how well we perform random sampling, the average of the sampled data can deviate from the mean of the entire dataset. Therefore, we need a method to determine how different the average of the extracted data is from the original mean of the entire dataset. This is where the concept of p-value comes into play.

-

"모집단 정규분포 그래프의 평균값이 100 이다"라는 귀무가설이 참이라는 가정 할 때, 10,000개의 데이터에서 100개의 샘플을 계속해서 뽑고 평균값을 구하고 있다고 하자. 100개의 샘플을 sampling 할 때 이론적으로 나올 수 있는 평균값의 분포가 있다. 이때, 내가 방금 뽑은 95라는 평균값 보다 더 큰 평균값이 나올 수 있는 확률이 p-value이다.
When assuming that the null hypothesis states "the mean of the population normal distribution is 100," and continuously drawing 100 samples from a dataset of 10,000 to calculate the mean, there is a theoretical distribution of possible mean values that can occur when sampling the 100 values. In this case, the p-value represents the probability of obtaining a mean greater than the observed average of 95 that you just drew.

-

위의 예시로 다시 설명해보자면
1) 모집단의 평균값이 100이라는 '귀무가설'을 세웠다.
2) 무작위하게 뽑은 샘플들의 평균값이 95였다.
3) 95라는 평균값이 앞으로도 수행할 무작위 sampling에서 나올 확률이 p-value다.
Let's explain again using the example you provided:
1. We set the null hypothesis as "the mean of the population is 100."
2. The average of the randomly selected samples was 95.
3. The p-value represents the probability of obtaining a value as extreme as 95 or higher in future random sampling.

이때, 95라는 평균값보다 더 높은 값, 96~100이 앞으로도 수행할 무작위 sampling에서 나올 확률이 97% 라고하자. (p-value=0.97) 그렇다면 우리가 1) 에서 말한 '모집단의 평균값이 100'이라는 '귀무가설'은 맞는 귀무가설일까 틀린 가설일까? 97% 확률로 일어날 사건이기 때문에 맞는 귀무가설이라고 할 수 있을 것이다.
In this case, let's say the probability of obtaining values higher than 95, specifically in the range of 96 to 100, in future random sampling is 97% (p-value = 0.97). So, is the null hypothesis we stated in step 1, "the mean of the population is 100," a valid or invalid hypothesis? Considering that the event has a 97% chance of occurring, we can conclude that it is a valid null hypothesis.
-

이때, 귀무가설의 의미를 다시 상기해야 한다. 귀무가설은 "새로울 게 없다"인 가설이다. 다른 말로 귀무가설은 부정적, 소극적, 보수적, 전통적인 입장이며, 과학자들이 제발 틀리기를 기도하는 가설이다. '기존에 알려진 사실'로 생각해도 된다.
It is important to revisit the meaning of the null hypothesis. The null hypothesis states that "there is no new effect" or "there is no difference." In other words, the null hypothesis takes a negative, conservative, and traditional stance. It is a hypothesis that scientists hope to reject, as it represents the status quo or the "already known fact."

따라서, 귀무가설이 0.05 이하의 p-value를 가질 때 우리는 일반적으로 이 귀무가설이 틀렸다고 말한다. 귀무가설이 틀리고 나서야 과학자들이 그토록 원하는 대립가설이 참이라고 말할 수 있는 것이다.
Indeed, when the null hypothesis has a p-value of less than 0.05, it is generally concluded that the null hypothesis is rejected. Scientists can then state that the alternative hypothesis, which they had been hoping to support, is likely to be true.

-

위에서는 주로 평균값에 대해서 얘기하였으나, 평균과 분산을 동시에 알아야 가설검증을 할 수 있다. 또한, 모분포의 평균과 분산값에 대한 조건이 있으면, 거기서 n 개를 sampling 했을 때 그 n 개의 평균이 얼마나 잘 나올 수 있는 값인지 중심극한정리와 표준정규분포의 성질을 이용하여 정확하게 계산이 가능하다. 따라서 그 경우마다 p-value를 구할 수 있게 된다.
In the previous discussion, we mainly focused on the average value, but hypothesis testing requires knowledge of both the mean and variance. Moreover, if there are conditions regarding the mean and variance of the population distribution, it is possible to calculate precisely how well the sample mean of n values will perform using the properties of the central limit theorem and the standard normal distribution. Therefore, it becomes possible to calculate the p-value for each specific case.
