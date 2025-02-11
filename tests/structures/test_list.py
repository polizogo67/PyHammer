from hammer.datastructures import LinkedList

def test_sample():

    ll = LinkedList()
    N = 20
    M = 10

    assert ll.pop() is None

    for i in range(N):
        ll.push(i)
        assert ll.size == i + 1

    for i in range(M):
        assert ll.pop() == N - 1 - i
        assert ll.size == N - 1 - i

    ll.insert(5, 100)
    assert ll.size == ll.count()

    # print( ll.size, ll.get(6) ) # 0 None
