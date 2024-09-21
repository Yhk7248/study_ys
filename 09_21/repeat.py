"""
연수님 오늘은 복습입니다!!

1. python 개발 환경 설치
    1) python.org 에서 python 다운로드
    2) Pycharm 다운로드
    3) Git bash
    4) 파이참 열어서 테스트 용 프로젝트 생성해보고 가상환경 폴더 만들기
    5) 테스트 완료되면 git bash 로 PacharmProjects 폴더 열어서 git bash 로 clone
    6) 이후의 수업에서는 git pull 만 반복하면 됨.

2. function 예제
    ********************************** 주의사항 ******************************************

        1) 함수의 구성.
            1. def 키워드
            2. 함수명
            3. 매개 변수 (필수 아님)
            4. return (필수 아님)
        2) 함수 내부의 변수 이름과 함수 외부의 변수 이름은 다른 메모리 주소에 할당 되기 때문에 이름이 같다고 해서 영향을 주지 않음.
        3) 함수에 전달되는 변수의 이름과 함수 내부에서 사용될 변수 이름은 달라도 됨.

    ************************************************************************************
    1) 2x + 3 의 해를 return 하는 함수를 만들어라
        def func_linear(x):
            return 2*x +3

    2) add 함수, multiply 함술를 이용해서 2x + 3 의 해를 구하는 코드를 작성하라.
        def add(a, b):
            return a+b

        def multiply(a, b):
            return a*b

        if __name__ == "__main__":
            x = int(input)) # 5 입력
            x = multiply(x, 2) # 2x 를 먼저 계산
            y = add(x, 3) # 2x 의 결과에 3을 더한 결과 계산
            print(y)
"""