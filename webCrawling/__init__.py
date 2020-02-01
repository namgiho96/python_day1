from webCrawling.ctrl import Ctrl
if __name__ == '__main__':
    def print_menu():

        print('0. Exit')
        print('1. Bugs Music')
        print('2. Naver Movie')
        print('3. WiKi pid')
        print('4. hanbit Auto Login')
        print('5. winter')

        return input('메뉴 선택 \n')

    app = Ctrl()
    while 1:
        menu = print_menu()
        if menu == '1':
            app.bugs_music('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20200201&charthour=16')
            break
        if menu == '2':
            app.naver_movie('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
            break
        if menu == '3':
            app.wiki('http://dh.aks.ac.kr/Encyves/wiki/index.php/%EC%A1%B0%EC%84%A0_%EC%84%B8%EC%A2%85')
            break
        if menu == '4':
            app.hanbit_login('http://www.hanbit.co.kr/')
            break
        if menu == '5':
            app.weather('')  #TODO : 날씨 크롤링
            break
        elif menu == '0':

            break