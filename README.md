# python
  - 2022/02/03 공부용이에용
  - VS Code Github 연결해볼거에요

# python Function
  - def 함수명(매개변수): 형식의 구조를 갖는다

# Python Class 
  - Python의 Method의 첫번째 parameter는 관례적으로 self를 사용한다. 객체를 호출할때 호출한 객체 자신이 전달되기 때문이다. 
  - 생성자 Constructor "__init__"
  - java 처럼 Overloading 존재 하지 않음. 

# Python Module
  - Module로 import 설정시에는 하위 구문은 해석하지 않음 if __name_ =="__main__"
  - Module의 일부분만 사용시에는 from [Module이름] import [Method이름]
  - 특정 모듈 Folder설정. 
    - import sys
      sys.path [확인]
      sys.path.append([특정 모듈 Folder 경로설정])
    - PYTHONPATH 환경변수 사용
      set PYTHONPATH = [특정 모듈 Folder 경로설정]

# Python Package 
  - __init__.py