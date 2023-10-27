[Learn Nextflow in 2023](https://www.nextflow.io/blog/2023/learn-nextflow-in-2023.html#)
# Before you start
- Be familar with
	- Linux command
	- Python or Perl
	- Some biology
# Meet the Tutorials!
## 1. Basic Nextflow Community Training
[Basic Training](https://training.nextflow.io/basic_training/)
[YouTube Playlist(7hrs): Community Nextflow & nf-core Foundational Training](https://youtube.com/playlist?list=PL3xpfTVZLcNiLFLiDqk_H5b3TBwvgO_-W&si=Km51foYLlUM19nJ3)
### Environment setup
- You can start Nextflow by 1) local installation or 2) Gitpod
- For this tutorial, local installation require something like
	- Bash
	- Java 11
	- Git
	- Docker
	- Singularity 2.5.x (or later)
	- Conda 4.5 (or later)
	- Graphviz
	- AWS CLI
	- A configured AWS Batch computing environment
- Meanwhile, Gitpod requires only
	- Github ID
	- Internet
- I chose Gitpod as I am not familiar with AWS
- Gitpod is online based IDE service
- Not 100% free, but offer around 50 hours as credits monthly
- Visit [https://gitpod.io/#https://github.com/nextflow-io/training](https://gitpod.io/#https://github.com/nextflow-io/training), connect Git ID to Gitpod
- Get your own workplace to practice Nextflow
- Test the environment
``` bash
nextflow info
```
- I didn't roll back the version to the previous version as like the tutorial recommended. I guess there are some bugs with JAVA when you follow the tutorial with the old version.
## Introduction
- Nextflow is a workflow orchestration engine and domain-specific language (DSL) that makes it easy to write data-intensive computational workflows.
### Processes and Channels
-  `process` takes input data and give output data
	- `process` includes command or `script` which has to be executed
- `channel` is where the data come in
### Execution abstraction
- Executor is where the Nextflow run
- There would be local executor like your computer
- Or, High-Performace Computing(HPC), Cloud platform would be
- Good thing is that you don't need to modify the workflow only for local computer or cloud. They run same in every platform. Just need to define the target platform.
### Scripting Language
- DSL
- Nextflow scripting is an extension of the Groovy programming language which, in turn, is a super-set of the Java programming language.
## Your first script
**hello.nf**
```groovy
#!/usr/bin/env nextflow

params.greeting = 'Hello world!' 
greeting_ch = Channel.of(params.greeting) 

process SPLITLETTERS { 
    input: 
    val x 

    output: 
    path 'chunk_*' 

    script: 
    """
    printf '$x' | split -b 6 - chunk_
    """
} 

process CONVERTTOUPPER { 
    input: 
    path y 

    output: 
    stdout 

    script: 
    """
    cat $y | tr '[a-z]' '[A-Z]'
    """
} 

workflow { 
    letters_ch = SPLITLETTERS(greeting_ch) 
    results_ch = CONVERTTOUPPER(letters_ch.flatten()) 
    results_ch.view { it } 
} 
```
- run the code
```bash
nextflow run hello.nf 
#N E X T F L O W  ~  version 23.10.0
#Launching `hello.nf` [confident_mclean] DSL2 - revision: 197a0e289a
#executor >  local (3)
#[bd/de1214] process > SPLITLETTERS (1)   [100%] 1 of 1 ✔
#[cc/562f4f] process > CONVERTTOUPPER (1) [100%] 2 of 2 ✔
#WORLD!
#HELLO 
```