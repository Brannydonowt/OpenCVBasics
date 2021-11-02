import os.path
import cv2

fileExists = os.path.isfile('loadvideo/video.mp4')
print(fileExists)

vid_capture = cv2.VideoCapture('loadvideo/video.mp4')
frameDelay = 40
if (vid_capture.isOpened() == False):
    print ("Error opening the video file")
else:
        # Get Framerate info ( 5 = framerate)
        fps = int(vid_capture.get(5))
        print ("Frame Rate : ", fps, " frames per second")

        #Get Frame Count ( 7 = framecount)
        frame_count = vid_capture.get(7)
        print ("Frame count : ", frame_count)

i = 0

while(vid_capture.isOpened()):
    #vCapture.read methods returns a tuple, <bool, frame>

    ret, frame = vid_capture.read()
    if ret == True:
        # output frames to a videoframes folder
        cv2.imwrite('loadvideo/videoframes/img' + str(i) + '.jpg', frame)
        i += 1
        cv2.imshow('Frame', frame)
        k = cv2.waitKey(frameDelay)
        # 113 is ascii code for q key
        if k == ord('q'):
            break
    else:
        break

vid_capture.release()
cv2.destroyAllWindows()