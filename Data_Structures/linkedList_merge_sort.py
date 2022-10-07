from linked_lists import LinkedList


def merge_sort(linked_list):
    '''
    This function sorts a list in ascending order 
        - Recursively divides the linked list  into sub lists containing a single node 
        - Repeatedly merge the sublists to produce a sorted sublist until one remains

    Returns a sorted linked list
    '''
    if linked_list.size() == 1:
        return linked_list

    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    '''
    divide the unsorted list at midpoint into sublists 
    '''
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None
        return left_half, right_half

    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    '''
    This function merges two linked lists, sorting by data in nodes 
    Returns a new Mmerge list 
    '''
    # create a new linked list that contains nodes from
    # merging left and right
    merged = LinkedList()

    # add a fake head that is discarded later
    merged.add(0)

    # set current to the head of the linked list
    current = merged.head

    # obtain head nodes for the left and linked lists
    left_head = left.head
    right_head = right.head

    # go throught he list until you reacht the tail node
    while left_head or right_head:
        # if the head node of the left is None: we're past the tail
        # add the node from the right to merged ist
        if left_head is None:
            current.next_node = right_head
            # call next on right to set loop condition to false
            right_head = right_head.next_node
            # if the head node of right is none, the we past the tail
            # add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # call next on ledt to set loop condition to False
            left_head = left_head.next_node
        else:
            # not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data

            # if data on left is less than right data, set current to left ode
            if left_data < right_data:
                current.next_node = left_data

                # move left head to next node
                left_head = left_head.next_node
            # if data on left is greater than right, set current to right node
            else:
                current.next_node = right_head
                # move right head to next node
                right_head = right_head.next_node

        # move current to next scope
        current = current.next_node

    # discard fake node and set first merged node as node
    head = merged.head.next_node
    merged.head = head

    return merged


l = LinkedList()
l.add(1)
l.add(35)
l.add(22)
l.add(32)
l.add(2)
l.add(34)
l.add(21)

print(l)
