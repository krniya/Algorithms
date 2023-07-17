class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
        listOneStack, listTwoStack = [], []
        while l1:
            listOneStack.append(l1.val)
            l1 = l1.next
        while l2:
            listOneStack.append(l2.val)
            l2 = l2.next
        carry, prevLinkedList = 0, None
        while listOneStack or listTwoStack:
            firstNumber = listOneStack.pop() if listOneStack else 0
            secondNumber = listTwoStack.pop() if listTwoStack else 0
            currentSum = firstNumber + secondNumber
            currentSum += carry
            carry = 0
            if currentSum > 9:
                carry = 1
                currentSum %= 10
            currentLinkedList = ListNode(currentSum)
            currentLinkedList.next = prevLinkedList
            prevLinkedList = currentLinkedList
        return prevLinkedList
    
    
listOne = ListNode(7)
listOne.next = ListNode(2)
listOne.next.next = ListNode(4)
listOne.next.next.next = ListNode(3)

listTwo = ListNode(5)
listTwo.next = ListNode(6)
listTwo.next.next = ListNode(4)

current = addTwoNumbers(listOne, listTwo)
while current:
    print(current.val)
    current = current.next


