# _*_coding:cp1251_*_

x = int(input("������� �����: "))               # ����� �����
sum = 0                                         # ������� �����
proiz = 1                                       # ������� ������������
while x > 0:                                    # ���� ���� �������� ����� ������ "0"
   dig = x % 10                                 # ������� �� �������
   sum += dig                                   # ��������� ������� � �����
   proiz *= dig                                 # �������� ������� � ������������
   x //= 10                                     # �������� ������� �� ����� � ��������� �����
print("����� ����� = ", sum)                    # ����� ���������� � �������
print("������������ ����� = ", proiz)           # ����� ���������� � �������
