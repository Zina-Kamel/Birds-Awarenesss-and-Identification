import tensorflow as tf
from PIL import Image
import numpy as np
import pandas as pd
import os
from labels import *

def load_model():
    """Loads and caches the TFLite model for inference."""

    tflite_model_path = 'model/birds.tflite'
    interpreter = tf.lite.Interpreter(tflite_model_path)
    #Allocate memory for the input and output tensors used by the TFLite model
    interpreter.allocate_tensors()
    # the input details contain the concerned datatype and the expected input size
    # This will come in handy while pre-processing the uploaded image
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    return interpreter, input_details, output_details

def run_inference(model, image, input_details, output_details):
    """Runs inference on the input image and returns the probability list (unsorted)."""

    #Resizing the input image as per the model requirements
    expected_dims = input_details[0]['shape'][1:3]
    image = image.resize(expected_dims, Image.ANTIALIAS)

    #Taking only 3 channels in case of any png image that have 4 channels
    image = np.asarray(image, dtype=np.float32)[:,:,:3]/255.0
    #Since, the model expects the image in a batch, so we add another dimension
    # To make the new dimension as 1 x width x height x 3
    image = image.reshape([1, image.shape[0], image.shape[1], 3])
    #Input the image to the TFLite model and run inference with invoke()
    model.set_tensor(input_details[0]['index'], image)
    model.invoke()
    #Collect the output probabilities for all labels
    species = model.get_tensor(output_details[0]['index'])
    return species

def display_inference(labels, model_output=None, for_catalog=False, num_predictions=3):
    if not for_catalog:
        model_output = model_output.flatten()
        # Calculate the top 3 indices with the highest probabilities
        top_indices = model_output.argsort()[-3:][::-1]
        top_scores = [round(model_output[index]*100, 2) for index in top_indices]
        # Retrieve name of the species from the labels using indices
        top_preds = [labels[index] for index in top_indices]

    #DIsplay catalog image with the basic and detailed info from database

    for num_prediction in range(num_predictions):
        #Divide into sub-parts for catalog image and info
        pred_image, pred_info = st.beta_columns([1,2])
        if not for_catalog:
            name = top_preds[num_prediction]
            index = top_indices[num_prediction]
        else:
            name = labels[num_prediction]
            index = num_prediction

def getList(dict):
    return list(dict.keys())

labels = getList(dic)

#transforming names into wikipedia links
def get_wiki_url(i, labels):
    name = labels[i]
    name_lower = name.lower()
    new_name = name_lower.replace(" ", "_")
    return "https://en.wikipedia.org/wiki/" + new_name

wiki_urls = [""]*len(labels)

for i in range(len(labels)):
    wiki_urls[i] = get_wiki_url(i, labels)

