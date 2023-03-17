import cv2
from ultralytics import YOLO

model = YOLO("jeremy.pt")
results = model.predict(source="0", show=True)  # predict on an image

cv2.waitKey(0)
cv2.destroyAllWindows()
