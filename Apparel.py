from clarifai.rest import Image as ClImage

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import pprint as pp

def finditemandcolor(imageurl):

    app = ClarifaiApp(api_key='e5af645934f34cee8ec140028c1fff12')
    model = app.models.get('apparel')
    image = ClImage(url=imageurl)
    itemspredict = model.predict([image])

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

    #pp.pprint(colorpredict)

    try:
        colorlist = sorted(colorpredict["outputs"][0]["data"]["colors"], key=lambda k: k['value'],reverse=True)
        if(len(colorlist)>5):
            colorlist = itemlist[:5]
        else:
            colorlist = colorlist
    except:
        colorlist = []

    finalitemlist = []
    finalcolorlist = colorlist
    tempdict = dict()

    for i in itemlist:
        tempdict["name"] = i["name"]
        tempdict["value"] = i["value"]
        finalitemlist += [tempdict]
        tempdict = dict()

    return(finalitemlist,finalcolorlist)


if __name__ == "__main__":
    temp1,temp2 = finditemandcolor("temp")
    pp.pprint(temp1)
    pp.pprint(temp2)