#���� https://blog.tonyseek.com/post/event-manage-with-greenlet/

from time import sleep

event_listeners = {}

def fire_event(name):
    event_listeners[name]()

def use_event(func):
    def call(*args, **kwargs):
        generator = func(*args, **kwargs)
        # ִ�е�����
        event_name = next(generator)
        # �������ѹ����Э�̡�ע�ᵽ�¼���������
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
    yield "click" #��main����ִ��test_work()��ʱ��������ǰЭ��
    print("clicked!!") #������һ�ε���next����send������ʱ��Ż�ִ��

if __name__ == "__main__":
    test_work()
    sleep(3) # ���˺ܶ���������
    fire_event("click") #Э�̾����Լ����ȡ����������Լ�����click �¼�
