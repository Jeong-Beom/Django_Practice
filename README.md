# Django_Practice
### 시작 가이드(공통)
#### Installation
1. Install git
```bash
sudo apt-get install git
```
2. Install curl
```bash
sudo apt-get install curl
```
3. Install pyenv
```bash
curl https://pyenv.run | bash
```
4. PATH 등록(~/.bashrc 또는 ~/.bash_profile에 등록)
```
# pyenv path add
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# pyenv-virtualenv add
eval "$(pyenv virtualenv-init -)"
```
5. Install packages
```bash
sudo apt-get update;
sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget llvm liblzma-dev \
libncurses-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev \
libffi-dev python3-tk
``` 

----------------------
### mysite01
> - 프로젝트 소개: Django로 게시판 서비스 만들기
> - 개발기간: 2024.06.17~2024.06.30
> - 시작 가이드는 mysite01 폴더 참고
> - 기술스택
>> Environment
>>> <img src ="https://img.shields.io/badge/Ubuntu-E95420.svg?&style=for-the-badge&logo=Ubuntu&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/visualstudiocode-007ACC.svg?&style=for-the-badge&logo=visualstudiocode&logoColor=white"/>
>>><img src ="https://img.shields.io/badge/git-F05032.svg?&style=for-the-badge&logo=git&logoColor=white"/>
>>><img src ="https://img.shields.io/badge/github-181717.svg?&style=for-the-badge&logo=github&logoColor=white"/>
>> Development
>>> <img src ="https://img.shields.io/badge/python-3776AB.svg?&style=for-the-badge&logo=python&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/django-092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/html5-E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/css3-1572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/bootstrap-7952B3.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/>
>> Deployment
>>> <img src ="https://img.shields.io/badge/microsoftazure-0078D4.svg?&style=for-the-badge&logo=microsoftazure&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/amazonwebservices-232F3E.svg?&style=for-the-badge&logo=amazonwebservices&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/postgresql-4169E1.svg?&style=for-the-badge&logo=postgresql&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/nginx-009639.svg?&style=for-the-badge&logo=nginx&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/gunicorn-499848.svg?&style=for-the-badge&logo=gunicorn&logoColor=white"/>
----------------------
