import yolov5

# load pretrained model
model = yolov5.load('yolov5s.pt')

# or load custom model
#model = yolov5.load('train/best.pt')
  
# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1  # maximum number of detections per image

# set image
img = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'

# perform inference
results = model(img)

# inference with larger input size
results = model(img, size=1280)

# inference with test time augmentation
results = model(img, augment=True)

# parse results

# show detection bounding boxes on image
results.show()

# save results into "results/" folder
#results.save(save_dir='results/')
