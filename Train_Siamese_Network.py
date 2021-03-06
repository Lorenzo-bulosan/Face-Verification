# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:46:09 2020
@author: lorenzo
Description: Trains the siamese network Vgg16 with the data inside the database
"""

#%% Import libraries
from Siamese_Network import SiameseFaceNet

#%% Main function to train given a database

def main():
	
    # From class above
    fnet = SiameseFaceNet() 

    # Folder paths
    model_dir_path = './models_v2'
    fnet.load_model(model_dir_path)
    KnownImages_dir_path = "./data/Known-Images"
       
    # Encodings of People to verify against
    database = dict()
    database["lorenzo"] = [fnet.img_to_encoding(KnownImages_dir_path + "/lorenzo.jpg")]
    database["karianne"] = [fnet.img_to_encoding(KnownImages_dir_path + "/karianne.jpg")]
    database["taner"] = [fnet.img_to_encoding(KnownImages_dir_path + "/taner.jpeg")]
    database["gwen"] = [fnet.img_to_encoding(KnownImages_dir_path + "/gwen.jpeg")]
    
    # Train given database
    fnet.fit(database=database,model_dir_path=model_dir_path, epochs=500, batch_size=4, threshold=0.15)
    

#%% Calling main

if __name__ == '__main__':
	main()

#%%