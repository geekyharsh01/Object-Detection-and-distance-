project1.py

This code is for detecting face and it gives output the speed and distance of that person.
To make this code work 
1)you have to copy aksml.xml file that is for face detection. and type this file name in cascade classifier.
2)give reference image of yours in ref_image
3) at line cap = cv2.video capture put 0 in bracket if u want to give live feedback from cam or give video in " " to give video feed.
 and  thats it simply run the program.

updatedproject.py

This code is for detecting multiplefaces to run this code copy nd just put aksml.xml file there.
and
give ref imafe 1 in ref_image and reference image 2 in ref_image2  thatts it

and finally u can give video feed in videocapture .

multipleProject.py

This code is our final design , it uses yolo algorithm and using this code we can detect distance of multiple objects like car, bottle etc.
As of now we implemented for a mobile and a human and a banana and a bottle.
YOu can add more things just you have to add ref image and known distance for that ref image and just edit the code wherever required.
For this project 3 extra files you need to copy are 
classes.txt
yolov4-tiny.weights
yolov4-tiny.cfg

and video capture put 0 to give cam feed or put video file name to give video feed.






 

