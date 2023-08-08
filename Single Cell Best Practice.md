https://www.sc-best-practices.org/preamble.html
# INTRODUCTION
## [1. Prior art](https://www.sc-best-practices.org/introduction/prior_art.html)

## [2. Single-cell RNA sequencing](https://www.sc-best-practices.org/introduction/scrna_seq.html#)

- RNA-Seq largely follows the DNA sequencing protocols, but includes a reverse transcription step where complementary DNA (cDNA) is synthesized from the RNA template.
	RNA-Seq은 DNA sequencing protocol을 많이 따르지만, RNA template에서 complementary DNA를 합성하기 위한 reverse transcription 과정이 포함된다.

- Sequencing of RNA can be mainly conducted in two ways: Either by sequencing the mixed RNA from the source of interest across cells (bulk sequencing) or by sequencing the transcriptomes of the cells individually (single-cell sequencing).  
	RNA sequencing 방법 두 가지:  
	1) 여러 세포에서 유래한 RNA들을 sequencing하기 (bulk sequencing)  
	2) 각 세포에서 유래한 transcriptiomes를 sequencing하기 (single-cell sequencing)

- Some drugs or perturbations may affect only specific cell types or interactions between cell types. To uncover such relationships, it is vital to examine gene expression on a single-cell level.
	특정 약물이나 교란법은 특정 세포종류나 세포종류들 사이에서만 영향일 미칠 수 있다. 이러한 관계를 밝혀내기 위하여 single-cell 수준에서 유전자 발현을 조사하는 것은 중요하다.

- Single-cell RNA-Seq (scRNA-Seq) does, however, come with several caveats. First, single-cell experiments are generally more expensive and more difficult to properly conduct. Second, the downstream analysis becomes more complex due to the increased resolution, and it is easier to draw false conclusions.
	scRNA-seq의 단점
	1) 더 비싸고 더 어려움
	2)  Resolution이 증가하였기 때문에 downstream 분석과정은 복잡해지고 false 결과가 더 자주 나옴   

- Just like bulk sequencing, single-cell sequencing requires lysis, reverse transcription, amplification, and the eventual sequencing. In addition, single-cell sequencing requires cell isolation and a physical separation into smaller reaction chambers or another form of cell labeling to be able to map the obtained transcriptomes back to the cells of origin later on.
	Single-cell sequencing은 lysis, reverse transcription, amplification, 실제 sequencing 과정과 더불어서, 특유의 cell isolation 과정과 어떤 방식으로든 개별 세포를 차후에 인식할 수 있도록 처리하는 과정이 필요하다.

- Hence, these are also the steps where most single-cell assays differ: single-cell isolation, transcript amplification, and, depending on the sequencing machine, sequencing.
	따라서, 여러 single-cell sequencing 방법들이 다음의 과정들은 서로 다른 방법들을 사용한다: single-cell isolation, transcript amplification...때로는 sequencing 과정 마저도 다르다

- Transcript quantification is the process of counting the hits of the sequenced transcripts against the gene sequences. There are two major approaches to transcript quantification: full-length and tag-based. Full-length protocols try to cover the whole transcript uniformly with sequencing reads, whereas tag-based protocols only capture the 5’ or 3’ ends.
	Transcript quantification이란 유전자 서열과 대응하는 sequenced transcripts 수를 세는 과정이다. 대표적으로 두 가지 방법이 있다.
		1) Full-length: transcript 전체를 sequencing reads와 비교
		2) Tag-based: 5' end 혹은 3' end만 비교

- The usage of UMIs is a common solution to quantify the original, non-duplicated molecules. The UMIs serve as molecular barcodes and are also sometimes referred to as random barcodes. These ‘barcodes’ consist of short random nucleotide sequences that are added to every molecule in the sample as a unique tag. UMIs must be added during library generation before the amplification step.
	UMIs는 증폭과정을 거치지 않은 본래의 (유전)분자물질을 정량하는 일반적인 방법이다. UMIs는 분자바코드로 때로는 랜덤바코드로 불린다. 이 '바코드'들은 짧은 뉴클레오타이드 서열들이 랜덤하게 이루어진 형태이다. 이 서열들은 하나의 unique tag로 붙여지게 된다. UMIs는 반드시 amplication step 이전인 library generation 과정에서 붙여져야한다.