# 실행하는 파일
from calcaulator.controller import Controller
if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. Calculator')
        return input('메뉴 선택 \n')

    while 1:
        menu = print_menu()
        if menu == '0':
            break
        if menu == '1':
            app = Controller()
            print('계산기 작동')
            num1 = int(input('첫번째 숫자'))
            operator = input('연산자')
            num2 = int(input('두번째 숫자'))
            result = app.exec(num1, num2, operator)
            print('결과 : %d' % result)
