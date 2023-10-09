[He J, Lin L, Chen J. Practical bioinformatics pipelines for single-cell RNA-seq data analysis. Biophys Rep. 2022 Jun 30;8(3):158-169. doi: 10.52601/bpr.2022.210041. PMID: 37288243; PMCID: PMC10189648.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10189648/)
# Single Cell Isolating Method
## 1. Plate method(=microfluidic based method)
- Isolate through The Fluorescene-Activated Cell Sorting(FACS)
- Isolate 50~500 cells
- High sensitivity(reliably 10,000 genes per cell)
## 2. Droplet based method
- Barcode, tag transript
- Unique Molecular Identifiers(UMI): less time, less cost
- Isolate ~ 10,000 cells
- 1,000 ~ 3,000 genes per cell
- Dropout: expressed genes' transcripts -> not detected

# Considered factors to choose method
## 1. Number of cells
- target cell type -> effects on proportion in sample
## 2. Cell size
- Check platform's limitation
- Small size(under 25μm in diameter) cells are easy and give minimal damage
- Bigger or irregular shape cells need different apporoach
	- ex. snRNA-seq: only for nuclear transcript 
## 3. Technical biases
# Preprocessing
## 1. QC
- *FASTQC*
## 2. Trimming
- *Trimmomatic*
- *cutadapt*
- Cutting adapter and bad quality reads
## 3. Count gene expressions
- Each cells and each genes
- Tools for non-UMI and non-barcoded data
	- Use traditional bulk RNA-seq quantification tools
		- *RSEM*
		- *STAR*
		- *HTSeq*
	- Use traditional tools for downstream process also
- Tools for UNI and bardcoded data
	- *CellRanger*
	- *STARsolo*
	- *STARsolo* was faster
- Caution: nearly all quantification tools are genee-centric
	- *'We think a single-cell transpasable elements(TEs) are more importat'*
# Quality Control
## 1. QC for cell
1) Exclude barcodes from dead cells and floating RNA
	- Compare the counts between UMIs, expressed genes, total detected counts, and proportion of RNA from mitochondrial genes
2) Remove Doublets and Multiplets
	- Doublets and Multiplets are cell barcodes, corresponding more than one cell
	- Check if there are too many counts or expressions
	- Hard to remove them correctly
		- Because the doublets often harbor 'hybrid' expression
	- Tools
		- *scrublet*
		- *DoubleFinder*
		- *scds*
## 2. QC for gene
- QC for 20,000 ~ 50,000 genes
- Need to remain only desired gene
	- Filter in genes only from few cells or
	- Filter out not informatics cells
	- To filter, use the minimum cell cluster size of interest
- Need to consider droplets
- 'We don't recommend gene QC'
	- Hard to set threshold
	- Lie in danger of filter out the gene that could be informtative
# Norrmalization
- Reads between cells are different, and give negative effect to analysis
- To avoid it, we must correct them(normalization)
- Commonly depth scaling
- Tools
	- *scran package*
	- *scone tool*
	- *scran package* was best, and *scone tool* provided specialized method based on data
- If some RNA is not caputerd, try to use spike-ins, but not recommend
# Feature Selection
- From droplet method, one cells's transcriptome is low and makes noise from data
- To remove the noise, we can use dimensional reduction, clustering, etc
	- Need to select Highly Variable Genes(HVGs)
		- HVGs can be identified by fitting the variance-mena of each gene by a Generalized Linear Model(GLM)
		- The gene which has high level variance is important
			- So how to estimate gene variance?: Standard Deviation, Square Coefficient of Variance
			- prefer the gene with larger mean expression value
- *Giniclust*
	- uses 'Fano factor' and 'Gini index' to find rare cell type
# Dimensionalit reduction, Visualization
- scRNA-seq dataset has high-dimension (one gene - one dimension)
	- It must be reduced into 2~3 dimensions
## Strategies of dimensionality reduction
### 1. Linear Algorithm
- Principal Component Analysis (PCA)
	- perserves Euclidean distance between cells
	- common for bulk RNA seq
	- But, cellular relationships can't be analyzed well
	- and direc visualization from high throughput
### 2. Non-linear Algorithm
# Batch Correction