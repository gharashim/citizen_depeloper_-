class Node:
    def __init__(
            self,
            name = None,
            tel = None,
            phone = None,
            next = None
    ) -> None:
        self.name = name
        self.tel = tel
        self.phone = phone
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.root = None


    def add_data_rear(self, n) -> None:
        if self.root is None:
            self.root = n
        else:
            curr = self.root
            while curr.next:
                curr = curr.next
            curr.next = n


    def show(self) -> None: # 연결된 node의 data를 순서대로 보여주는 메서드 구현
        curr= self.root
        while curr: # 연결 리스트가 끝인지 확인
            print(curr.name, curr.tel, curr.phone) # 값 출력
            curr = curr.next # 이동


    def pop_first(self) -> None:
        curr = self.root
        if curr:
            self.root = curr.next
            print('{} 고객님의 {}가 발송됐습니다.'.format(curr.name, curr.phone))
        else:
            print('현재 예약 고객은 0명 입니다.')


    def search_data(self, val) -> None:
        curr = self.root
        cnt = 0
        if self.root is None:
            print('현재 예약 고객은 0명 입니다.')
            cnt = 1
        else:
            while curr:
                if curr.name == val:
                    print('{} 님의 예약 정보 입니다.'.format(curr.name))
                    print('전화 : {}'.format(curr.tel))
                    print('모델 : {}'.format(curr.phone))
                    cnt = 1
                curr = curr.next
        if cnt == 0:
            print('{}님은 현재 예약 명단에 없습니다.'.format(val))


    def del_data(self, val) -> None:
        curr = self.root
        cnt = 0
        if curr is None:
            print('현재 예약 고객은 0명 입니다.')
            cnt = 2
        else:
            while curr.next.next:
                if curr.next.name == val:
                    curr.next = curr.next.next
                    cnt = 1
                else:
                    curr = curr.next
            if curr.next:
                if curr.next.name == val:
                    curr.next = None
                    cnt = 1

        if cnt == 0:
            print('{}님은 현재 예약 명단에 없습니다.'.format(val))
        elif cnt == 1:
            print('{}님의 예약을 취소 합니다.'.format(val))
        # pass


    def write_data(self) -> list:
        curr = self.root
        result = []
        while curr:
            result.append([curr.name, curr.tel, curr.phone])
            curr = curr.next
        return result


def load_database(ds: LinkedList):
    # 파일의 데이터를 읽어 Node 객체에 저장하고
    # Node를 LinkedList에 추가
    with open('result.txt', mode = 'r', encoding = 'utf-8') as f:
        while True:
            line = f.readline()
            if line == '': break
            ds.add_data_rear(Node(*line.split()))


def reserve_product(ds: LinkedList):
    # 사용자로부터 정보를 입력 받아 Node를 구성
    # Node를 LinkedList의 끝(root에서 가장 먼 곳)에 추가
    import re
    p = re.compile(r'^[0-9]{3}-[0-9]{4}-[0-9]{4}$')

    print('[고객 정보]')
    name = input('이름 : ')

    tel = input('번호 : ')
    while len(re.findall(p, tel)) < 1:
        print('잘못된 전화번호 양식 입니다.')
        tel = input('번호 : ')

    phone = input('기종 : ')

    ds.add_data_rear(Node(name, tel, phone))


def ship_product(ds: LinkedList):
    # LinkedList의 가장 앞단의 Node를 제거
    ds.pop_first()


def search_customer(ds: LinkedList):
    # 사용자로부터 정보를 입력 받아 LinkedList에 탐색 후 결과 출력
    print('[예약 검색]')
    name = input('이름 : ')
    ds.search_data(name)


def remove_customer(ds: LinkedList):
    # 입력된 고객 정보를 포함하는 Node를 LinkedList에서 제거
    print('[예약 취소]')
    name = input('이름 : ')
    ds.del_data(name)


def write_database(ds: LinkedList):
    # ds에 저장된 데이터를 파일로 저장
    result = ds.write_data()
    result_file = 'result.txt'
    with open(result_file, mode = 'w', encoding = 'utf-8') as f:
        for i in range(len(result) - 1):
            line = result[i]
            f.write(str(line[0]) + ' ' + str(line[1]) + ' ' + str(line[2]) + '\n')
        if len(result) > 0:
            line = result[-1]
            f.write(str(line[0]) + ' ' + str(line[1]) + ' ' + str(line[2]))


# -----------------------------------------------------------------------------
# 프로그램의 시작

ds = LinkedList()

load_database(ds)

while True:
    print("\n-------------------------------------------")
    print("   대  기  인  원  관  리  프  로  그  램   ")
    print("-------------------------------------------\n")
    print("1) 구매 예약")
    print("2) 제품 출고")
    print("3) 예약 삭제")
    print("4) 예약 검색")
    print("5) 종료")

    select = input("> ")

    if select == "1":
        reserve_product(ds)
    elif select == "2":
        ship_product(ds)
    elif select == "3":
        remove_customer(ds)
    elif select == "4":
        search_customer(ds)
    else:
        break

write_database(ds)