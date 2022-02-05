def mergeKLists(lists):
    if not lists or len(lists) == 0:
        return None
    while len(lists) > 1:
        mergeList = []
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i+1] if (i+1) < len(lists) else None
            mergeList.append(mergeLists(list1, list2))
        lists = mergeList
    return lists[0]

def mergeLists(list1, list2):
    dummy = current = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 or list2
    return dummy.next