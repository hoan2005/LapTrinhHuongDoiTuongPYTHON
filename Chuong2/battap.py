lis={}
class QuanLyOto:
    hangxe="vinfast"
    def __init__(self,maxe,tenxe,mausac,namsx,gianban,soghe):
        self.maxe=maxe
        self.tenxe=tenxe
        self.mausac=mausac
        self.namsx=namsx
        self.giaban=gianban
        self.soghe=soghe
    def them(self):
        lis[self.maxe]=[self.maxe,self.tenxe,self.mausac,self.namsx,self.giaban,self.soghe]
        print("đã thêm thành công")
    def show(self,maxe):
        if maxe in lis:
            print("ma xe :",lis[maxe][0])
            print("ten xe :",lis[maxe][1])
            print("mau xe :",lis[maxe][2])
            print("namsx xe :",lis[maxe][3])
            print("gia xe :",lis[maxe][4])
            print("so ghe xe :",lis[maxe][5])
            return
        print("mã xe không tồn")
while(True):
    n=input("nhập chức năng bạn muốn")
    if(n==1):
        QuanLyOto.them()




