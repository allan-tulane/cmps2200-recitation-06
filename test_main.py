from main import *

def test_left_and_right_child():
    heap = BinaryHeap()
    heap.H = [10, 12, 15, 25, 30, 36]
    assert heap.lchild(1) == 3
    assert heap.lchild(2) == 5
    assert heap.lchild(3) == -1
    
    assert heap.rchild(1) == 4
    assert heap.rchild(2) == -1

def test_parent():
    heap = BinaryHeap()
    heap.H = [10, 12, 15, 25, 30, 36]
    assert heap.parent(1) == 0
    assert heap.parent(2) == 0
    assert heap.parent(4) == 1
    assert heap.parent(0) == -1

def test_reheapUp():
    heap = BinaryHeap()
    # we added the 7 at the end of the list, but it is
    # out of place. We must promote it to the root.
    heap.H = [10, 12, 15, 25, 30, 36, 7]
    heap.reheapUp(6)  
    assert heap.H == [7, 12, 10, 25, 30, 36, 15]

def test_reheapDown():
    heap = BinaryHeap()
    heap.H = [13, 10, 12, 15, 25, 30, 36]
    # the 13 is out of place. We must demote it one level to the left.
    heap.reheapDown(0)  
    assert heap.H == [10, 13, 12, 15, 25, 30, 36]

def test_deleteMin():
    heap = BinaryHeap()
    heap.H = [10, 12, 15, 25, 30, 36]
    heap.deleteMin()
    assert heap.H == [12, 25, 15, 30, 36]

def test_insert():
    heap = BinaryHeap()
    heap.H = [10, 12, 15, 25, 30, 36]
    heap.insert(11)
    assert heap.H == [10, 12, 11, 25, 30, 36, 15]

def test_heapsort():
    L = [12,5,1,6,9,10,8,2]
    assert heapsort(L) == sorted(L)    

