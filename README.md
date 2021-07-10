# Birds-Awarenesss-and-Identification

This project is aimed at helping raise awareness about rare and endangered species of birds. It is a web application powered by Computer Vision 
that can detect more than 270 species of birds and provide important details about them (species, diet, endangered status, current distribution..)

## What I used:
* Flask
* Beautiful Soup
* TensorFlow and TensorFlow Lite 
* OpenCV
* InceptionResNetV2

## More about the project:

I first trained the model on the dataset which includes more than 270 species of birds and got an accuracy of more than 97%. Then I converted the model to tflite for deployment. 
To get infromation about the birds, I used Beautiful Soup to scrape data and wrote a python script to extract the url from the names.


