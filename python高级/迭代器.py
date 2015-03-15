def iter_(obj):
    it = iter(obj)
    try:
        while True:
            val = it.next()
            print val
    except StopIteration:
        pass

iter_(range(5))
iter_("hello")
