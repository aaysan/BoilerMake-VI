from clarifai.rest import Image as ClImage

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import re
import pprint as pp
import cv2
import pyimgur

CLIENT_ID = "100ef2fd6ae00e0"

def getApparel():
    cv2.namedWindow("Cloth Detection")
    vc = cv2.VideoCapture(2)

    time = 0
    # input("Press s to start")
    while vc.isOpened():
        ret, frame = vc.read()
        if frame is None:
            print("Apperal Detection Error in getApperal")
            break
        time += 1
        if time == 3:
            cv2.imwrite("Clothing.png", frame)
            break

def get_clothing_url_string():
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image("Clothing.png",title="Image for Clothing Detection")
    return uploaded_image.link



def finditemandcolor(imageurl):

    app = ClarifaiApp(api_key='e5af645934f34cee8ec140028c1fff12')
    model = app.models.get('apparel')
    image = ClImage(url=imageurl)
    itemspredict = model.predict([image])

    # pp.pprint(itemspredict)
    model2 = app.models.get('color')
    image = ClImage(url=imageurl)
    colorpredict = model2.predict([image])
    try:
        itemlist = sorted(itemspredict["outputs"][0]["data"]["concepts"], key=lambda k: k['value'],reverse=True)
        if(len(itemlist)>5):
            itemlist = itemlist[:5]
        else:
            itemlist = itemlist
    except:
        itemlist = []

    # pp.pprint(colorpredict)

    try:
        colorlist = sorted(colorpredict["outputs"][0]["data"]["colors"], key=lambda k: k['value'],reverse=True)
        if(len(colorlist)>5):
            colorlist = itemlist[:5]
        else:
            colorlist = colorlist
    except:
        colorlist = []

    finalitemlist = []
    finalcolorlist = []
    tempdict = dict()

    for i in itemlist:
        tempdict["name"] = i["name"]
        tempdict["value"] = i["value"]
        tempdict["Occasion"] = get_occasion(tempdict["name"])
        finalitemlist += [tempdict]
        tempdict = dict()
    tempdict = dict()
    for i in colorlist:
        tempdict["name"] = i["w3c"]["name"]
        tempdict["value"] = i["value"]
        tempdict["hex"] = i["w3c"]["hex"]

        finalcolorlist += [tempdict]
        tempdict = dict()

    return(finalitemlist,finalcolorlist)


def get_occasion(name):
    # Casual, Sportwear, Business/Business Casual

    sportspattern = "activewear|sweatpants|legging|relax|"
    sportwear = re.search(sportspattern, name.lower())


    if sportwear is not None:
        return "Activewear"

    businesspattern = "dress|coat|suit|cardigan|turtle|jacket"
    businesswear = re.search(businesspattern, name.lower())

    if businesswear is not None:
        return "Business"



    return "Casual"

# if __name__ == "__main__":
#     temp1,temp2 = finditemandcolor("https://i.imgur.com/JhwydNl.png")
#     pp.pprint(temp1)
#     pp.pprint(temp2)