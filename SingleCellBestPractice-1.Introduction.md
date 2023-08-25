https://www.sc-best-practices.org/preamble.html    
\*2023년 8월 기준으로 작성된 문서 내용을 복사한 것이며, 해당 문서는 꾸준히 수정이 되어지고 있음    
\*개인적으로 읽을만했던 내용만 복사해옴    
\*문장 전체를 직역하지 않음    
# INTRODUCTION
## [1. Prior art](https://www.sc-best-practices.org/introduction/prior_art.html)

## [2. Single-cell RNA sequencing](https://www.sc-best-practices.org/introduction/scrna_seq.html#)

## 2.4 RNA sequencing
- RNA-Seq largely follows the DNA sequencing protocols, but includes a reverse transcription step where complementary DNA (cDNA) is synthesized from the RNA template.    
  *RNA-Seq은 DNA sequencing protocol을 많이 따르지만, 차이점으로 RNA template에서 complementary DNA를 합성하기 위한 reverse transcription 과정이 포함된다.*
## 2.5 Single-cell RNA sequencing

**2.5.1. Overview**

- Sequencing of RNA can be mainly conducted in two ways:    
  *RNA sequencing 주요 방법 두 가지:*     
	1) Either by sequencing the mixed RNA from the source of interest across cells (bulk sequencing)    
	   *여러 세포에서 유래한 RNA들을 sequencing하기*     
	2) by sequencing the transcriptomes of the cells individually (single-cell sequencing).    
	   *각 세포에서 유래한 transcriptiomes를 sequencing하기* 
	      
- Some drugs or perturbations may affect only specific cell types or interactions between cell types.    
  *특정 약물이나 교란법(perturbation)은 특정한 세포종류들 혹은 상호작용 영향일 미칠 수 있다.*
- To uncover such relationships, it is vital to examine gene expression on a single-cell level.    
  *이러한 관계를 밝혀내기 위해 single-cell 수준의 유전자 발현 조사가 중요.*

- Single-cell RNA-Seq (scRNA-Seq) does, however, come with several caveats.    
  *sRNA-seq의 단점(caveat)*
	- First, single-cell experiments are generally more expensive and more difficult to properly conduct.    
	  *비싸고 어렵다*
	- Second, the downstream analysis becomes more complex due to the increased resolution, and it is easier to draw false conclusions.    
	  *Resolution이 증가 -> downstream 분석과정 복잡해짐 & false 결과빈도 증가*
	  
- Just like bulk sequencing, single-cell sequencing requires:
	- lysis
	- reverse transcription
	- amplification
	- the eventual sequencing.
- In addition, single-cell sequencing requires cell isolation and a physical separation into smaller reaction chambers or another form of cell labeling to be able to map the obtained transcriptomes back to the cells of origin later on.    
  *Single-cell sequencing은  transcriptome이 어느 세포에서 유래했는지 추적하기 위해 특유의 cell isolation 과정과 모든 세포들을 물리적으로 분리하는 과정이 필수적으로 필요하다.(작은 chamber든 labelling이든)*

- Hence, these are also the steps where most single-cell assays differ:    
  *따라서, 여러 single-cell sequencing 방법들이 다음의 과정들을 서로 다르게 수행하는 경우가 많다*
	- single-cell isolation
	- transcript amplification
	- sequencing(depending on the sequencing machine)   

**2.5.2 Transcript quantification**

- Transcript quantification is the process of counting the hits of the sequenced transcripts against the gene sequences.    
  *Transcript quantification이란 유전자 서열과 대응하는 sequenced transcripts 수를 세는 과정이다.*
- There are two major approaches to transcript quantification:
	1) Full-length protocols
		- try to cover the whole transcript uniformly with sequencing reads    
		  *transcript 전체를 sequencing reads와 비교*
	- Tag-based protocols
		- only capture the 5’ or 3’ ends.     
		  *5' end 혹은 3' end만 비교*  
		  
- The usage of UMIs is a common solution to quantify the original, non-duplicated molecules.    
  *UMIs는 증폭과정을 거치지 않은 본래의 (유전)분자물질을 정량하는 일반적인 방법이다.*
	- The UMIs serve as molecular barcodes and are also sometimes referred to as random barcodes.    
	  *UMIs는 분자바코드로 때로는 랜덤바코드로 불린다.*
	- These ‘barcodes’ consist of short random nucleotide sequences that are added to every molecule in the sample as a unique tag.    
	  *이 '바코드'들은 짧은 뉴클레오타이드 서열들이 랜덤하게 이루어진 형태이다. 이 서열들은 하나의 unique tag로 붙여지게 된다.* 
	- UMIs must be added during library generation before the amplification step.    
	  *UMIs는 반드시 amplication step 이전인 library generation 과정에서 붙여져야한다.*

**2.5.3 Single-cell sequencing protocols**

- Currently, three types of single-cell sequencing protocols exist, which are grouped primarily by their cell isolation protocols:    
  *현재는 cell isolation protocol에 따라 3개의 방식으로 분류한다.*
	1) Microfluidic device-based strategies    
		  -  cells are encapsulated into hydrogel droplets    
		     *세포를 hydrogel droplet을 이용해서 분리*
	2) Well plate based protocols    
		- cells are physically separated into wells     
		  *세포를 well을 이용해서 분리*
	3) The commercial Fluidigm C1 microfluidic chip based solution
		- loads and separates cells into small reaction chambers.     
		  *세포를 small reaction chamber를 이용해서 분리*

**2.5.3.4. Nanopore single-cell transcriptome sequencing**

- [Lebrigand _et al._, 2020](https://www.nature.com/articles/s41467-020-17800-6)introduced ScNaUmi-seq (Single-cell Nanopore sequencing with UMIs) which combines Nanopore sequencing with cell barcode and UMI assignment.
	- The barcode assignment is guided with Illumina data by comparing the cell bar code sequences found in the Nanopore reads with those recovered from the Illumina reads for the same region or gene.
	- However, this effectively requires two single-cell libraries.
- scCOLOR-seq([Philpott _et al._, 2021](https://www.nature.com/articles/s41587-021-00965-w)) computationally identifies barcodes without errors using nucleotide pair complementary across the full length of the barcode.
	- These barcodes are then used as guides to correct the remaining erroneous barcodes.
	- A modified UMI-tools directional network based method corrects for UMI sequence duplication.

- Strengths:
	- Recovers splicing and sequence heterogeneity information

- Weaknesses:
	- Nanopore reagents are expensive.
	- High cell barcode recovery error rates.
	- Depending on the protocol, barcode assignment is guided with Illumina data requiring two sequencing assays.
#### 2.5.3.5 Summary
- In summary, we strongly recommend that wet lab and dry lab scientists select the sequencing protocol based on the aim of the study.
	- Is a deep characterization of a specific cell type population desired?
		- In this case one of the plate-based methods may be more suitable.
	- On the contrary, droplet based assays will capture heterogeneous mixtures better, allowing for a more broad characterization of the sequenced cells.
	- Moreover, if the budget is a limiting factor, the protocol of choice should be more cost-effective and robust.

- When analyzing the data, be aware of the sequencing assay specific biases.
	- For an extensive comparison of all single-cell sequencing protocols, we recommend the “Benchmarking single-cell RNA-sequencing protocols for cell atlas projects” paper by [Mereu et al., 2020](https://www.nature.com/articles/s41587-020-0469-4).
### 2.5.4 single-cell vs single-nuclei
- So far we have only been discussing single-cell assays, but it is also possible to only sequence the nuclei of the cells.

- Single-cell profiling does not always provide an unbiased view on cell types for specific tissues or organs, such as, for example, the brain.
	- During the tissue dissociation process, some cell types are more vulnerable and therefore difficult to capture.
	- Moreover, single-cell sequencing highly relies on fresh tissue, making it difficult to make use of tissue biobanks.

- On the other hand, the nuclei are more resistant to mechanical force, and can be safely isolated from frozen tissue without the use of tissue dissociation enzymes[Krishnaswami et al., 2016].

- Both options have varying applicability across tissues and sample types, and the resulting biases and uncertainties are still not fully uncovered.
	- It has been shown already that nuclei accurately reflect all transcriptional patterns of cells[Ding et al., 2020].
	- The choice of single-cell versus single-nuclei in the experimental design is mostly driven by the type of tissue sample.
- Data analysis however should be aware of the fact that dissociation ability will have a strong effect on the potentially observable cell types.
- Therefore, we strongly encourage discussions between wet lab and dry lab scientists concerning the experimental design.
# [3. Raw data processing](https://www.sc-best-practices.org/introduction/raw_data_processing.html)
- Here, we will primarily refer to this phase of processing as “raw data processing”, and our focus will be on the phase of data analysis that begins with lane-demultiplexed FASTQ files, and ends with a count matrix representing the estimated number of distinct molecules arising from each gene within each quantified cell, potentially stratified by the inferred splicing status of each molecule (Fig. 3.1).    

![Fig. 3.1.](https://www.sc-best-practices.org/_images/overview_raw_data_processing.jpg)    
Fig. 3.1 An overview of the topics discussed in this chapter.    
In the plot, “txome” stands for transcriptome.

- This count matrix then serves as the input for the myriad methods that have been developed for various analyses carried out with scRNA-seq data [Zappia and Theis, 2021], from methods for normalization, integration, and filtering through methods for inferring cell types, developmental trajectories, and expression dynamics.
- In particular, we will cover the fundamental steps in raw data processing, including read alignment/mapping, cell barcode (CB) identification and correction, and the estimation of molecule counts through the resolution of unique molecular identifiers (UMIs).

>A note on what precedes raw data processing    
>
>The decision of where to begin discussing raw data processing is somewhat arbitrary. We note that while, here, we consider starting with lane-demultiplexed FASTQ files as the raw input, even this already represents data that has been processed and transformed from raw measurements. Further, some of the processing that precedes the generation of the FASTQ files is relevant to challenges that may arise in subsequent processing. 

## 3.1 Raw data quality control
- Once raw FASTQ files have been obtained, the quality of the reads themselves can be quickly diagnosed by running a quality control (QC) tool, such as [`FastQC`](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/), to assess read quality, sequence content, etc.
	- If run successfully, `FastQC` generates a QC report for each input FASTQ file.
	- Overall, this report summarizes the quality score, base content, and certain relevant statistics to spot potential problems originating from library preparation or sequencing.
- Although nowadays, single-cell raw data processing tools internally evaluate some quality checks that are important for single-cell data, such as the N content of sequences and the fraction of mapped reads, it is still a good habit to run a quick quality check before processing the data, as it evaluates other useful QC metrics.
## 3.2 Alignment and mapping
- Mapping or alignment is a fundamental step in single-cell raw data processing. It refers to the process of determining the potential loci of origin of each sequenced fragment (e.g., the set of genomic or transcriptomic loci that are similar to the read).
- Depending on the sequencing protocol, the resulting raw sequence file contains:
	- the cell-level information
	- commonly known as cell barcodes (CB)
	- the unique molecule identifier (UMI)
	- the raw cDNA sequence (read sequence)    
	  generated from the molecule.
- Tools such as:
	- Cell Ranger (commercial software from 10x Genomics) [Zheng et al., 2017]
	- zUMIs [Parekh et al., 2018]
	- alevin [Srivastava et al., 2019]
	- RainDrop [Niebler et al., 2020]
	- kallisto|bustools [Melsted et al., 2021]
	- STARsolo [Kaminow et al., 2021]
	- alevin-fry [He et al., 2022]    
	  provide dedicated treatment for aligning scRNA-seq reads along with parsing of technical read content (CBs and UMIs), as well as methods for demultiplexing and UMI resolution.
- While the specific algorithms, data structures, and time and space trade-offs made by different alignment and mapping approaches can vary greatly, we can roughly categorize existing approaches along two axes:
	- The type of mapping they perform
	- The type of reference sequence against which they map reads.
### 3.2.1. Types of mapping
- Here we consider three main types of mapping algorithms that are most commonly applied in the context of mapping sc/snRNA-seq data:
	- spliced alignment
	- contiguous alignment
	- variations of lightweight mapping

- First, let us draw a distinction here between alignment-based approaches and lightweight mapping-based approaches ([Fig. 3.14](https://www.sc-best-practices.org/introduction/raw_data_processing.html#raw-proc-fig-alignment-mapping)).    

![image](https://www.sc-best-practices.org/_images/alignment_vs_mapping.png)    
Fig. 3.14 An abstract overview of the alignment-based method and lightweight mapping-based method.    

- Alignment approaches apply a range of different heuristics to determine the potential loci from which reads may arise and then subsequently score, at each putative locus, the best nucleotide-level alignment between the read and reference, typically using dynamic programming-based approaches.
- The exact type of dynamic programming algorithm used depends on the type of alignment being sought.
	- [Global alignment](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm) is applicable for the case where the entirety of the query and reference sequence are to be aligned.
	- [local alignment](https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm) is applicable when, possibly, only a subsequence of the query is expected to match a subsequence of the reference.
- Typically, the models most applicable for short-read alignment are neither fully global nor fully local, but fall into a category of semi-global alignment where the majority of the query is expected to align to some substring of the reference (this is often called “fitting” alignment).
- Moreover, it is sometimes common to allow soft-clipping of the alignment so that the penalties for mismatches, insertions, or deletions appearing at the very start or end of the read are ignored or down-weighted. This is commonly done using [“extension” alignment](https://github.com/smarco/WFA2-lib#-33-alignment-span).
- Though these modifications change the specific rules used in the dynamic programming recurrence and traceback, they do not fundamentally change its overall complexity.

- Apart from these general alignment techniques, a number of more sophisticated modifications and heuristics have been designed to make the alignment process more practical and efficient in the context of aligning genomic sequencing reads.
	- For example, `banded alignment` [Chao _et al._, 1992](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id96 "Kun-Mao Chao, William R. Pearson, and Webb Miller. Aligning two sequences within a specified diagonal band. Bioinformatics, 8(5):481–487, 1992. URL: https://doi.org/10.1093/bioinformatics/8.5.481, doi:10.1093/bioinformatics/8.5.481.") is a popular heuristic included in the alignment implementation of many popular tools, which avoids computing large parts of the dynamic programming table if the user is uninterested in alignment scores below a certain threshold.
	- Likewise, other heuristics like X-drop [Zhang _et al._, 2000](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id108 "Zheng Zhang, Scott Schwartz, Lukas Wagner, and Webb Miller. A greedy algorithm for aligning term`DNA` sequences. Journal of Computational Biology, 7(1-2):203–214, February 2000. URL: https://doi.org/10.1089/10665270050081478, doi:10.1089/10665270050081478.") and Z-drop [Li, 2018](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id97 "Heng Li. Minimap2: pairwise alignment for nucleotide sequences. Bioinformatics, 34(18):3094–3100, May 2018. URL: https://doi.org/10.1093/bioinformatics/bty191, doi:10.1093/bioinformatics/bty191.") are popular for pruning un-promising alignments early.
	- Recent algorithmic progress, such as wavefront alignment [Marco-Sola _et al._, 2022](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id107 "Santiago Marco-Sola, Jordan M Eizenga, Andrea Guarracino, Benedict Paten, Erik Garrison, and Miquel Moreto. Optimal gap-affine alignment in o(s) space. bioRxiv, April 2022. URL: https://doi.org/10.1101/2022.04.14.488380, doi:10.1101/2022.04.14.488380."), [Marco-Sola _et al._, 2020](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id105 "Santiago Marco-Sola, Juan Carlos Moure, Miquel Moreto, and Antonio Espinosa. Fast gap-affine pairwise alignment using the wavefront algorithm. Bioinformatics, September 2020. URL: https://doi.org/10.1093/bioinformatics/btaa777, doi:10.1093/bioinformatics/btaa777.")], allows for determining optimal alignments in asymptotically (and practically) shorter time and smaller space if high-scoring (low divergence) alignments exist.
	- Finally, considerable effort has also been devoted to optimizing data layout and computation in a way that takes advantage of instruction-level parallelism [Farrar, 2007](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id100 "Michael Farrar. Striped Smith–Waterman speeds database searches six times over other SIMD implementations. Bioinformatics, 23(2):156–161, 2007."), [Rognes and Seeberg, 2000](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id101 "Torbjørn Rognes and Erling Seeberg. Six-fold speed-up of Smith–Waterman sequence database searches using parallel processing on common microprocessors. Bioinformatics, 16(8):699–706, 2000."), [Wozniak, 1997](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id99 "Andrzej Wozniak. Using video-oriented instructions to speed up sequence comparison. Bioinformatics, 13(2):145–150, 1997.")],and to expressing the alignment dynamic programming recurrences in a manner that is highly amenable to data parallelism and vectorization (e.g., as in the difference encoding of [Suzuki and Kasahara 2018](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id106 "Hajime Suzuki and Masahiro Kasahara. Introducing difference recurrence relations for faster semi-global alignment of long sequences. BMC Bioinformatics, February 2018. URL: https://doi.org/10.1186/s12859-018-2014-8, doi:10.1186/s12859-018-2014-8.").
- Most widely-used alignment tools make use of highly-optimized and vectorized alignment implementations.

- In addition to the alignment score, a backtrace of the actual alignment that yields this score may be obtained. Such information is typically encoded as a `CIGAR` string (short for “Concise Idiosyncratic Gapped Alignment Report”), a compressed alphanumeric representation of the alignment, within the SAM or BAM file that is output.
	- An example of a `CIGAR` string is `3M2D4M`, which represents that the alignment has three matches or mismatches, followed by a deletion of length two from the read (bases present in the reference but not the read), followed by four more matches or mismatches.
	- Other variants of the `CIGAR` string can also delineate between matches or mismatches.
		- For example, `3=2D2=2X` is a valid extended `CIGAR` string encoding the same alignment as just described, except that it makes clear that the three bases before the deletion constitute matches and that after the deletion, there are two matched bases followed by two mismatched bases.
	- A detailed description of the `CIGAR` string format can be found in [the SAMtools manual](https://samtools.github.io/hts-specs/SAMv1.pdf) or [the SAM wiki page of UMICH](https://genome.sph.umich.edu/wiki/SAM#What_is_a_CIGAR.3F).

- At the cost of computing such scores, alignment-based approaches know the quality of each potential mapping of a read, which they can then use to filter reads that align well to the reference from mappings that arise as the result of low complexity or “spurious” matches between the read and reference.
- Alignment-based approaches include both:
	- traditional “full-alignment” approaches, as implemented in tools such as:
		- `STAR`[Dobin _et al._, 2013](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id149 "Alexander Dobin, Carrie A Davis, Felix Schlesinger, Jorg Drenkow, Chris Zaleski, Sonali Jha, Philippe Batut, Mark Chaisson, and Thomas R Gingeras. Star: ultrafast universal rna-seq aligner. Bioinformatics, 29(1):15–21, 2013.")
		- `STARsolo`[Kaminow _et al._, 2021](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id115 "Benjamin Kaminow, Dinar Yunusov, and Alexander Dobin. STARsolo: accurate, fast and versatile mapping/quantification of single-cell and single-nucleus term`RNA`-seq data. bioRxiv, 2021.") 
	- _selective-alignment_ implemented in:
		- `salmon`[Srivastava _et al._, 2020](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id139 "Avi Srivastava, Laraib Malik, Hirak Sarkar, Mohsen Zakeri, Fatemeh Almodaresi, Charlotte Soneson, Michael I Love, Carl Kingsford, and Rob Patro. Alignment and mapping methodology influence transcript abundance estimation. Genome Biology, 21(1):1–29, 2020.") 
		- `alevin`[Srivastava _et al._, 2019](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id111 "Avi Srivastava, Laraib Malik, Tom Smith, Ian Sudbery, and Rob Patro. Alevin efficiently estimates accurate gene abundances from dscRNA-seq data. Genome biology, 20(1):1–16, 2019.")    
		  which score mappings but omit the computation of the optimal alignment’s backtrace.

- Alignment-based approaches can be further categorized into:
	1) spliced-alignment
	2) contiguous-alignment approaches    
	   (currently, there are no lightweight-mapping approaches that perform spliced mapping).

	- Spliced-alignment approaches are capable of aligning a sequence read over several distinct segments of a reference, allowing potentially large gaps between the regions of the reference that align well with the corresponding parts of the read.
		- These alignment approaches are typically applied when aligning RNA-seq reads to the genome, since the alignment procedure must be able to align reads that span across one or more splice junctions of the transcript, where a sequence that is contiguous in the read may be separated by intron and exon subsequences (potentially spanning kilobases of sequence) in the reference.
		- Spliced alignment is a challenging problem, particularly in cases where only a small region of the read spans a splicing junction, since very little informative sequence may be available to place the segment of the read that overhangs the splice junction by only a small amount.
	- On the other hand, contiguous alignment seeks a contiguous substring of the reference that aligns well against the read.
	- In such alignment problems, though small insertions and deletions may be allowed, large gaps such as those observed in spliced alignments are typically not tolerated.

- Finally, we can draw a distinction between alignment-based methods such as those described above and lightweight-mapping methods, which include approaches such as:
	- pseudoalignment [Bray _et al._, 2016](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id135 "Nicolas L Bray, Harold Pimentel, Páll Melsted, and Lior Pachter. Near-optimal probabilistic term`RNA`-seq quantification. Nature biotechnology, 34(5):525–527, 2016.")
	- quasi-mapping [Srivastava _et al._, 2016](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id134 "Avi Srivastava, Hirak Sarkar, Nitish Gupta, and Rob Patro. Rapmap: a rapid, sensitive and accurate tool for mapping term`rna`-seq reads to transcriptomes. Bioinformatics, 32(12):i192–i200, 2016.")
	- pseudoalignment with structural constraints [He _et al._, 2022](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id118 "Dongze He, Mohsen Zakeri, Hirak Sarkar, Charlotte Soneson, Avi Srivastava, and Rob Patro. Alevin-fry unlocks rapid, accurate and memory-frugal quantification of single-cell RNA-seq data. Nature Methods, 19(3):316–322, 2022.").
- Such approaches generally achieve superior speed by avoiding nucleotide-level alignment between the read and reference sequences.
- Instead, they base the determination of the reported mapping loci of a read on a separate set of rules and heuristics that may look only at the set of matching k-mers or other types of exact matches (e.g., via a consensus rule) and, potentially, their orientations and relative positions with respect to each other on both the read and reference (e.g., chaining).
	- This can lead to substantially increased speed and mapping throughput, but also precludes easily-interpretable score-based assessments of whether or not the matches between the read and reference constitute a good match capable of supporting a high-quality alignment.
### 3.2.2. Mapping against different reference sequences
- While different choices can be made among the mapping algorithms themselves, different choices can _also_ be made about the reference against which the read is mapped.
- We consider three main categories of reference sequence against which a method might map:
	- The full (likely annotated) reference genome
	- The annotated transcriptome
	- An augmented transcriptome
- It is also worth noting that, currently, not all combinations of mapping algorithms and reference sequences are possible.
	- For example, lightweight mapping-based algorithms do not currently exist that can perform spliced mapping of reads against a reference genome.
#### 3.2.2.1 Mapping to the full genome
- The first type of reference, against which a method may map, consists of the entire genome of the target organism, usually with the annotated transcripts considered during mapping.
	- Tools like:
		- `zUMIs` [Parekh _et al._, 2018](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id121 "Swati Parekh, Christoph Ziegenhain, Beate Vieth, Wolfgang Enard, and Ines Hellmann. zUMIs - a fast and flexible pipeline to process term`RNA` sequencing data with UMIs. GigaScience, May 2018. URL: https://doi.org/10.1093/gigascience/giy059, doi:10.1093/gigascience/giy059.")
		- `Cell Ranger` [Zheng _et al._, 2017](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id151 "Grace X. Y. Zheng, Jessica M. Terry, Phillip Belgrader, Paul Ryvkin, Zachary W. Bent, Ryan Wilson, Solongo B. Ziraldo, Tobias D. Wheeler, Geoff P. McDermott, Junjie Zhu, Mark T. Gregory, Joe Shuga, Luz Montesclaros, Jason G. Underwood, Donald A. Masquelier, Stefanie Y. Nishimura, Michael Schnall-Levin, Paul W. Wyatt, Christopher M. Hindson, Rajiv Bharadwaj, Alexander Wong, Kevin D. Ness, Lan W. Beppu, H. Joachim Deeg, Christopher McFarland, Keith R. Loeb, William J. Valente, Nolan G. Ericson, Emily A. Stevens, Jerald P. Radich, Tarjei S. Mikkelsen, Benjamin J. Hindson, and Jason H. Bielas. Massively parallel digital transcriptional profiling of single cells. Nature Communications, 8(1):14049, Jan 2017. URL: https://doi.org/10.1038/ncomms14049, doi:10.1038/ncomms14049.")
		- `STARsolo` [Kaminow _et al._, 2021](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id115 "Benjamin Kaminow, Dinar Yunusov, and Alexander Dobin. STARsolo: accurate, fast and versatile mapping/quantification of single-cell and single-nucleus term`RNA`-seq data. bioRxiv, 2021.")    
		  take this approach.
	- Since many of the reads arise from spliced transcripts, such an approach also requires the use of a splice-aware alignment algorithm where the alignment for a read can be split across one or more splicing junctions.
- The main benefits of this approach are that reads arising from any location in the genome, not just from annotated transcripts, can be accounted for.
	- Since these approaches require constructing a genome-wide index, there is little marginal cost for reporting not only the reads that map to known spliced transcripts but also reads that overlap or align within introns, making the alignment cost when using such approaches very similar for both single-cell and single-nucleus data.
	- A final benefit is that even reads residing outside of the annotated transcripts, exons, and introns can be accounted for by such methods, which can enable _post hoc_ augmentation of the set of quantified loci (e.g., as is done by Pool _et al._ [2022](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id142 "Allan-Hermann Pool, Helen Poldsam, Sisi Chen, Matt Thomson, and Yuki Oka. Enhanced recovery of single-cell term`RNA`-sequencing reads for missing gene expression data. bioRxiv, 2022. URL: https://www.biorxiv.org/content/early/2022/04/27/2022.04.26.489449, arXiv:https://www.biorxiv.org/content/early/2022/04/27/2022.04.26.489449.full.pdf, doi:10.1101/2022.04.26.489449.")] by adding expressed UTR extensions to transcript annotations in a sample-specific and data-driven manner) and potentially increase gene detection and quantification sensitivity.

- On the other hand, the versatility of the strategy of performing spliced alignment against the full genome comes with certain trade-offs.
	- First, the most commonly-used alignment tools that adopt this strategy in the single-cell space have substantial memory requirements.
		- Due to its speed and versatility, most of these tools are based upon the STAR [Dobin _et al._, 2013](https://www.sc-best-practices.org/introduction/raw_data_processing.html#id149 "Alexander Dobin, Carrie A Davis, Felix Schlesinger, Jorg Drenkow, Chris Zaleski, Sonali Jha, Philippe Batut, Mark Chaisson, and Thomas R Gingeras. Star: ultrafast universal rna-seq aligner. Bioinformatics, 29(1):15–21, 2013.") aligner.
		- Yet, for a human-scale genome, constructing and storing the index can require upwards of 32 GB of memory.
		- The use of a sparse [suffix array](https://en.wikipedia.org/wiki/Suffix_array) can reduce the final index size by close to a factor of 2, but this comes at a reduction in alignment speed, and it still requires larger memory for the initial construction.
	- Second, the increased difficulty of spliced alignment compared to contiguous alignment and the fact that current spliced-alignment tools must explicitly compute a score for each read alignment, means that this approach comes at an increased computational cost compared to the alternatives.
	- Finally, such an approach requires the genome of the organism under study is available.
		- While this is not problematic for the most commonly-studied reference organisms and is rarely an issue, it can make using such tools difficult for non-model organisms where only a transcriptome assembly may be available.