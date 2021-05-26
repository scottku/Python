from .database import *
# __init__.py
# 패키지 import할 때 초기화 작업을 수행하는 파일
#   없어도 패키지로 인식

# from 패키지 import * : 내부의 모든 객체를 import
__all__ = ["Database"] # 명시된 심볼만 export
# __all__ = []    # *로 import 시 아무 것도 export 하지 않음
