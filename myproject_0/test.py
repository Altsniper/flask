from flask import Flask

# Flask 우리가 지정하지 않으면 기본적으로 app.py를 시작점으로 인식
# Flask 어플리케이션을 생성하는 코드, 어플리케이션의 입구를 만들어줌
# 이 파일에 다른 파일 경유 없이 test.py를 통해 실행된다면 __name__ 변수에는 'test'라는 문자열이 담김
app = Flask(__name__)

# URL과 FLASK코드를 매핑하는 Flask 데코레이터
@app.route('/')
def hello():
     return f'Hello, {__name__}'

# /blog/post/1
# 라우팅 주소를 만들때는 /경로명 까지만 적어줌
# 그 다음에 만들어질 하위 경로도 /경로명
@app.route('/james')
def hello_james():
     return f'Hello, james'

@app.route('/jjangu')
def hello_jjangu():
     return f'<b>Hello, jjangu</b>'