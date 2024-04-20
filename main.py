from ultralytics import YOLO

model = YOLO("yolov8m.yaml")  

model.train(data="config.yaml", epochs=500)  