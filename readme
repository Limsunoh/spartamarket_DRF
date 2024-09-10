<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=spartamarket_DRF&fontSize=90" />


## App
### products

- **상품 등록**
    - **조건**: 로그인 상태, 제목과 내용, 상품 이미지 입력 필요.
    - **구현**: 새 게시글 생성 및 데이터베이스 저장.

- ** 상품 댓글**
    - **조건**: 댓글 달기 가능

- **상품 목록 조회**
    - **조건**: 로그인 상태 불필요.

- **상품 수정**
    - **조건**: 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능.

- **상품 삭제**
    - **조건**: 로그인 상태, 삭제 권한 있는 사용자(게시글 작성자)만 가능.

### accounts
- **회원가입**
    - **조건**: username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력하며 성별, 자기소개 생략 가능

- **로그인**
    - **조건**: 사용자명과 비밀번호 입력 필요.

- **프로필 조회**
    - **조건**: 로그인 상태 필요.

- **로그아웃**
    - **조건**: 로그인 상태 필요.

- **본인 정보 수정**
    - **조건**: 이메일, 이름, 닉네임, 생일 입력 필요하며, 성별, 자기소개 생략 가능

## ERD
c:\Users\BIOSTAR\Desktop\사진\ERD.png

## Troubling/Troubleshooting
** 회원상세 보기 검사할때 남의 로그인 정보까지 모두 보이는 참사 발생
    - view에서 ListAPIView 때문이라는걸 검색을 통해 알아낸뒤 ListAPIView대신 RetrieveAPiView를 사용 

** 회원 프로필 수정 시 로그인된 사용자라면 다른 사용자의 프로필까지 수정가능함
    - serializer에 권한 확인하는 로직 작성 및 부분 업데이트 가능하게끔 작성


## Version
'''
asgiref==3.8.1
asttokens==2.4.1
black==24.8.0
blinker==1.8.2
certifi==2024.7.4
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
decorator==5.1.1
Django==4.2
django-extensions==3.2.3
django-seed==0.3.1
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
exceptiongroup==1.2.2
executing==2.0.1
Faker==28.4.1
Flask==3.0.3
Flask-SQLAlchemy==3.1.1
greenlet==3.0.3
idna==3.7
ipython==8.26.0
itsdangerous==2.2.0
jedi==0.19.1
Jinja2==3.1.4
MarkupSafe==2.1.5
matplotlib-inline==0.1.7
mypy-extensions==1.0.0
packaging==24.1
parso==0.8.4
pathspec==0.12.1
pillow==10.4.0
platformdirs==4.2.2
prompt_toolkit==3.0.47
psycopg2==2.9.9
pure_eval==0.2.3
Pygments==2.18.0
PyJWT==2.9.0
python-dateutil==2.9.0.post0
requests==2.32.3
six==1.16.0
SQLAlchemy==2.0.31
sqlparse==0.5.1
stack-data==0.6.3
tomli==2.0.1
toposort==1.10
traitlets==5.14.3
typing_extensions==4.12.2
tzdata==2024.1
urllib3==2.2.2
wcwidth==0.2.13
Werkzeug==3.0.3
'''
