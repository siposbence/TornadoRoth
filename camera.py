import cv2


vcap = cv2.VideoCapture("rtsp://hackathon:!Hackath0n@192.168.0.2:554/2")


print(vcap)

while(1):

    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)
