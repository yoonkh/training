#1번을 눌리면 주문하기  2번 잔액보기 5번을 눌리면 나가기
#1번을 누르면 메뉴가 나오고 1.빅맥 2.상하이 3.1955
#2번 누르면 상하이버거사고 잔액,메뉴 보여줍니다
#계속해서 루프를 돌다가 5번을 누르면 끝


from order2 import Burger

big = Burger('빅맥', 4000)
shang = Burger('상하이버거', 5500)
old = Burger('1955', 6500)

def turn_off():
    print('=============== 햄버거 세트 ===============')
    while True:
        choice = input('뭐 먹을래?\n  1: 빅맥  2: 상하이버거  3: 1955버거  5: 간다\n   Input : ')
        if choice == '5':
            print('=========== 잘가 ============')
            break
        elif choice == '1':
            big.info()

        elif choice == '2':
            shang.info()

        elif choice == '3':
            old.info()

        else:
            print('안먹어??')
        print('==============================')


if __name__ == '__main__':
    turn_off()




