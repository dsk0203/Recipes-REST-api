# Recipes-REST-api

A REST API running on AWS (Amazon Web Services) EC2 instance Ubuntu 18.02 LTS.

Taking incredibly messy data, transforming this data into a helpful API that can return recipes to cook based on current ingredients on hand. Pass ingredients with HTTP and GET request. 


User will pass in ingredients with

18.224.181.112:8080/recipes?i=ingredient1"&"i=ingredient2"&"i=ingredient3 etc..

Cleaning Data Files:
Data_Clean.ipynb
API_backbone.ipynb

File running on EC2:
flask_api_server.py


The original Data:

![ScreenShot](https://github.com/dsk0203/Recipes-REST-api/blob/master/original_dataset.JPG)


Curl Example & Response: 

![ScreenShot](https://github.com/dsk0203/Recipes-REST-api/blob/master/curl.JPG)




