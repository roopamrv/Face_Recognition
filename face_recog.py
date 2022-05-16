import cv2
import face_recognition


imgpath = "/Users/roopamverma/PycharmProjects/Images/Roopam.webp"
img = cv2.imread(imgpath)
# Converting image from bgr to rgb
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# As it can load multiple images there using only index 0
img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2path = "/Users/roopamverma/PycharmProjects/Images/Sheetam.jpeg"
img2 = cv2.imread(img2path)
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2_encoding = face_recognition.face_encodings(rgb_img2)[0]

Image_result = face_recognition.compare_faces([img_encoding], img2_encoding)

print("Image Comparison Result: ", Image_result)


cv2.imshow("Img", img)
cv2.imshow("Img2", img2)
cv2.waitKey(0)


