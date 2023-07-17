[개발 서버 무료로 구하는 법 9가지](https://brunch.co.kr/@topasvga/705)   
[1.(시작) 구글 Cloud 가입과 서버 1대 받기](https://brunch.co.kr/@topasvga/168)   
[구글 클라우드 플랫폼에 Docker로 웹서버 띄우기](https://kibbomi.tistory.com/241)   
[Google Cloud Machine Type에 대해 알아보기 (E2, N2, N2D, N1)](https://hwan-hobby.tistory.com/8)   
[머신 계열 리소스 및 비교 가이드](https://cloud.google.com/compute/docs/machine-resource?hl=ko)    
[Google의 Container-Optimized OS를 실행하는 Compute Engine 인스턴스 만들고 구성하기](https://cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance?hl=ko)    
[구글 클라우드 플랫폼](https://blog.naver.com/rayhaha/223000083672)    
[Docker 설치하고, Docker로 웹 어플리케이션 배포해보기](https://wnsgml972.github.io/setting/2020/07/20/docker/)    
[Docker - 이미지 생성/배포하기](https://youngjinmo.github.io/2019/10/docker-image/)    
[windows 11에 docker 설치하기 (wsl2 이슈 해결)](https://herojoon-dev.tistory.com/120)    
[이전 버전 WSL의 수동 설치 단계](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)    
[Import Rocky Linux to WSL](https://docs.rockylinux.org/guides/interoperability/import_rocky_to_wsl/#import-rocky-linux-to-wsl "Permanent link")    
[도커와 컨테이너의 이해](https://tech.cloudmt.co.kr/2022/06/29/%EB%8F%84%EC%BB%A4%EC%99%80-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88%EC%9D%98-%EC%9D%B4%ED%95%B4-1-3-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88-%EC%82%AC%EC%9A%A9%EB%B2%95/)    
[[Docker] 도커로 Centos 다루기](https://velog.io/@dailylifecoding/docker-install-centos-and-run-basic)    
# 목표
1. Docker container에 QIIME, scRNA-seq 분석이 가능한 파이프라인 구축
3. 생성한 docker container를 Google cloud에 적용하고 시험
4. Google cloud 3개월의 무료 체험이 끝나면 docker container만 다른 클라우드 서비스로 이동

# 과정
## 1. Windows11에 Docker desktop설치
https://docs.docker.com/desktop/install/windows-install/
## 2. Linux 시스템의 image를 받고 container run까지 한 명령어로 끝내기
- Docker에 Centos, Ubuntu, Rocky Linux같은 시스템을 받은 다음, container를 생성하여 virtual machine을 사용하는 것과 비슷하게 환경을 구축하기로 결정하였다.
	- Docker는 프로세스를 격리하는 container 역할을 해주므로 엄밀하게 virtual machine이라고 말할 수는 없다.
	- 다만 OS system으로 container를 처음부터 생성하고 이를 기반으로 개발환경을 구축해간다면 이와 비슷한 효과를 낼 수 있다고 생각된다.
	- 재밌는 점은, WSL에 linux system을 설치하고 그 안에 docker를 실행하는 것도 가능하고, 심지어 docker 안 container에 있는 linux system에서 다시 docker를 중복으로 실행하는 것도 가능하다.
- 어느 Linux 시스템을 선택할 것인가?
	- RHEL 계열의 Rocky Linux를 사용하기로 결정하였다.
	- Centos가 유료 stream version 외에는 유지보수를 종료한다는 점과, Centos 개발진이 오픈소스 무료 linux system으로 배포한다는 점이 좋았다.
- Docker에 설치는...
	1) Powershell에서 명령어를 사용하는 방법, 혹은
	2) Windows에서 UI환경의 Docker desktop을 활용하는 방법이 있다.
	- 다만, linux system을 설치하는 경우 interactive 옵션(-i)과 TTY 옵션(-t)을 켜지 않으면 command terminal의 충돌로 container가 실행되지 않는다.
	- 위 옵션을 Docker desktop에서 키는 방법을 알 수 없었다.
	- 인터넷에서 조사를 했을 때 대부분의 경우 아직 1) 처럼 shell 명령어로 설치가 이루어지고 있었다.
### Powershell 명령어를 사용하여 설치하기
```shell
docker run --name RockyLinux9_test --hostname ROCKY -it rockylinux:9
```

# 번외: Docker에 Rocky Linux image 받아오기
- `docker run` 명령어의 경우 image가 없으면 자동으로 다운받는 과정이 포함되어 있다.
- 만약 container를 생성하지 않고 image만 받고 싶은 경우, 다음과 같이 가능하다.
- Docker hub에서 자신이 원하는 linux system을 검색한 뒤, image를 받는 것이 가능하다. [#](https://hub.docker.com/_/rockylinux)
- Docker desktop 가장 상단의 검색창에서 받고 싶은 image를 검색한 다음, `Pull`을 눌러서 다운받 것도 가능하다.
- 어떤 이름(태그)으로 다운받아야 하는지 확인한 다음, Powershell을 열어서 다음의 명령어를 수행한다
```shell
docker pull rockylinux:9
```
- Docker window 프로그램에서 Images 메뉴를 보면 Rocky Linux가 추가된 것을 알 수 있다.
	- 혹은 Powershell에서 `docker images -a` 명령어로 확인할 수 있다.
	```shell
PS C:\WINDOWS\system32> docker images -a
REPOSITORY                 TAG       IMAGE ID       CREATED       SIZE
rockylinux                 9         eeea865f4111   7 weeks ago   176MB
	```
### 참고로...
>*"The `rockylinux:latest` tag is intentionally missing. Please choose a major version (currently 8 or 9) tag, or a more specific tag to ensure you are pulling the version of Rocky Linux you want: e.g. `rockylinux:8` or `rockylinux:9`"*
- 보통은 `docker pull rockylinux`라는 명령어로 쉽게 최신 버전을 받을 수 있지만, 2023년 7월 기준으로 불가능하다. 따라서 뒤에 태그로 `:9`를 적어줘야 한다.    

- Rocky Linux가 두 버전이 검색되서 혼란이 가중되었다.
	- Docker Official Image로 배포되는 것  [#](https://hub.docker.com/_/rockylinux)
	- Sponser OSS로 배포되는 것 [#](https://hub.docker.com/r/rockylinux/rockylinux)
- 두 배포처의 주소가 조금 다르다.
	- Official image의 경우 다운받기 위해서는 rockylinux 뒤에 tag를 적어주지 않으면 latest 버전이 없다는 에러가 뜨면서 다운이 되지 않는다. 단순하게 9를 tag로 사용할 경우 최신버전인 9.2로 다운되었다. (`rockylinux:9)
	- Sponser OSS에서도 9.2버전을 받을 수 있지만 따로 tag를 해줘야 한다(`rockylinux/rockylinux:9`)
	- 태그를 하지 않을 경우 Sponser OSS에서는 8.6버전을 받았다(`rockylinux/rockylinux`)


# 번외: WSL2에 Rocky Linux 설치
- Rocky linux를 windows11에서 사용하기 위해서는
	1) WSL2(Windows Subsystem for Linux) 설치
	2) Rocky linux 사이트에서 최신버전 tar.xz 파일 다운로드
	3) Powershell에서 WSL2를 통해 os import 수행
```shell
wsl --import RockyLinux9 <Rocky Linux 설치할 장소. 나의 경우 C:\Users\사용자\rockylinux> <다운받은 tar.xz 파일 위치> --version 2
```
- 이제 rocky linux를 powershell이나 visual studio code에서 실행한 다음 `docker`명령어를 실행하면 옵션이 떠야한다.
```shell
[root@SurfacePro8 system32]# docker

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Common Commands:
  run         Create and run a new container from an image
  exec        Execute a command in a running container
  ps          List containers
  ...
```