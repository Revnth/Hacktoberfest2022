ABOUT AVL TREE
AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes.

                20
             /      \
           12        25
         /   \      /
        8     15   17
      /
     4

The above tree is AVL because the differences between heights of left and right subtrees for every node are less than or equal to 1.

now, Example of a Tree that is NOT an AVL Tree:

                20
             /      \
           12        25
         /   \      /
        8     15   17
      /   \
     4     7
    /

1

The above tree is not AVL because the differences between the heights of the left and right subtrees for 8 and 12 are greater than 1.

Why AVL Trees?
The majority of BST operations, including search, max, min, insert, delete, and others, take O(h) time, where h is the BST's height. For a skewed Binary tree, the cost of these operations can increase to O(n). We can provide an upper bound of O(log(n)) for all of these operations if we make sure that the height of the tree stays O(log(n)) after each insertion and deletion. An AVL tree's height is always O(log(n)), where n is the tree's node count.
