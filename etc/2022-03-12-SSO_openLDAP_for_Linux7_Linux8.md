---
layout: post
title: "openLDAP를 이용한 SSO 시스템 구축 (Linux 7, Linux 8)"
subtitle: "여러 서버의 아이디와 비밀번호를 한번에 관리하는 법"
date: 2022-03-12
author: "Lee Je Hee"
URL: "/2022/03/12/openLDAP_SSO_Linux/"
published: True
tags:
 - openLDAP
 - Linux 7
 - Linux 8
 - Rocky Linux 8
 - SSO
---

# Single Sign-On(SSO) 시스템이 필요한 상황은?
최근 새로운 서버가 여러 대 들어왔다.\
이렇게 서버가 들어오고 나가는 과정 중에서 사용자들을 매번 새로 등록해야 하는 문제가 생겼다.\
많은 서버, 많은 사용자들 ... 그리고 퇴사자가 발생하면 모든 서버에 하나하나 접속해서 삭제해야하는 상황까지 발생했다.

Single Sign-On(SSO)시스템은 여러 Linux 환경에서 많은 사용자와 그룹을 관리할 때 유용하다.\
여러 사용자의 정보를 하나의 Linux 서버에서 저장하고, client가 되는 Linux 서버로 이를 배포하는 방식이다.\
따라서 한번만 아이디와 그룹 정보를 수정하면, 다른 Linux 서버들로 자동으로 수정된다.

좀 더 자세하게 설명을 하고 싶지만 나보다는 보안 전문가들의 설명을 듣는 것이 더 옳다고 생각되기 때문에, 해당 시스템을 구축하면서 참고하였던 링크들을 이 글 최하단에 첨부할 예정이다.

# 설치 전 주의점 1. Linux 7, Linux 8
SSO 시스템을 구축하면서 맞닥뜨린 가장 큰 문제 중 하나는 Linux 서버 별로 OS가 달랐다는 것이다.\
제목에는 7부터 언급했지만 Centos 6을 사용하는 Linux 서버도 있었다.\
해당 Linux 서버는 곧 폐기할 예정이라 손대지 않았다.\
이 글을 보게될 사람들 중에 Linux 6을 사용하고 있는 사람들이 얼마나 있을지는 모르겠지만,
만약 Linux6 환경인 경우에는 다른 글을 구글링하기를 바란다.

2022년 4월을 기준으로 openLDAP에 대한 대부분의 한국어 포스트는 먼저 openLDAP를 Linux 7에 설치한 후, 이를 Linux 7 기반의 다른 Linux서버에 배포하는 방식을 설명한다.

![][/img/2022_05/linux7to7.png]


그러나 나의 경우는 아래의 그림과 같이 일부 client 서버가 새로 들여온 **Rocky linux 8**이 설치되어 있는 상황이었다.

![][/img/2022_05/linux7to8.png]
따라서 Linux 8, 그 중에서도 Centos 8이 아닌 Rocky linux 8을 client 서버로 삼는 경우를 이 포스트에서 설명하고자 한다.

# 설치 전 주의점 2. SELinux off
설치하는 환경에 따라 다르겠지만 SELinux를 전부 끄거나 일부분만 선택적으로 끄지 않으면 openLDAP 서버와 client 서버가 정상적으로 동기화되지 않을 수 있다.

당연히 SELinux를 끄면 보안에서 문제가 생긴다.\
[이 블로그](https://it-serial.tistory.com/entry/Linux-SELinux-%EA%B0%9C%EB%85%90-%EA%B4%80%EB%A0%A8-%EB%AA%85%EB%A0%B9%EC%96%B4)에서 말하듯이 '보안이 취약하면 편리가 증가한다'는 점을 명심하고,\
보안 상 문제는 없는지 점검하면서 주의 깊게 진행하기를 바란다.

# 설치 전 주의점 3. 보안 인증서(CA)
openLDAP의 경우 인증서 사용 여부를 결정할 수 있다.\
이 또한 보안과 직결된 부분이기 때문에 주의 깊게 진행해야 한다.\
만약 `ldap_sasl_bind(SIMPLE): Can't contact LDAP server (-1)` 과 같은 오류가 발생할 경우 인증서 관련한 오류일 수 있다.\
이때는 올바르게 인증서를 설정하거나, 혹은 인증서를 삭제하기 위하여 `/etc/openldap/ldap.conf` 파일을 수정하기를 바란다.

# 1. openLDAP 설치
LDAP 서버에 필요한 패키지를 설치한다.

```shell
yum instal -y openldap openldap-clients openldap-servers
```

openLDAP 서버를 실행한다.
```shell
$ systemctl start slapd --now

# openLDAP가 389 포트를 사용하면서 정상적으로 돌아가고 있는지 확인
$ netstat -tnlp| grep -i 389
```

관리자 비밀번호로 삼을 비밀번호를 생성한다.
```shell
$ slappasswd
"New password:
Re-enter new password:
{XXXX}XXXXXXXXXXXXXXXX00XXXXXX00XX00XX"

```

LDAP 서버 설정을 위한 파일 `conf.ldif`를 생성하여 편집한다.\
설정은 host명 '**exampleserver**'라고 가정하고 작성하겠다.\
openLDAP 관리자의 계정 이름은 '**admin**'으로 작성하겠다.
```shell
$vim conf.ldif
```

```python
dn: olcDatabase={2}hdb,cn=config
changetype: modify
replace: olcSuffix
olcSuffix: dc=exampleserver   # 호스트 이름.
							  # 만약 "my.com"인 경우에는 "dc=my,dc=com"을 적는다

dn: olcDatabase={2}hdb,cn=config
changetype: modify
replace: olcRootDN
olcRootDN: cn=admin, dc=exampleserver #openLDAP 관리자 admin

dn: olcDatabase={2}hdb,cn=config
changetype: modify
replace: olcRootPW
olcRootPW: {XXXX}XXXXXXXXXXXXXXXX00XXXXXX00XX00XX #관리자 비밀번호를 적는다.

```

LDAP 서버에 conf.ldif 파일을 업로드한다.
```shell
$ ldapmodify -Y EXTERNAL -H ldapi:/// -f conf.ldif
```

LDAP 서버 설정을 위한 파일 `monitor.ldif`를 생성하고 편집한다.\
해당 파일에는 admin 계정 이름과 호스트명을 주의해서 적어준다.
```python
$vim monitor.ldif
```

```python
dn: olcDatabase={1}monitor,cn=config
changetype: modify
replace: olcAccess
olcAccess: {0}to *
	by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external, cn=auth" read
	by dn.base="cn=admin, dc=exampleserver" read
	by * none
```

LDAP 서버에 monitor.ldif 파일을 업로드한다.
```shell
$ldapmodify -Y EXTERNAL -H ldapi:/// -f monitor.ldif
```

이제 예제 DB를 이용한 openLDAP DB 구성한다.\
`/usr/share/openldap-servers/DB_CONFIG.example` 위치에 예제 DB가 구성되어져 있다.\
```shell
$cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
$chown ldap:ldap /var/lib/ldap/
```

기타 파일들을 LDAP 서버에 업로드한다.
```shell
$ ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/cosine.ldif
$ ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/nis.ldif
$ ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/inetorgperson.ldif
```

LDAP 서버 설정을 위한 `base.ldif`파일을 생성하고 편집한다.\
이 파일은 가장 중요한 파일이라고 할 수 있다.\
이 파일에서 사용자 혹은 그룹을 어떻게 명명할지 결정할 수 있다.\
여기서는 사용자는 'People', 그룹은 'Group'으로 명명한다.
```shell
$vim base.ldif
```

```python
dn: dc=labgeserver
dc: my
objectClass: top
objectClass: domain

dn: cn=admin, dc=exampleserver
objectClass: organizationalRole
cn: admin
description: LDAP Manager

dn: ou=People, dc=exampleserver
objectClass: organizationalUnit
ou: People

dn: ou=Group, dc=exampleserver
objectClass: organizationalUnit
ou: Group
```

LDAP 서버에 base.ldif 파일을 업로드한다.
```shell
$ ldapadd -x -W -D "cn=admin, dc=exampleserver" -f base.ldif
'Enter LDAP Password:
adding new entry "dc=exampleserver"

adding new entry "cn=admin,dc=exampleserver"

adding new entry "ou=People,dc=exampleserver"

adding new entry "ou=Group,dc=exampleserver"'
```

LDAP 권한을 설정한다.
```shell
$ authconfig --enableldap --enableldapauth --ldapserver=<서버이름> --ldapbasedn="dc=exampleserver" --enablemkhomedir --update
```
[참고](https://hostadvice.com/how-to/how-to-set-up-ldap-authentication-with-openldap-on-centos-7/)

여기까지 정상적으로 수행했다면 LDAP 서버는 모두 설치한 것이다.

# 2. 사용자의 추가
사용자ldif 파일을 작성한 뒤 `ldapadd` 명령어를 통하여 업로드 한다.\
한 ldif 파일에 여러 사용자 내용을 작성한 뒤 한번에 업로드할 수도 있다.

### 사용자 ldif 파일 생성
```shell
$vim add_user.ldif
```

### 사용자 ldif 파일 작성
```python
dn: uid=<사용자이름>,ou=People,dc=exampleserver
objectClass: top
objectClass: account
objectClass: posixAccount
objectClass: shadowAccount
cn: <사용자이름>
uid: <사용자이름>
uidNumber: <사용자 uid>
gidNumber: <사용자가 들어갈 그룹의 gid>
homeDirectory: /home/<사용자이름>        <- 변경할 수 있음
loginShell: /bin/bash        <- 변경할 수 있음
gecos:        <- 안 적는 경우 id와 동일한 값을 줌
userPassword: {crypt}x
shadowLastChange: 17058        <- 1970년 1월 1일 기준으로 며칠이 지났는지 계산.
                                  ShawdowMin은 이 값에서부터 시작.
                                  오늘 날짜로 해버리면 오늘은 비밀번호 못 바꿈. shadowMin: 0
shadowMax: 99999
shadowWarning: 7
```

### 새 사용자 ldif 파일 업로드
```shell
ldapadd -x -W -D "cn=admin,dc=exampleserver" -f add_user.ldif
'Enter LDAP Password: 
adding new entry "uid=<사용자이름>,ou=People,dc=exampleserver"'
```

### 사용자 비밀번호 설정
```shell
$ ldappasswd -x -D "cn=admin,dc=exampleserver" -W -S "uid=<사용자이름>,ou=People,dc=exampleserver"
```

# 3. 그룹의 추가
그룹 ldif 파일을 작성한 뒤 `ldapadd` 명령어를 통하여 업로드 한다.

한 ldif 파일에 여러 그룹 내용을 작성한 뒤 한번에 업로드할 수도 있다.

### 그룹 ldif 파일 생성
```shell
$vim add_group.ldif
```

### 새 그룹 ldif 파일 작성
```python
dn: cn=<그룹이름>,ou=Group,dc=exampleserver
objectClass: top
objectClass: posixGroup
gidNumber: <그룹 gid>
```

### 새 그룹 ldif 파일 업로드
```bash
ldapadd -x -W -D "cn=admin,dc=exampleserver" -f group_IMS.ldif
'Enter LDAP Password: 
adding new entry "cn=<그룹이름>,ou=Group,dc=exampleserver"'
```

여기까지 잘 수행한 경우 사용자와 그룹이 정상적으로 작성된 것이다.

# 4. 사용자&그룹의 삭제 및 수정
### 사용자&그룹의 삭제
```shell
ldapdelete -D "cn=admin,dc=exampleserver" -W "uid=<사용자명>,ou=People,dc=exampleserver"
ldapdelete -D 'cn=admin,dc=exampleserver' -W "cn=<그룹명>,ou=Group,dc=exampleserver"
```

### 사용자&그룹의 수정
내용의 수정은 `.ldif` 파일을 생성한 뒤, LDAP 서버에 `ldapmodify` 명령어로 올리는 방식이다.

예시로 'guest_group'이라는 그룹 안의 'guest01' 유저를 삭제해보겠다.

먼저 다음과 같은 내용의 ldif 파일을 생성한다.

```python
dn: cn=guest_group,ou=Group,dc=exampleserver
changetype: modify
delete: member
member: uid=guest01
```

그 다음 `ldapmodify` 명령어로 해당 파일을 올린다.

```shell
ldapmodify -W -D "cn=admin,dc=exampleserver" -f modify_1.ldif
```

ldif 파일에서 세번째 줄의 `delete` 외에도 `replace`, `add` 같은 수정 명령어를 쓸 수 있으며, 그 뒤에는 수정하려는 항목의 이름이 정확하게 와야 한다.

수정하려는 항목은 사용자 혹은 그룹을 추가할 때 썼던 ldif 파일을 보거나, `ldapsearch` 명령어로 확인한다.

# 5. Pluggable Authentication Modules(PAM)설정 (Linux7)

Linux환경에 로그인 할 때 Linux 내 로그인 정보가 아닌 LDAP 서버의 내용을 먼저 참조하도록 설정해야 한다.

``` shell
yum -y install nss-pam-ldapd

systemctl start nslcd
```

그 다음 4개의 파일에 내용을 추가해줘야하는데 각각 다음과 같다.

/etc/nslcd.conf
/etc/pam.d/system-auth
/etc/pam.d/password-auth
/etc/nsswitch.conf

## /etc/nslcd.conf 수정
```powershell
...

uri ldap:<IP 주소>    # '/etc/hosts/'에 등록된 host명을 적는 것도 가능하다.

...

# The distinguished name of the search base.
base dc=exampleserver
...
```

## /etc/pam.d/system-auth 수정
Linux에서 해당 파일을 위에서 순서대로 읽기 때문에 줄을 넣는 위치에 주의한다.

보안을 위한 넣는 위치만 파악할 수 있도록 다른 옵션들은 삭제해서 공개한다.

넣어야하는 줄은 세번째 열에 'pam_ldap.so' 내용을 포함하고 있다.

```python
#%PAM-1.0
# This file is auto-generated.
# User changes will be destroyed the next time authconfig is run.
auth        required      pam_env.so
...
auth        sufficient    pam_ldap.so
auth        required      pam_deny.so

account     required      pam_unix.so
...
account     [default=bad success=ok user_unknown=ignore] pam_ldap.so
account     required      pam_permit.so

password    requisite     pam_pwquality.so
...
password    sufficient    pam_ldap.so
password    required      pam_deny.so

session     optional      pam_keyinit.so
...
session     requisite      pam_ldap.so
```

## /etc/pam.d/password-auth 수정
```python
#%PAM-1.0
# This file is auto-generated.
# User changes will be destroyed the next time authconfig is run.
auth        required      pam_env.so
...
auth        sufficient    pam_ldap.so
auth        required      pam_deny.so

account     required      pam_unix.so
...
account     [default=bad success=ok user_unknown=ignore] pam_ldap.so
account     required      pam_permit.so

password    requisite     pam_pwquality.so
...
password    sufficient    pam_ldap.so 
password    required      pam_deny.so

session     optional      pam_keyinit.so 
...
session     optional      pam_ldap.so
```

## /etc/nsswitch.conf 수정
```python
...

passwd:      files ldap
shadow:      files ldap
group:       files ldap
#passwd:     files sss
#shadow:     files sss
#group:      files sss
#initgroups: files sss

hosts:      files dns myhostname

...
```

## 서버 연결 및 권한 부여
```shell
$ authconfig --enableldap --enableldapauth --ldapserver=<서버이름> --ldapbasedn="dc=exampleserver" --enablemkhomedir --update
```

# 6. Pluggable Authentication Modules(PAM)설정 (Rocky Linux8)
Rocky Linux8의 경우 보안정책이 엄격해지면서 Linux7과 같이 직접적으로 텍스트 수정을 막게 되어있다.

1차적으로 authconfig 명령어 자체가 막혀있으며, 만약 임의로 텍스트 수정한 다음 openLDAP를 재시작하면 백업된 보안파일로 롤백되게된다.

당면했던 문제는 Rocky Linux8의 메뉴얼의 경우 Linux7을 쓰는 OS의 client 서버가 된다는 경우를 상정하지 않고 작성되었다는 점이었다.

구형 보안 시스템을 메인으로 하다보니 약간의 충돌이 있었고, 이를 타파하기 위해서 약간의 꼼수를 부려 Rocky Linux8의 보안설정을 텍스트 수정하기로 했다.

## **6-1. RHEL 8 가이드가 제시한 것과 동일하게 sssd에 맞춰서 연결**
[Rocky Linux 8 openLDAP: Configure LDAP client](https://www.server-world.info/en/note?os=Rocky_Linux_8&p=openldap&f=3)

## 6-2. 다음의 사항들을 확인
- 메뉴얼에서 말한 것과 같이 `authselect select sssd` 수행 확인
- Linux7 서버에 설치된 LDAP 아이디로 Rocky Linux8 서버에 접근 불가능함 확인

## 6-3. 파일 3개 수정
### nsswith.conf
```python
# Generated by authselect on Thu Mar 10 16:26:00 2022
# Do not modify this file manually.

# If you want to make changes to nsswitch.conf please modify
# /etc/authselect/user-nsswitch.conf and run 'authselect apply-changes'.
#
# Note that your changes may not be applied as they may be
# overwritten by selected profile. Maps set in the authselect
# profile takes always precedence and overwrites the same maps
# set in the user file. Only maps that are not set by the profile
# are applied from the user file.
#
# For example, if the profile sets:
#     passwd: sss files
# and /etc/authselect/user-nsswitch.conf contains:
#     passwd: files
#     hosts: files dns
# the resulting generated nsswitch.conf will be:
#     passwd: sss files # from profile
#     hosts: files dns  # from user file

passwd:     ldap sss files systemd
group:      ldap sss files systemd
netgroup:   sss files
automount:  sss files
services:   sss files
```
### system-auth
```python
# Generated by authselect on Thu Mar 10 16:26:00 2022
# Do not modify this file manually.

auth        required                                     pam_env.so
...
auth        required                                     pam_deny.so
auth        sufficient                                   pam_ldap.so

account     required                                     pam_unix.so
...
account     [default=bad success=ok user_unknown=ignore] pam_ldap.so
account     required                                     pam_permit.so

password    requisite                                    pam_pwquality.so
...
password    sufficient                                   pam_ldap.so
password    required                                     pam_deny.so

session     optional                                     pam_keyinit.so
...
session     requisite                                    pam_ldap.so
```
### password-auth
```python
# Generated by authselect on Thu Mar 10 16:26:00 2022
# Do not modify this file manually.

auth        required                                     pam_env.so
...
auth        sufficient                                   pam_ldap.so
auth        required                                     pam_deny.so

account     required                                     pam_unix.so
...
account     [default=bad success=ok user_unknown=ignore] pam_ldap.so
account     required                                     pam_permit.so

password    requisite                                    pam_pwquality.so
...
password    sufficient                                   pam_ldap.so
password    required                                     pam_deny.so

session     optional                                     pam_keyinit.so 
...
session     requisite                                    pam_ldap.so
```

## 6-4. 다음의 명령어 실행 후 LDAP 아이디로 로그인 시도
`systemctl restart nslcd`

-----

이외에도 openLDAP 관리자 계정이 비밀번호를 수정해 줄 필요없이, LDAP 유저 스스로 `passwd`명령어를 통해 쉽게 비밀번호를 수정 가능하게 하는 방법도 존재한다.

아래에 LDAP 구성을 위해 참고했던 링크들을 올리니 필요한 경우 참고하기를 바란다.


[LDAP Server 설치 (on CentOS)](https://dejavuqa.tistory.com/264)

[OpenLDAP을 활용한 기반시스템 중앙 인증관리 #1](https://blog.hkwon.me/use-openldap-part1/)

[OpenLDAP Software 2.4 Administrator's Guide: Running slapd](https://www.openldap.org/doc/admin24/runningslapd.html)

[Linux PAM](https://blog.naver.com/leekh8412/220872048171)

[https://blog.naver.com/leekh8412/220872048171](https://blog.naver.com/leekh8412/220872048171)

[LDAP을 이용한 OS(Linux/AIX)인증 - PAM 사례(3) - DSMENTORING](https://ldap.or.kr/ldap%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-oslinuxaix%EC%9D%B8%EC%A6%9D-pam-%EC%82%AC%EB%A1%803/)

[리눅스 환경에서 LDAP을 이용한 PAM 구성 - DSMENTORING](https://ldap.or.kr/pam_ldap/)

[LDAP Client 설치 (on CentOS)](https://dejavuqa.tistory.com/265)

[6.19. pam_mkhomedir - 사용자 홈 디렉터리 만들기](https://wariua.github.io/linux-pam-docs-ko/sag-pam_mkhomedir.html)

[What is Umask and How To Setup Default umask Under Linux?](https://www.cyberciti.biz/tips/understanding-linux-unix-umask-value-usage.html#:~:text=umask%20and%20level%20of%20security)

[Configure OpenLDAP on Rocky Linux 8 | GoLinuxCloud](https://www.golinuxcloud.com/install-configure-openldap-rocky-linux-8/#:~:text=Rocky%20Linux%208%20has%20the%20firewalld%20application%20as%20its%20default%20firewall.%20We%20can%20enable%20the%20ldap%20and%20ldaps%20services%20as%20below)

[8 simple steps to configure ldap client RHEL/CentOS 8](https://www.golinuxcloud.com/ldap-client-rhel-centos-8/)

[Let openldap users change password with passwd in centos, i broke it](https://serverfault.com/questions/1066458/let-openldap-users-change-password-with-passwd-in-centos-i-broke-it)

[OpenLDAP Software 2.4 Administrator's Guide: Access Control](https://www.openldap.org/doc/admin24/access-control.html)

[OpenLDAP: Allow users to change their password with the unix passwd command.](https://www.unixguide.net/content/openldap-allow-users-change-their-password-unix-passwd-command)

[Service - LDAP Access Control | Ubuntu](https://ubuntu.com/server/docs/service-ldap-access-control)

[[SOLVED] LDAP user's password change issue](https://forums.centos.org/viewtopic.php?t=66493)

[Linux-PAM 시스템 관리자 안내서](https://wariua.github.io/linux-pam-docs-ko/Linux-PAM_SAG.html)

[4.1. 설정 파일 문법](https://wariua.github.io/linux-pam-docs-ko/sag-configuration-file.html)

