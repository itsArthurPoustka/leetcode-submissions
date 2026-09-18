class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_sorted_lists(list1, list2):
    sorted_list = []

    while list1.next != None and list2.next != None:
        if list1.val < list2.val:
            sorted_list.append(list1.val)
            list1 = list1.next
        else:
            sorted_list.append(list2.val)
            list2 = list2.next


    return sorted_list

# lista = ListNode(1, next=ListNode(2, ListNode(3)))
# # print(lista.next)
# d_l = lista.next
# d=d_l.next
# print(d.next.val)

lista = ListNode()
lista.val = 1
lista.next = ListNode(2)
print(lista.val)
print(lista.next.val)