**Leaf Quality AI Mode;**
1. In this exercise I trained a deep learning model for 3 classes Healthy leaf, Early Blight & Late Blight which achieved an accuracy of 99%
2. Then I setup the FastAPI server and created a POST API that takes an images and then provide the confidence and class of the leaf
3. I created a Next14 Project as a basic front-end to take input of image and then post it on the FastAPI server whhere I recieved the results and show it on Front-end

   
## To run the server

Download dependencies:
1. Tensorflow
2. Pillow
3. uvicorn
   
Run command in terminal
``` uvicorn main:app --reload```

Download Postman:
Post the image in body with key of 'file' and select the image in sample folders
