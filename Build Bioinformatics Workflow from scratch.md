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