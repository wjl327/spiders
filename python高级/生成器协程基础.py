'''
������python������֪ʶ
��������ʵҲ���ǵ�����
'''
def repeater():
    n = 0
    while True:
        n= (yield n)


'''
send�ǳ�next����һ���ָ��������ķ�����
Python 2.5�У�yield�������yield���ʽ������ζ��yield���ڿ�����һ��ֵ��
�����ֵ��������������send���������ôӶ��ָ�ִ��ʱ������send�����Ĳ�����
����send�����Noneֵǰ�����������봦�ڹ���״̬�������׳��쳣��
���������ȵ���next()���߳�ִ�к͹���
'''
r = repeater()

print r.next()
print r.send(10)

#close�������ڹر����������Թرյ����������ٴε���next��send���׳�StopIteration�쳣
r.close()

