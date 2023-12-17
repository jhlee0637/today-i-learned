[Williams, C.G., Lee, H.J., Asatsuma, T. _et al._ An introduction to spatial transcriptomics for biomedical research. _Genome Med_ **14**, 68 (2022). https://doi.org/10.1186/s13073-022-01075-1](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-022-01075-1)
# Background
- 2009년 처음으로 단일세포에서 mRNA에 대한 전체 레퍼토리가 transcriptome이라는 이름 아래에 밝혀졌다.
- 이를 계기로 진핵세포에서 scRNA-seq에 대한 연구가 활발해졌다.
- 대부분의 scRNA-seq 방식은 단일세포를 손상되지 않은 상태로 분리하거나 라벨을 통해 구별하는 방법을 요구한다.
	- 대표적으로 microfluidic, droplet-based, 혹은 limiting dilution method가 있다.
## What is ‘spatial transcriptomics’ and why is it useful?
- 손상없이 단일세포로 분리되는 세포들이 있는가 하면, 그렇지 않은 세포들도 있었다.
	- T cell과 같은 면역세포들은 혈액 내에서도 자유롭게 움직이기 때문에 분리하기 쉬웠다.
	- 반면 뇌 속의 뉴론같은 세포들은 손상 시키지 않고 세포를 분리하기가 어려웠다.
- 따라서 세포가 아닌 조직단위로 trancriptomics 연구를 수행하려는 시도가 존재했다.
	- 조직에서 세포를 분리시킬 필요가 없기 때문에 spatial information 또한 잘 보존되었다.
- 세포의 spatial information은 어떠한 정보를 제공하는가?
	- 세포의 표현형(phenotype)
	- 세포 상태(cell state)
	- 세포와 조직의 기능
# Spatial transcriptomic technologies
- Spatial transcriptomic은 조직 내 특정한 spatial 영역에서 하나의 유전자의 transcripts 수를 구하는 것을 목적으로 한다.
- 조직의 크기는 작게는 1$mm^2$ 부터 한 장기(organ)에 이르기까지 다양하다.
- 목표로 하는 유전자의 개수도 10개부터 수천 혹은 whole genome에 이를 수 있다.
- Spatial 영역은 whole tissue domain부터 500 μm × 500 μm, 혹은 단일세포 전체까지 이를 수 있다.
# A guide to spatial transcriptomic analyses
<img src="https://media.springernature.com/full/springer-static/image/art%3A10.1186%2Fs13073-022-01075-1/MediaObjects/13073_2022_1075_Fig3_HTML.png?as=webp">
*Typical structure of spatial transcriptomics analysis. Data are first preprocessed using technique-specific methods and algorithms. Normalization methods account for technical variation. Downstream analyses may be performed with a range of general-purpose transcriptomic analysis packages or with specialized methods for spatial transcriptomics.*
## Pre-processing spatial transcriptomic data
- scRNA-seq에서 pre-processing이란 이미지 혹은 서열 데이터를 활용하여 분석하기 용이한 matrix로 만드는 것을 의미한다.
- Matrix는 특정한 spatial capture 영역에서 조사한 '유전자 별 transcript count'(transcript counts per gene)이다.
- 이 matrix를 **gene-spot matrices**라고 부르겠다.
	- multi-omics 연구의 경우 trasncript count가 아니라 protein count인 경우도 있다.
- In Situ Hybridization(ISH)-based 혹은 In Situ Sequencing(ISS)-based scRNA-seq의 경우 유전자 서열이나 유전자 특이적인 바코드를 데이터로 얻게된다.
	- 
## Generalized toolkits for downstream analysis
## Identification of spatial features
## Deconvolution
## Imputation and mapping single cells
## Cell-cell interaction inference