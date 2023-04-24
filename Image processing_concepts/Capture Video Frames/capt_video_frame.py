import cv2
vid = cv2.VideoCapture(0) 
i=0
while(True):  
    ret, frame = vid.read()  
    cv2.imshow('frame', frame) 
    # press 'q' to stop the live streaming
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    cv2.imwrite('img'+str(i)+'.jpg',frame)
    i+=1
    
vid.release() 
cv2.destroyAllWindows() 