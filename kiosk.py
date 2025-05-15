drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스", "딸기 주스"]
prices = [1500, 2500, 4000, 4200]

# drinks = ["아이스 아메리카노"]
# prices = [1500]
total_price = 0
amounts = [0] * len(drinks)

#할인 적용 정책
DISCOUNT_THRESHOLD = 10000 # 할인이 적용되는 임계값(임계값=threshold)
DISCOUNT_RATE= 0.1 # 할인율


def run() ->None:
    """
    키오스크 실행(구동) 함수
    :return: None
    """
    while True:
        try:
            menu = int(input(display_menu()))
            if len(drinks) >= menu >= 1:
                order_process(menu - 1)
            elif menu == len(drinks)+1:
                print("주문을 종료합니다")
                break
            else:
                print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")
        except ValueError:
            print(f"문자를 입력할 수 없습니다. 숫자를 입력해주세요")




def apply_discount(price: int) -> float:
    """
    총 금액이 특정 금액(임계값)을 넘어서면 할인율을 적용하는 함수
    :param price: 할인 전 총 금액
    :return: 할인이 적용된 금액 또는 할인이 적용되지 않은 금액
    """
    if price >= DISCOUNT_THRESHOLD:
        return price*(1-DISCOUNT_RATE)
    return price


def get_ticket_number()->int:
    """
    주문 번호표 처리 기능 함수
    :return: 번호
    """
    number = 0
    try:
        with open("ticket.txt","r") as fp:
            number = int(fp.read())
    except FileNotFoundError:
        number = 0

    number= number +1

    with open("ticket.txt", "w") as fp:
        fp.write(str(number))

    return number


def order_process(idx: int) -> None:
    """
    주문 처리 함수 1) 주문 디스플레이  2) 총 주문 금액 누산  3) 주문 품목 수량 업데이트
    :param idx: 고객이 선택한 메뉴 - 1 (인덱스, 정수)
    :return: 없음
    """
    global total_price
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {prices[idx]}원 입니다")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1


def display_menu() -> str:
    """
    음료 선택 메뉴 디스플레이 함수
    :return: 음료 메뉴 및 주문 종료 문자열
    """
    print("="*30)
    menu_texts = "".join([f"{j+1}) {drinks[j]} {prices[j]}원\n" for j in range(len(drinks))])
    menu_texts = menu_texts + f"{len(drinks)+1}) 주문종료 : "
    return menu_texts


def print_receipt() -> None:
    """
    영수증 출력 기능
    :return: 없음
    """
    print(f"{'상품명':^20}{'단가':^6}{'수량':^6}{'금액':^6}")
    for i in range(len(drinks)):
        if amounts[i] > 0:
            print(f"{drinks[i]:^20}{prices[i]:^6}{amounts[i]:^6}{prices[i] * amounts[i]:^6}")

    discounted_price= apply_discount(total_price)
    discount=total_price-discounted_price


    print(f"할인 전 총 주문 금액 : {total_price}원")
    if discount > 0:
        print(f"할인 금액:{discount}원 ({DISCOUNT_RATE*100}%)")
        print(f"할인 금액: {discount}원")
        print(f"할인 적용 후 지불하실 총 금액은{discounted_price}원 입니다.")
    else:
        print(f"할인이 적용되지 않았습니다.\n 지불하실 총 금액은 {total_price}원 입니다.")



def test() -> None:
    """
    앞으로 추가될 키오스크 기능
    :return:
    """
    pass