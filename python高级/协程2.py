#引用 https://blog.tonyseek.com/post/event-manage-with-greenlet/

from time import sleep

event_listeners = {}

def fire_event(name):
    event_listeners[name]()

def use_event(func):
    def call(*args, **kwargs):
        generator = func(*args, **kwargs)
        # 执行到挂起
        event_name = next(generator)
        # 将“唤醒挂起的协程”注册到事件管理器中
        def resume():
            try:
                next(generator)
            except StopIteration:
                pass
        event_listeners[event_name] = resume
    return call

@use_event
def test_work():
    print("=" * 50)
    print("waiting click")
    yield "click" #在main方法执行test_work()的时候它挂起当前协程
    print("clicked!!") #它是下一次调用next或者send方法的时候才会执行

if __name__ == "__main__":
    test_work()
    sleep(3) # 做了很多其他事情
    fire_event("click") #协程就是自己调度。所以这里自己触发click 事件
