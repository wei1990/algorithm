# encoding:utf-8
from listnode_handle import ListNodeHandle
from solution import Solution
#from solution import ListNode
#
#l1_1 = ListNode(1)
#l1_2 = ListNode(2)
#l1_3 = ListNode(4)
#l1_1.next = l1_2
#l1_2.next = l1_3
#
#2_1 = ListNode(1)
#l2_2 = ListNode(3)
#l2_3 = ListNode(4)
#l2_1.next = l2_2
#l2_2.next = l2_3
#
#s = Solution()
#l3 = s.mergeTwoLists(l1_1, l2_1)
#list3 = []
#while l3:
#    list3.append(l3.val)
#    l3 = l3.next
#print(list3)


listnode1 = ListNodeHandle(None)
l1 = [1,2,4]
for i in l1:
    listnode1.add_node(i)
listnode1.print_node(listnode1.head)

listnode2 = ListNodeHandle(None)
l2 = [1,3,4]
for i in l2:
    listnode2.add_node(i)
listnode2.print_node(listnode2.head)

# 合并两个有序链表
s = Solution()
newlist_head = s.mergeTwoLists(listnode1.head, listnode2.head)
# 递归或者非递归返回的都是表头，所以可以直接用第一个结点来实例化类 ListNode_handle
newlist = ListNodeHandle(newlist_head)         
newlist.print_node(newlist.head)
