# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2

print(cv2.__version__)
img = cv2.imread('images/parrot.jpg')
cv2.imshow('Display image', img)
cv2.waitKey()  # là hàm chờ không cho thoát cửa sổ lập tức mà phải chờ người dùng nhấn phím bất kỳ để thoát
# Lấy kích thước ảnh ==> Viết example api bằng FastAPI lấy thông tin của ảnh upload lên
(w, h, d) = img.shape
print("width={}, height={}, depth={}".format(w, h, d))
# Lấy giá trị màu ở 1 điểm ảnh
(R, G, B) = img[150, 150]
print("R={}, G={}, B={}".format(R, G, B))
# Cắt ảnh có tọa độ điểm trên cùng bên trái là (50, 60) và tọa độ điểm dưới cùng bên phải là (350, 360)
cut = img[50:350, 60:360]
cv2.imshow('Region of interest', cut)
cv2.waitKey()
# Thay đổi kích thước ảnh: resize
# Đoạn lệnh dưới biến đổi ảnh gôc sang ảnh có chiều cao là 300px
r = 300 / h
dim = (300, int(w * r))
resized = cv2.resize(img, dim)
cv2.imshow('Resized image', resized)
cv2.waitKey()
# Xoay ảnh
# Để xoay được ảnh cần phải xác định gốc xoay và hướng xoay. Sau khi xác định xong ta tính ma trận xoay bằng hàm getRotationMatrix2D trong opencv. Cuối cùng ta nhân ma trận này với ma trận ảnh gốc ta được ảnh sau khi xoay (warpAffine)
# Đoạn lệnh dưới xoay ảnh một góc 180 độ theo chiều ngược kim đồng hồ với gốc xoay là điểm chính giữa hình ảnh (center)
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow('Rotated image', rotated)
cv2.waitKey()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
