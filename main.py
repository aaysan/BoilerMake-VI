from imageupload import uploadimage
import Apparel
import pprint as pp
import get_face
import get_weather_info
import get_face_id
import cognitive_face as CF


if __name__ == "__main__":


    api_key = '4451dd6234604147b336e729fd121333'
    key = api_key  # Replace with a valid Subscription Key here.
    CF.Key.set(key)

    base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(base_url)

    weather_tuple = get_weather_info.get_weather_info()

    try:
        CF.face_list.create("smartdrobe")
    except:
        print("The list exist.")



    get_face.get_face()
    url = get_face.get_face_url_string()
    print(url)
    faceId = get_face_id.get_face_id(url)
    print(faceId)

    get_face_id.lookup_face(faceId, url)


    temp = ""

    while temp == "":
        temp = input("Are you ready? ")

    # imurl = uploadimage("image1.jpg")
    Apparel.getApparel()

    imurl = Apparel.get_clothing_url_string()
    temp1, temp2 = Apparel.finditemandcolor(imurl)
    pp.pprint(imurl)
    pp.pprint(temp1)
    pp.pprint(temp2)




