class Node:
    def __init__(self, val, next = None) -> None:
        self.data = val
        self.next = next # 연결(Linked) 될 node를 클래스 속성으로 부여
        
# root = Node('root')
a1 = Node(0)
a2 = Node(1)
a3 = Node(2)

root = a1 # next property를 a1에 할당 / a1 인스턴스를 root의 next property에 바인딩
a1.next = a2
a2.next = a3