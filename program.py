# Nhận diện gương mặt bằng openCV
import cv2
img = cv2.imread('images/queen.jpg') # Ảnh gốc cần detect
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Tạo một bức ảnh xám từ ảnh gốc
cv2.imshow("Gray picture", gray)
cv2.waitKey()
# Sử dụng haar cascade classifier của openCV
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Sử dụng phương thức detectMultiScale để phát hiện khuôn mặt trong bức ảnh xám
faces = faceCascade.detectMultiScale(
    gray, # nguồn bức ảnh xám
    scaleFactor=1.1, # độ scale sau mỗi lần quét, tính theo 1%. Nếu như đẻ scaleFactor = 1 thì tấm ảnh sẽ giữ nguyên
    minNeighbors=5, # scale và quét ảnh cho đến khi không thể scale được nữa thì lúc này sẽ xuất hiện những khung ảnh trùng nhau, số lần trùng nhau chính là tham số minNeighbors để quyết định cho việc có chọn khung ảnh này là khuôn mặt hay không
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)
# Sau khi tính toán thì dữ liệu các khuôn mặt đã có trong biến faces, để xác thực chúng ta vẽ nó lên bức ảnh gốc và phác họa ra màn hình
# Draw
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# Write a new image with detecting faces
cv2.imwrite('images/queen-fd.jpg', img)
# Show
cv2.imshow("Face detect", img)
cv2.waitKey()