import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image, ImageEnhance



img = Image.open('./working.png')

enhancer1 = ImageEnhance.Sharpness(img)
enhancer2 = ImageEnhance.Contrast(img)
img_edit = enhancer1.enhance(100.0)
img_edit = enhancer2.enhance(100.5)

img_edit.save("edited_image.png")



reader = easyocr.Reader(['hi','en'])
result = reader.readtext("working.png",paragraph="False")

# print(result[0][1])

mainExcelData = []

print("Fetching The Text Activated ")


print(result)
print("==============================The Uplift Data=============================")


print("==============================Complete String=============================")
stringo = result[0][1] + result[1][1] + result[2][1] + result[3][1] 
print(stringo)


applicationID = stringo[0:3]
voterIDCard = stringo[22:33]
name = stringo[33:43]
parentsName = stringo[47:55]
HouseNo = stringo[60:66]
age = stringo[68:78]
sex = stringo[89:90]


# dataWhole = {
#                "applicationID" : applicationID,
#                "voterIDCard" : voterIDCard,
#                "name" : name,
#                "parentsName" : parentsName,
#                "House_No" : HouseNo,
#                "age"  : age,
#                "Sex" : sex, 
#             }


# mainExcelData.append(dataWhole);



print("This is your Application ID " +  applicationID);
print("This is your Application ID " +  voterIDCard);
print(name)
print(parentsName)
print(HouseNo)
print(age)
print(sex)


# pd.DataFrame(mainExcelData).to_excel("dataCleared.xlsx",index=False)
# df = pd.DataFrame([result[0][1]])
# df.to_excel("data.xlsx")




