import cv2
import time
import math


initialTime =0
initialDistance =0
changeInTime =0
changeInDistance =0

listDistance =[]
listDistance2=[]

listSpeed = []
listSpeed2 =[]

know_distance = 30 #centimer
know_width = 14.3

GREEN = (0,255,0)
RED = (0,0,255)
WHITE = (255,255,255)
fonts = cv2.FONT_HERSHEY_COMPLEX
# cap = cv2.VideoCapture(0)




face_detector = cv2.CascadeClassifier("aksml.xml")
#focal length finder
def FocalLength(measured_distance, real_width,width_in_rf_image):
    focal_length = (width_in_rf_image*measured_distance)/real_width
    return focal_length

#distance finder
def Distance_finder(Focal_length,real_face_width,face_width_in_frame):
    distance = (real_face_width*Focal_length)/face_width_in_frame
    return distance







def face_data(image):
    face_width = 0
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image,1.3,5)
    for(x,y,h,w) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),WHITE,1)
        face_width = w
    return face_width



def speedFinder(coveredDistance,timeTaken):

    speed = coveredDistance/timeTaken
    return speed

def averageFinder(completeList,averageOfItems):
    #findin length
    lengthOfList =len(completeList)
    #calculating no. of items to find average
    selectedItems = lengthOfList-averageOfItems
    # getingg the list mos
    selectedItemsList = completeList[selectedItems:]
# finding the average
    average = sum(selectedItemsList)/len(selectedItemsList)
    return average


#readding referance imaage
ref_image = cv2.imread("image.jpg")
ref_image2 = cv2.imread("image.jpg")
ref_image_face_width = face_data(ref_image)
ref_image_face_width2 = face_data(ref_image2)
Focal_length_found = FocalLength(know_distance,know_width,ref_image_face_width)
Focal_length_found2 = FocalLength(know_distance,know_width,ref_image_face_width2)
print(Focal_length_found)
print(Focal_length_found2)
# cv2.imshow("ref_image",ref_image)



cap = cv2.VideoCapture("grpvid.mp4")



while True:
    _, frame = cap.read()

    face_width_in_frame = face_data(frame)
    face_width_in_frame2 =face_data(frame)
    #finding the distance by caclling function ditance finder
    if face_width_in_frame!=0:

        Distance = Distance_finder(Focal_length_found,know_width,face_width_in_frame)
        Distance2 = Distance_finder(Focal_length_found2,know_width,face_width_in_frame2)
    #drawing text on screen
        listDistance.append(Distance)
        listDistance2.append(Distance2)

        averageDistance = averageFinder(listDistance,2)
        averageDistance2 =averageFinder(listDistance2,2)


        #convertung centimeter into meter
        distanceInMeters = averageDistance/100
        distanceInMeters2=averageDistance2/100
        if(initialDistance!= 0):

            # finding change in distance
            changeInDistance = initialDistance-distanceInMeters
            # finding change in time
            # if changeInDistance<0:
            #     changeInDistance* -1
            changeInTime = time.time() - initialTime
            #finding the speed
            speed = speedFinder(coveredDistance=changeInDistance,timeTaken=changeInTime)
            listSpeed.append(speed)
            averageSpeed = averageFinder(listSpeed,4)
            cv2.line(frame,(45,70),(255,70),(0,0,0),28)
            cv2.putText(frame,f"speed: {round(averageSpeed,2)} m/s",(50,75),fonts,0.6,GREEN,2)


            # print(speed)
        # initialDistance and timw
        initialDistance = distanceInMeters
        initialDistance2=distanceInMeters2
        initialTime = time.time()
        cv2.putText(frame,f"Distance = {Distance}",(50,50),fonts,0.6,(WHITE),2)
        cv2.putText(frame,f"Distance2 = {Distance2}",(50,100),fonts,0.6,(WHITE),2)




    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


