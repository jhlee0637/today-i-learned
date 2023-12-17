[Gonorazky HD, Naumenko S, Ramani AK, Nelakuditi V, Mashouri P, Wang P, Kao D, Ohri K, Viththiyapaskaran S, Tarnopolsky MA, Mathews KD, Moore SA, Osorio AN, Villanova D, Kemaladewi DU, Cohn RD, Brudno M, Dowling JJ. Expanding the Boundaries of RNA Sequencing as a Diagnostic Tool for Rare Mendelian Disease. Am J Hum Genet. 2019 Mar 7;104(3):466-483. doi: 10.1016/j.ajhg.2019.01.012. Epub 2019 Feb 28. Erratum in: Am J Hum Genet. 2019 May 2;104(5):1007. PMID: 30827497; PMCID: PMC6407525.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6407525/)

# Abstract
- 2019년 기준으로 [[Mendelian disease]]에 기반하여, 유전형의 우성 혹은 열성을 통해 gene-panel과 [[Knowledge/Bioinformatics/WES|WES]] 결과를 분석하는 방법이 일반적이다.
- 그러나 유전형에 기반한 진단은 그 성과가 50%에 불과하다.
- [[WES]]의 단점을 보완하기 위해서 [[Knowledge/Bioinformatics/WGS|WGS]]를 활용할 수도 있으나, [[WGS]] 또한 [[Mutation]] 분석, 특히 non-coding 돌연변이에 대한 분석에서 단점을 지닌다.
- 이를 해결하기 위해서 [[RNA-seq]]을 통해 transcriptome 분석으로 진단에 더 적절한지 알아보았다.
- 'monogenetic neuromuscular disorder'에 대한 RNA-seq 분석을 통해 특히 희귀질환에 대해서 RNA-seq이 더 적절한 진단방법이라는 점을 알 수 있었다.
# Material and Methods

## Generating Sequencing Data
- The Centre of Applied Genomics (TCAG)에서 수행
- Illumina HiSeq 2000
	- Paird-end 126+126bp sequencing
	- Sequencing depth 50-100M paried reads per sample
## Gene Panels
- 8개의 가상의 neuromuscular disease 관련 gene panels 생성
	- 132개의 유전자를 지님
	- Panel은 2017년의 monogenic neuromuscular disorder에 대한 자료를 참고
	- 필요한 경우 ENSEMBL annotation에 따라 OMIM 유전자 혹은 모든 단백질 코딩 유전자들에 대해서도 분석했다.
	- Famil 40에 대해서는 Mitocarta gene panel을 사용했다.
## Read Alignment, Quality Control, and Read Quantitation
- 