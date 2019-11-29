# encoding:utf-8

from listnode import ListNode

class ListNodeHandle:              # 链表操作类型
    def __init__(self, node):
         self.head = node           #该类需要初始化头节点和当前节点。即用一个链表的头结点来实例化，可以用listnode_handle()来实例化一个空链表
         self.cur_node = node 
        
        
    def add_node(self, data):       # 添加结点操作，该结点的数值为data
        node = ListNode(None)       # 新建ListNode类型
        node.val = data
        node.next = None
        if self.head == None:       # 若当前链表为空，则直接将其作为头结点
            self.head = node
            self.cur_node = node
        else:                       # 否则将该结点连到后面，将当前结点更新 
            self.cur_node.next = node
            self.cur_node = self.cur_node.next
        return self.head

    def insert_node(self, i, data):    # 在第i个位置插入一个数值为data的结点  
        node = ListNode(None)
        node.val = data
        node.next = None

        cur_node = self.head
        for j in range(i-1):        # 索引到位置i 
            cur_node = cur_node.next
        node.next = cur_node.next
        cur_node.next = node

    def delete_node(self,i):           # 删除位置为i的结点
        cur_node = self.head
        for j in range(i-1):        # 索引到位置为i的结点
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next

    def print_node(self,node):      # 从头开始打印所有结点的数值
        while node:
            print(node.val, end=' ')
            node = node.next
        print(end='\n')

    def find_node(self, value):     # 寻找链表中是否存在数值value  
        if self.head == None:
            return False
        else:
            node = self.head
            while(node):
                if node.val == value:
                    return True
                else:
                    node = node.next
            return False
