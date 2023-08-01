# 준비된 환경
1. Rocky Linux 9
	- Docker를 활용하여 windows11 환경에서 구축
2. 서버를 다루기 편하도록 docker와 Visual Studio Code와 연결시킴
	- VSCode의 docker 확장프로그램을 통하여 연결
	- Docker window의 bash 혹은 VSCode에서 bash 붙여넣기로 접속하면 관리자 계정으로 접속하는게 아님. 그렇게 접속하면 cluster system에 접속할 때 처럼 bash가 뜬다. (`sh-5.1#`)
	- VSCode의 open a remote window를 통해서 열면 서버 디렉토리도 확인할 수 있고, 서버 내 bash도 올바르게 연결해준다.
# 1. 자주 사용하는 기본적인 패키지, 라이브러리 설치
## 기본상식: yum? dnf? apt? sudo?
- `yum`과 `apt`는 모두 패키지 설치 관리자다. 다만 같은 리눅스 계열이라 할지라도 어느 리눅스 시스템을 쓰느냐에 따라 다른 패키지 설치 관리자를 사용하게 된다.
- `yum`은 Rocky Linux 9와 같은 '레드헷 리눅스(RHEL)' 계열의 리눅스 시스템의 패키지 설치 관리자이다.
	- RHEL에는 대표적으로 Centos 시리즈가 잘 알려져있다.
- `dnf`는 RHEL 계열 중에서도 버전 8 이상부터 지원하는 패키지 설치 관리자이다. `yum`을 사용하는 방식과 똑같이 사용할 수 있다. 다만 상대적으로 RHEL8 이상 버전이 아직 널리 쓰이지 않아서 많은 인터넷의 팁들이 `yum`으로 명령어를 소개하고 있다. Rocky Linux의 경우 RHEL9 계열이므로 당연히 dnf로도 설치가 가능하다.
- `apt` 패키지 설치 관리자는 Ubuntu에서 사용되는 패키지 설치 관리자다.
	-  RHEL계열에서 기본적으로는 사용되지 않는다.
- `sudo`는 패키지의 한 종류로, 비밀번호만 알고 있다면 일반 사용자도 관리자 권한으로 명령어를 수행할 수 있게 해준다. 리눅스 시스템 계열과 상관없이 사용할 수 있지만, Rocky Linux에는 기본적으로 설치가 되어있지 않 패키지라 직접 설치해줘야한다.
# 기본적으로 다운받은 패키지들
모든 명령어는 일반사용자가 아닌 root 사용자로 로그인한 상태에서 진행하였다.
## which
`yum install which`
## python
 `yum install python`
## pip
`yum install pip`
## wget
`pip install wget`
## sudo
`yum install sudo`
## vim
`yum install vim`
## unzip
`yum install unzip`
# 2. 막무가내로 GATK부터 설치
## GATK를 설치해보자
- Anaconda로 받거나, 공식 github에서 clone으로 받거나, docker image로 받거나 여러 방법이 있다.
	- [Getting started with GATK4](https://gatk.broadinstitute.org/hc/en-us/articles/360036194592-Getting-started-with-GATK4)
- 그러나 해당 방법들은 다시 추가적인 환경 구축을 요구한다 -> 귀찮다
- 간단하게 파일만 받아서 설치하자.
- [GATK github /release](https://github.com/broadinstitute/gatk/releases)
	- 파일을 다운 받는다.
	- `unzip gatk-4.4.0.0.zip`
	- 끝
- 대신 수동설치는 최신버전을 받기 위해서 주기적으로 수동설치를 요구한다는 단점 아닌 단점이 있다.
	- 파이프라인의 안정성 유지와 최신 버전을 통한 성능향상은 모두 중요하다.
	- 최신 버전이 항상 더 나은 퍼포먼스를 약속하지 않으며, 예상치 못한 버그를 일으킬 수 있다.
## GATK를 위한 필수프로그램들을 다운받자
[GATK github #requirements](https://github.com/broadinstitute/gatk#requirements)
- GATK를 run하기 위한 필수항목과 build하기 위한 필수항목이 다르게 적혀있다. 이번에는 run만을 위한 프로그램만 설치한다.
1. 특정 버전의 JAVA
	- 4.4.0.0 버전의 경우 OpenJDK 17 버전을 요구하고 있다.
	- 향후에 요구사항이 바뀔 수 있으니 설치 전에 항상 requirement 부분을 잘 읽어보자
	- [install openjdk17 on centos RHEL 7](https://computingforgeeks.com/install-java-openjdk-17-on-centos-rhel-7/?expand_article=1)
	- `wget https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.rpm`
	- `yum -y install ./jdk-17_linux-x64_bin.rpm`
	- 버전확인도 수행하자
```shell
# java --version
java 17.0.8 2023-07-18 LTS
```
2. Python
	- 이미 설치했다
3. R
	- R은 잘 알려진 통계 및 그래프 그리기에 특화된 프로그램이다.
	- Centos, Rocky Linux와 같은 RHEL 계열의 패키지 설치 관리자는 기본적으로는 R을 제공하지 않는다.
	- 대신, Powertools라고 하여 개발자 전용 패키지를 추가로 설치하여 주면, R이 포함되어 있다.
	- `yum install epel-release`
	- `yum config-manager --set-enabled crb` 
	- `yum install R`
## GATK가 정상적으로 실행되는지 확인해보자
- gatk가 설치되어 있는 디렉토리에서 gatk를 찾는다.
	- 만약 이 과정이 귀찮다면, gatk를 bash enviroment에 추가하는 방법도 있다. 다만 개인적으로 필수적이거나 설치 과정 중에서 자연스럽게 추가되지 않는 경우에는 지양하는 편이다.
- 나의 경우 `/download/gatk-4.4.0.0` 디렉토리에 gatk가 들어있었다.
- `--list` 를 통하여 GATK를 돌려본다.
```shell
# /download/gatk-4.4.0.0/gatk --list
Using GATK jar /download/gatk-4.4.0.0/gatk-package-4.4.0.0-local.jar
Running:
    java -Dsamjdk.use_async_io_read_samtools=false -Dsamjdk.use_async_io_write_samtools=true -Dsamjdk.use_async_io_write_tribble=false -Dsamjdk.compression_level=2 -jar /download/gatk-4.4.0.0/gatk-package-4.4.0.0-local.jar --help
USAGE:  <program name> [-h]

Available Programs:
...
```
- 이렇게 프로그램 목록이 쫙 뜨면 성공이다.