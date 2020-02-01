# 제일먼저 실행하라는 명령어

from contacts.ctrl import Ctrl

if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 연락처 추가')
        print('2. 연락처 목록 보기')
        print('3. 연락처 삭제')
        return input('메뉴 선택 \n')

    app = Ctrl()

    while 1:
        menu = print_menu()
        if menu == '0':
            break
        if menu == '1':
            app.register(input('name\n'),
                         input('phone\n'),
                         input('email\n'),
                         input('addr\n'))
            print('등록 되었습니다')
            break
        if menu == '2':
            print(app.list())
            break
        elif menu == '3':
            app.remove(input('삭제할 이름'))
            break
