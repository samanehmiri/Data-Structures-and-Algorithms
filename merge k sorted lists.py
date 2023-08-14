'''
Merge k Sorted Lists

Q: You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.

Merge all them into one sorted linked-list and return it.

Solution: 

Let's say we have k = 4 items each (linked-list) in our lists initially.
lists: [[ List 1 ], [ List 2 ], [ List 3 ], [ List 4 ]]

Step 1: Pairing and Merging:
Pair up the items and merge them:

Pair 1: Merge List 1 with List 2 -> [Merged list 1]
Pair 2: Merge List 3 with List 4 -> [Merged list 2]
Now we have k/2 merged lists: 2 merged lists.

Step 2: Repeat Merging until you have a single 
sorted linked list, which is the final result of 
merging the initial k sorted linked lists

Pair up the merged lists and merge them: [Merged list A]
Now we have k/4 merged lists: 1 merged lists.


Each step reduces the number of lists by half, and the merging process 
ensures that the merged lists are sorted. 
This approach is more efficient than merging one list 
at a time and leverages the divide and conquer strategy 
to achieve faster merging of multiple sorted linked lists.

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SortedList:
    def mergeKList(self, lists):
        k = len(lists)
        i = 1
        while i < k:
            for i in range(0, k - i, i * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + i])
            i *= 2
        return lists[0] if k > 0 else None
    
    def merge2Lists(self, l1, l2):
        head = curr = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l1
                l1 = curr.next.next
            curr = curr.next
        
        if not l1:
            curr.next = l2
        else:
            curr.next = l1
        
        return head.next




'''
Time complexity: O(Nlogk) where k is the number of linked lists.
    - merge two linked list is O(N) N in total number of nodes in two list, 
        sum up the merge process is O(logk).
Space complexity: O(1)
'''