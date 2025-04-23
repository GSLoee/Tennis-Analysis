from ultralytics import YOLO

model = YOLO('yolov8x')  # Load a custom model (YOLOv5)

# model.predict('input_videos/basketball_image.jpg', save=True)
result = model.track('input_videos/input_video.mp4',conf=0.2, save=True) 
# print(result)
# print("Boxes:")
# for box in result[0].boxes:
#     print(box)
