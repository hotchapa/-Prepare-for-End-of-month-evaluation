class Node:
    def __init__(self,data) :
        # 데이터를 저장할 변수
        # 다음 요소를 가리키는 변수
        self.value = data
        self.next = None
        # 리스트는 가장 앞 요소만 참조하면 모든 요소를 참조할 수 있음 (재귀니까?)

class MyLinkedList:
    def __init__(self):
        # 첫 번째 요소(노드)의 주소
        self.head = None
        self.size = 0
    def append(self,data):
        # 리스트에 데이터 추가
        # 노드 만들어서 마짐가에 추가, 첫요소라면 head에 참조 시키기
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node

        else:
            # 마지막 요소 찾아서 걔한테 달아주기
            # node의 next가 None인 요소가 마지막 요소
            current = self.head
            while current.next:
                current = current.next

        self.size += 1 # 노드를 새로 붙였으니, 길이가 증가해야됨

            # current의 next는 None
    def __str__(self):
        # 현재 리스트가 어떻게 구성되어있는지 출력하기 위해서 작성
        result = '['
        current = self.head
        while current : # current가 value를 가지고 있으면 계속 수행
                result += str(current.value+', ')
                current = current.next
        result += ']'
        return result

    def pop(self,idx=-1):
        if idx == 0:
            # head를 현재 head의 next로 바꿔주기
            self.head = self.head.next

        
        elif idx == -1: #마지막 요소라면
            # 마지막 요소의 이전 요소의 next를 None으로 바꿔주기
            d








lst = MyLinkedList() # 처음에 만들때 비어있는 리스트를 만든다고 가정
lst.append('A')
lst.append('B')
lst.append('C')
lst.append('D')
lst.append('E')
print(lst)