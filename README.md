# Birds-Awarenesss-and-Identification

This project is aimed at helping raise awareness about rare and endangered species of birds. It is a web application powered by Computer Vision 
that can detect more than 270 species of birds and provide important details about them (species, diet, endangered status, current distribution..)

[![Made with Python](https://img.shields.io/badge/Made%20with%20-Python-red?style=for-the-badge&logo=python)](http://www.python.org/)
[![Made with TfLite](https://img.shields.io/badge/Made%20with%20-Tf%20Lite-yellow?style=for-the-badge&logo=tensorflow)](http://www.tensorflow.org/)



## What I used:
* Flask
* Beautiful Soup
* TensorFlow and TensorFlow Lite 
* OpenCV
* InceptionResNetV2

## More about the project:

I first trained the model on the dataset which includes more than 270 species of birds and got an accuracy of more than 97%. Then I converted the model to tflite for deployment. 
To get infromation about the birds, I used Beautiful Soup to scrape data and wrote a python script to extract the url from the names.

## Downloading the app:

If you prefer to run it from your local host follow these steps:

### Cloning

You can clone the repository using the following URL

```bash
$ https://github.com/Zina-Kamel/Birds-Awarenesss-and-Identification.git
```

### Installing Requirements
Use the following to install the required packages

```
$ pip install -r requirements.txt
```

### Running the App
Now it's time to know more about birds!
Run the Flask app using
```bash
$ python run app.py
```

Upload your bird's picture using the upload button or add and drop to get all the important information about the bird!
