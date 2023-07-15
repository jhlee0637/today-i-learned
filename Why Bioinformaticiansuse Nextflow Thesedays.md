[Wikipedia: Nextflow](https://en.wikipedia.org/wiki/Nextflow)   
[Nextflow & Clara Parabricks](https://blog.naver.com/jinp7/222996328340)   
[Reddit: Does everyone use Nextflow thesedays?](https://www.reddit.com/r/bioinformatics/comments/sc8e0i/does_everyone_use_nextflow_thesedays/)   
[Reddit: Nextflow vs Snakemake](https://www.reddit.com/r/bioinformatics/comments/wazatv/nextflow_vs_snakemake/)   
[nf-core/rnaseq](https://nf-co.re/rnaseq/3.12.0)   
[Bioinformatics Tools: Nextflow & SnakeMake](https://medium.com/@MarinaBioinfoStarter/bioinformatics-tools-nextflow-snakemake-how-they-are-integrated-with-ci-cd-pipeline-c9f02781ccf7)   
[Snakemake vs Nextflow](https://labs.epi2me.io/snakemake-vs-nextflow/)   
[Workflow management systems in Bioinformatics](https://biomadeira.github.io/2022-10-25-workflow-management)   
# What is Nextflow
- Nextflow was originally developed at the Centre for Genomic Regulation in Spain and released as an open-source project on GitHub in July 2013.
- Workflow Management System
- Choose workflows(pipelines) on your purpose [#](https://nf-co.re/pipelines)
	- RNAseq
	- Amplicon Target Sequencing(microbial)
	- CRISP data
	- Nanostring   
	  ...
- Language: Groovy programming language
	- Java's extension
	- Similar with Python, Ruby, Smalltalk
- Cloud familiar
	- AWS[#](https://www.nextflow.io/docs/latest/aws.html)
	- Google Cloud[#](https://www.nextflow.io/docs/latest/google.html)[#](https://cloud.google.com/life-sciences/docs/tutorials/nextflow?hl=ko)
	- Azure Cloud[#](https://www.nextflow.io/docs/latest/azure.html)   
	  ...
- Container familiar[#](https://www.nextflow.io/docs/latest/container.html#)
	- Docker[#](https://www.nextflow.io/docs/latest/container.html#docker)
	- Sarus[#](https://www.nextflow.io/docs/latest/container.html#sarus)   
	  ...
# Workflow example: nf-core/rnaseq [#](https://nf-co.re/rnaseq/3.12.0)
- Pre-designed pipeline for RNA-seq
- You can choose methods on you desires (change some tools in some stages)
- Input...
	- a samplesheet
	- FASTQ files
- Perform...
	- quality control (QC)
	- trimming
	- (pseudo-)alignment
- Produce....
	- a gene expression matrix
	- extensive QC report
## Stage
1. Pre-processing
2. Genome alignment & quantification
3. Pseudo-alignment $ quantification
4. Final QC
# "Is Nextflow better than Snakemake?"

> *"...The popularity of **Python** among the Bioinformatics community would suggest **Snakemake** would be the most adopted option, but it turns out that **Nextflow** **is very popular** and the choice of many researchers and groups."* [#](https://biomadeira.github.io/2022-10-25-workflow-management)

## What is Snakemake
- Another Workflow Managerment System
- Pythonic

## Snakemake vs Nextflow?
- Snakemake is Python-like
- Snakemake needs user to pre-understand of Python
- Snakemake may need to install other tools first(conda, mambaforge)
- Snakemake is integrated with other bioinformatics tools such as BioConda, Maba

- Nextflow is UNIX-like
- Nextflow is easy to install, easy to learn
- Nextflow is well documentized 
- Nextflow has an active community

- Both systems enable the automatic parallelization of jobs and automatic retrying of failed jobs.
- Both workflow management systems support cloud execution via Kubernetes.

- Snakemake is faster than Nextflow(Dec 2022)
- Snakemake supports dry-run execution testing
- Nextflow onyl supports on selected commands