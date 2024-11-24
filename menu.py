def tong():
    a=int(input("nhập vào số a :"))
    b=int(input("nhậ vào số b :"))
    print("tổng là : ", a+b)
def nt():
    n=int(input("nhập vào số n"))
    if(n<2):
        print(n,":không phải là số nguyên tố")
        return
    for i in range(2,n):
        if(n%2==0):
            print(n,":không phải là số nguyên tố")
            return
    print(n,":không phải là số nguyên tố")
while(True):
    print("0 : thoát chương trình")
    print("1 : tính tổng")
    print("2 : kiêm tra nguyên tố")
    n=int(input("bạn chọn chức năng gì :"))
    if(n==0):
        break
    if(n==1):
        tong()
    if(n==2):
        nt()