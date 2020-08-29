# -*- coding: utf-8 -*-
#kaggle_script.ipynb


#Installing kaggle API for more info: https://github.com/Kaggle/kaggle-api
!pip install kaggle

#Upload kaggle token from profile
from google.colab import files
files.upload()

#move token to /kaggle dir
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

#Copy from kaggle API the command to download the dataset
!kaggle datasets download -d ktaebum/anime-sketch-colorization-pair

#Checking if the downloaded document is there
!ls



#Unzip download dataset
import zipfile
zip_ref= zipfile.ZipFile('anime-sketch-colorization-pair.zip','r')
zip_ref.extractall('/content/drive/My Drive/manga_data/data')
zip_ref.close()

#Mounting google Drive
from google.colab import  drive
drive.mount('/content/drive')

#Moving data from colab to drive
!mv '/content/files' '/content/drive/My Drive/manga_data/data'