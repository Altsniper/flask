from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# db에 대한 실제 내용이 작성되어 있습니다.
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
# Flask 우리가 지정하지 않으면 기본적으로 app.py를 시작점으로 인식
# Flask 어플리케이션을 생성하는 코드, 어플리케이션의 입구를 만들어줌
# 이 파일에 다른 파일 경유 없이 test.py를 통해 실행된다면 __name__ 변수에는 'test'라는 문자열이 담김
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM과 관련된 코드를 작성해줍니다.
    db.init_app(app)
    migrate.init_app(app, db)
    # main_views 내부에 있는 bp를 통한 라우팅 함수들을 등록
    from views import main_views

    app.register_blueprint(main_views.bp)

    return app