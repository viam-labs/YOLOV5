import yolov5

# load model
model = yolov5.load('fcakyon/yolov5n-cls-v7.0')

# set image
img = 'https://github.com/ultralytics/yolov5/raw/master/data/images/zidane.jpg'

# perform inference
results = model(img)

