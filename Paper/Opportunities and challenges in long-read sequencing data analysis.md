[Amarasinghe SL, Su S, Dong X, Zappia L, Ritchie ME, Gouil Q. Opportunities and challenges in long-read sequencing data analysis. Genome Biol. 2020 Feb 7;21(1):30. doi: 10.1186/s13059-020-1935-5. PMID: 32033565; PMCID: PMC7006217.](https://pubmed.ncbi.nlm.nih.gov/32033565/)

- [[today-i-learned/Knowledge/Bioinformatics/NGS|NGS]]는 600 베이스 정도를 생산할 때, [[Long-read Sequencing]]은10kb 이상의 리드를 생산할 수 있다.
- NGS는 비용효율적이고 정확하며, 다양한 툴과 파이프라인들이 현재 개발되어있다.
- 하지만 NGS는 재조립 과정을 필요로 한다.

- Long-read Sequencing은 long read를 활용한다.
	- de novo assembly, mapping, transcript isoform identification, structural variants detection을 향상시킬 수 있다.
- Long read는 DNA, RNA 모두 base modification을 방지하면서, 동시에 amplification을 제거할 수 있다.
- 이러한 유용성, 정확성, 생산성, 가격경쟁력이 3세대 기술로 하여금 훨씬 넓은 분야에서 활약할 수 있는 입지를 만들었다.

- model organism, non-model organism 에서 둘 다 사용 가능하다

2020년 기준, 두 회사의 기술이 3세대 기술을 이끌고 있다: PacBio, Oxford Nanopore Technologies

- 두 플랫폼에서 나오는 데이터들은 2세대 기술과 질적으로 차이가 있기 때문에, 전용 분석툴을 필요로 한다

- Long read를 활용하는게 아니라, 합성해서 활용하는 방법도 거론되고 있다.

- genome, methylome, variant, isoform, haplotype, specie 샘플에 대한 정확하게 조립할 수 있다는 전제에 따라서, 합성한 long read를 3세대 제품들로 분석하는 방법도 2011년 이후로 연구되고 있다.

- Long read analyzing tools

- 354개 정도의 툴들이 존재하며 이 중 262개는 Nanopore, 170개는 SMRT 데이터 분석을 위한 툴이다.
- 툴들이 개발되어온 과정을 들여다보면, 초기에 3세대 기술의 데이터 생산량이 특출나지 않았기 때문에 대부분 툴들이 비인간 데이터를 위한 것이었다.

- de novo, 오류교정, 카테고리 정교화가 인기가 많았다

- 반면 transcriptome 분석은 아직도 개발이 더디다

|   |   |   |
|---|---|---|
||Nanopore|PacBio SMRT|
|features|- 2014년 처음 출시<br>- 제품군: MinION, GridION, PromethION<br>- single-strand nucleic acids를 biological nanopore에 통과시키면서, 이온변화를 감지한다.<br><br>- 서로 다른 뉴클레오타이드는 핵산의 신축성에 각각 다른 저항성을 부여한다.<br>- 따라서 패턴에 따라 시퀀스를 특정하여 시퀀싱이 가능하다.<br><br>- Nanopore 시퀀싱의 경우 500 bp 을 시작으로 10~30 kb 정도까지 라이브러리를 받아들이는데, 2.3 Mb 길이를 활용했다는 기록도 있다.<br><br>- pore 안으로 얼마나 무거운 DNA 분자까지 전달할 수 있느냐가 성능을 결정한다.<br><br>- SMRT와 Nanopore의 basecalling 정확도는 최근 급격하게 올라왔다.<br>- raw base called error 비율의 경우 SMRT는 1% 이하, nanopore는 5% 이하를 기록하였다.|- 2011년 출시<br>- 제품군: RSII, Sequel, Sequel II<br>- 웰 바닥에 붙은 polymerase 가 nucleotide 한 개를 분해할 때 마다, 분해된 nucleotide와 동일한 형광신호를 잡아서 분석<br>- Read 의 길이가 polymerase read의 길이와 연관이 있다.<br><br>- 2018년에 나온 Sequel chemistry (V3) 의 경우 polymerase의 길이는 30kb 정도였다.<br><br>- SMRT 시퀀싱의 경우 250 bp ~ 50 kbp의 라이브러리를 받아들일 수 있다.|
|Basecalling|- nanopore 의 raw data는 4kHz 전류에서 측정된 전류의 세기값으로, fast5 포맷으로 저장된다.[A Look at the Nanopore fast5 Format](https://medium.com/@shiansu/a-look-at-the-nanopore-fast5-format-f711999e2ff6)<br><br>- fast5 포맷은 HDF5 데이터 포맷에 기반하였으며, HDF5 데이터 포맷은 JSON 포맷과 동일하다.<br><br>- nanopore의 basecalling은 연구가 활발하다.<br><br>- 데이터 알고리즘에 사용되던 은닉마르코프모델(HMMs, hidden Markov model)이 신경망모델(neural network)로 대체되면서, 다양한 신경망 모델들이 nanopore의 basecalling tool 로 시험되고 있다.<br>- 또한 모델들을 훈련하는 방법들도 활발하게 연구되고 있다.<br><br>- nanopore는 회사에서 제공하는 production basecaller인 Guppy 뿐 아니라, 개발자들이 만든 Flappie, Scrappie, Taiyaki, Runnie, Bonito 같은 basecaller 도 사용할 수 있다.<br>- Guppy 처럼 회사에서 제공하는 basecaller 가 가장 정확하고 안정적으로 작동<br>- 개발자들이 만든 basecaller 툴들의 경우 특정 목적에 따라서 사용할 수 있다.<br><br>- 예를 들어 homopolymer accuracy, variant detection, or base modification detection 용도로. 그치만 개발자들의 툴은 속도나 데이터 생산량 부분에서 최적화가 잘 되어있지 않다. 따라서 회사에서 제공하는 툴에 대한 개선의 용도로 사용한다. 예를 들어 Scrappie의 경우 homopolymer를 정확하게 mapping할 수 있다.<br><br>- 아예 독립적인 데이터 알고리즘을 활용하는 툴로는 Chiron이 있다.<br><br>- 딥러닝 신경망을 활용한 basecaller<br><br>- Guppy 에 대한 업데이트가 정기적으로 행해지는걸 볼 때, basecalling은 현재 3세대 기술에서 활발하게 개발되는 부분이다.|[SMRT Sequencing: How It works](https://www.pacb.com/technology/hifi-sequencing/how-it-works/)<br><br>[HiFi Sequencing](https://www.pacb.com/technology/hifi-sequencing/)<br><br>- 형광신호는 영상의 형태로 연속적으로 기록된다.<br>- 템플릿이 원형이기 때문에, polymerase는 DNA 이중가닥의 양쪽을 반복적으로 읽는다.<br>- 형광신호를 pulse에 따라 추적한 뒤 세분화한다.<br>- pulse 를 base로 변환시켜 하나의 긴 read를 얻는다. (=polymerase read)<br>- long read는 subreads로 나누어진다.<br><br>- 각 subread는 linker sequence가 없이도 1개씩 library insert로 넘어간다.<br>- subread는 unaligned BAM file의 형태로 저장된다.<br><br>- Aligning 과정에서 subreads를 모아서 CCS(consensus circular sequences)로 사용한다<br>- SMRT basecallers are chiefly developed internally and require training specific to the chemistry version used.<br>- 현재 basecalling workflow는 "css" 이다.|
|Errors, correction, and polishing|- DNA fragment의 길이와 read quality가 상관이 없다.<br>- 핵산이 pore을 통과하는 속도가 최적화된 속도와 얼마나 가까운지가 퀄리티를 좌우한다.<br>- pore을 통과하는 속도는 sequencing의 후반부에서는 느려지는 경향이 있으며, 속도가 느려지면 퀄리티가 떨어지게 된다.<br>- SMRT가 read를 여러번 읽는 것에 반해, nanopore는 단 한번만 읽는 것으로 library를 구축한다.<br>- nanopore의 프로토콜은 '1D sequencing protocol', '1D2 protocol'이 있다.<br><br>- 1D sequencing protocol의 경우 double strand DNA의 가닥들은 각각 따로 읽혀지며, 한번 통과를 할 때의 퀄리티는 조정없이 바로 반영된다.<br>- 1D^2 protocol의 경우 double strand DNA에서 먼저 template strand를 읽은 뒤 곧바로 complement strand가 이어서 읽혀지도록 구성되어 있다. 두 퀄리티를 종합하여 계산함으로써 좀 더 정확한 sequencing을 할 수 있도록 한다.<br>- 2018년 논문에서 1D sequencing protocol로 single-pass 정확도의 중간값이 95%를 달했다고 했다.<br>- human genomic DNA NA12878 에 대한 1D sequencing protol의 정확도 중간값은 91% 였다.<br>- 반면 1D^2 sequencing protocol의 경우 정확도를 98%까지 올렸다.<br><br>- nanopore의 정확도는 linear fragment에서도 가능하다: 만약 같은 서열이 여러개 존재한다면 말이다.<br><br>- nanopore에서 rolling circle amplification을 활용한 반복적인 라이브러리 제작법은 SMRT sequencing과 사뭇 비슷하다. subread들 또한 퀄리티값을 증가시키기 위해 활용된다.<br>- Oxford nanopore technologies는 현재 circularisation이 아니라 isothermal polymerisation을 통해 linear fragemtn에서 퀄리티를 높이는 법을 고민하고 있다(?) ONT is developing a similar linear consensus sequencing strategy based on isothermal polymerisation rather than circularisation|- CCS 의 정확도가 fragment를 읽은 횟수에 많이 의존한다. (각 SMRT-bell molecule의 sequencing depth를 의미. 그림참조.)<br>- ?<br>- 예를 들어, 2017년에 PacBio가 내놓은 Sequel v2의경우, 10 kbp를 넘어가는 fragment의 경우 딱 한번만 읽을 수 있었고, 횟수의 제한 때문에 정확도는 85~87% 수준이었다.<br>- 2018년에 나온 v3의 경우 polymerase의 길이를 20 kbp 에서 30 kbp로 늘렸다.<br>- CCS에서 약 4번 통과시키면 Q20 99.9%를 기록하고, 9번을 통과시키면 Q30 99.9%를 기록한다.<br><br>- Q20 = 염기 100개를 불러울 때 1개 염기를 잘 못 불러올 확률<br>- Q30 = 염기 1000개를 불러울 때 1개 염기를 잘 못 불러올 확률<br><br>- 만약 에러가 임의적으로 발생하는게 아니라면, sequencing depth를 늘려서 해결할 수 있는 에러가 아니다.<br>- 반면, subread에서 일어나는 무작위의 sequencing error의 경우, subread에는 mismatch 보다는 indel이 더 많기 때문에, CCS, assembly, variant call과 같은 final outputs가 시스템적인 오차(bias)를 피해야한다....?????  <br>    (However, the randomness of sequencing errors in subreads, consisting of more indels than mismatches [52–54], suggests that consensus approaches can be used so that the final outputs (e.g. CCS, assembly, variant calls) should be free ofsystematic biases. Still, CCS reads retain errors and exhibit a bias for indels in homopolymers [18].|
|Chemistry, software|- nanopore에서도 indel과 subs가 어느정도 랜덤하게 발생한다.<br>- 현재 nanopore에서 보편적으로 사용하고 있는 R9 버전의 pore와 basecaller 의 경우에는 complexity가 낮은 구간에 대하여 분석이 어렵다. 이는 homopolymer sequence에 대해서도 마찬가지이다.<br><br>- 전류의 세기를 측정하는 것은 pore에 존재하는 k-mer 분자인데, homopolymer는 통과할 때 베이스가 바뀌지 않다보니 전류의 세기변화가 없다싶히 하고, 결국 베이스의 수가 틀리게 나온다.<br><br>- 2020년에 새로 나온 R10 버전의 pore의 우에는 homopolymer sequence 분석에서 발생했던 문제를 보완하기 위해 만들어졌다.<br><br>- 어떤 k-mer 분자들은 생산하는 신호의 특색이 다른 k-mer 분자들과 유별나게 다르기도 하다. 이런 경우는 결국 systematic bias를 야기한다.<br><br>- 시퀀스의 퀄리티는 basecaller와 basecaller를 훈련할 때 사용한 데이터베이스의 종류 연관이 깊다.<br>- 따라서 basecaller를 특정 데이터로 훈련시켜놓으면, 그 데이터와 유사한 샘플의 결과정확도가 올라간다.<br>- Oxford Nanopore Technologies는 정기적으로 chemistry와 software 업데이트를 내놓으며 read quality를 높이는데 노력하고 있다: pore의 경우 지난 3년간 9.4, 9.4.1, 9.5.1, 10.0 4개의 버전이 추가되었으며, 2019년에는 Guppy의 버전만 12번 업데이트 하였다.|Pacbio는 지난 3년간 새로운 기기 한 대를 선보였다(Sequel II). 또한 4개의 chemistry를 추가하였다(Sequel v2 and v3; Sequel II v1 and v2). 그리고 SMRT-LINK 분석 세트 버전 4개를 발표하였다.|
|Polishing|- nanopore는 Nanopolish 라는 방법을 사용한다.<br>- Nanopolish는 base modification 을 고려하면서 polishing 하는 것이 정확도를 높여준다고 설명한다.|SMRT는 Arrow 라는 방법을 사용한다.|
|Detecting structural variation|||

# Correction

- 현재 long-read sequencing의 정확도는 read의 genomic origin을 판별하기에 충분한 정도를 기록하고 있다.
- de novo assembly, variant calling, intron-exon boundaries 판별과 같은 특정 high base-level 정확도를 요하는 작업의 경우 application이 추가적으로 필요한 상황이다.
- long-read에서 sequencing error를 고치는 법은 현재 두 가지가 있다.

## Non-Hybrid

- long read 들을 여러개를 한데모아 하나의 긴 consensus read를 만들고, 이 read를 중심으로 각 read들을 대조하여 고친다.
- 이렇게 고쳐진 reads들은 다시 consensus read를 만들거나 다른 용도로 활용한다.
- k-mer filtering이라고 하여 값이 낮은 k-mer를 sequencing error로 판단하고 거르는 방법도 있으며, 대표적으로 wtdbg2 assembler 툴이 있다.

## Hybrid

- short-read data를 참고하는 방법
- alignment-based hybrid 방법의 경우 short reads는 long reads에 직접적으로 붙어서 에러를 확인한다.
- assembly-based hybrid 방법의 경우 short reads를 활용해 de Bruijin graph를 만들거나 조립한다. Long read는 조립한 것이랑 맞춰보거나 de Bruijn 그래프에 따라 나누어서 에러를 고친다.
- assembly-based hybrid 방법이 에러를 고치는 속도나 퀄리티에서 가장 뛰어났으며, 대표적으로 FMLRC 툴이 있다.