'getNum������������'
def getNum():
    yield 1
    yield 2
    yield 3

'��������������������һ��������'
generator = getNum()

'''
��һ�ε�����������next����ʱ����������ʼִ�������������������ǹ���������ʱ��
ֱ������yieldʱ��ִͣ�У�����
����yield�Ĳ�������Ϊ�˴�next�����ķ���ֵ
'''
print generator.next()

'''
֮��ÿ�ε�����������next�����������������ϴ���ִͣ�е�λ�ûָ�ִ������������
ֱ���ٴ�����yieldʱ��ͣ������ͬ���ģ�yield�Ĳ�������Ϊnext�����ķ���ֵ
'''
print generator.next()
print generator.next()

'''
���������next����ʱ��������������
�����next�����ĵ��ý��׳�StopIteration�쳣
'''
print generator.next()
