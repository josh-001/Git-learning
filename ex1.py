from yolov5 import detect

img_url = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'

detect.run(source=img_url, weights="yolov5s6.pt", conf_thres=0.25, imgsz=640)
