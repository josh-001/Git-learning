from yolov5 import train, val, detect, export
# from yolov5.classify import train, val, predict
# from yolov5.segment import train, val, predict

train.run(imgsz=640, data='coco128.yaml')
val.run(imgsz=640, data='coco128.yaml', weights='yolov5s.pt')
detect.run(imgsz=640)
export.run(imgsz=640, weights='yolov5s.pt')
