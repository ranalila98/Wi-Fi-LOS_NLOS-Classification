# Wi-Fi Received Signal Strength (RSS) and Round Trip Time (RTT) dataset
Data measurement was done using Google Pixel 2 smartphone and Google nest wifi router, 

# Problem Description

To classify the indoor scenario based on wifi RSS and RTT values which is useful for accuracy improvement of wifi indoor positioning

### Dataset Decsription

Measurements were taken on 4 different indoor locations scenarios:

* LOS- No obstacle between smartphone and router
* Glass - A glass door obstacle between smartphone and router
* Metal - A metal door obstacle between smartphone and router
* Wall - A wall obstacle between smartphone and router


In every scenario 150 samples were taken at each meter from 1 m to 14 m. L

ine of Sight Count : 3243
Glass Count : 2852
Metal Count : 3017
Wall Count : 3064

 To make data set ready for building LOS and NLOS scenario classification model, samples are randomized to prevent overfitting of a model to particular places. 

 ## Importing Data Set in Python

To import data set data into Python environment, **dataset.py** script can be used. The CIR data still needs to be divided by number of acquired RX preamble samples (RX_PACC).

	import dataset
	
	# import raw data
	data = dataset.import_from_files()
	print(data)

