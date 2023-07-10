from flask import Blueprint


# Blueprint 클래스를 통해 임의의 객체를 만듭니다
bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/')
def hello():
     return f'Hello, {__name__}'

# /blog/post/1
# 라우팅 주소를 만들때는 /경로명 까지만 적어줌
# 그 다음에 만들어질 하위 경로도 /경로명
@bp.route('/james')
def hello_james():
     return f'Hello, james'

@bp.route('/jjangu')
def hello_jjangu():
     return f'<b>Hello, jjangu</b>'