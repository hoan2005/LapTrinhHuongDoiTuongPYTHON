# tạo lớp lớp khuôn mẫu để định dạng các thuộc và phương của 1 đối cụ thể
class QuanLySinhVien:
    # đây hàm tạo thuộc tính tuỳ vào mỗi đối tượng (Đây là hàm có sẵn của PYTHON)
    def __init__(self,a,b) : 
        self.ten=a
        self.masv=b   
    # Phương thức của mỗi đối tượng
    def show(self):
        print("ten sinh vien la :",self.ten)
        print("ma sinh vien la :",self.masv)
# tạo đối tượng dựa trên khuôn mẫu
sinhvien1=QuanLySinhVien("A","01")
sinhvien1.show()
sinhvien2=QuanLySinhVien("B","02")
sinhvien2.show()


""" Lưu ý đối số đầu tiên của phương thức trong hàm là chỉ 1 đối tượng cụ thể"""




