from imageupload import uploadimage
import Apparel
import pprint as pp
import get_face
import weather
import get_face_id
import cognitive_face as CF
import requests
import time


if __name__ == "__main__":


    api_key = '4451dd6234604147b336e729fd121333'
    key = api_key  # Replace with a valid Subscription Key here.
    CF.Key.set(key)

    base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(base_url)

    # weather_info = weather.get_weather_info()
    #
    # weather_database_url = r'https://webhooks.mongodb-stitch.com/api/client/v2.0/app/our_last_hackson-sfrvf/service/' \
    #                        r'weather/incoming_webhook/post_weather'
    #
    # requests.post(weather_database_url, json=weather_info)

    try:
        CF.face_list.create("smartdrobe")
    except:
        pass


    face_flag = True
    get_face.get_face()
    url = get_face.get_face_url_string()
    # print(url)
    faceId = get_face_id.get_face_id(url)
    # print(faceId)
    #
    nameofperson = get_face_id.lookup_face(faceId, url)

    face_database_url = r'https://webhooks.mongodb-stitch.com/api/client/v2.0/app/our_last_hackson-sfrvf/service/Capt' \
                        r'ure_face/incoming_webhook/face_detected'
    face_info = dict()
    face_info["name"] = nameofperson
    face_info["url"] = url
    requests.post(face_database_url, json=face_info)

    count = 0
    face_flag = False
    clothes_added_request = False
    nameofperson = ""
    while True:

        if count % 60 == 0:
            count = 0
            face_flag = False

        count += 1


        # input("Press s to start")
        #
        # a = "n"
        # while a == "n":
        # temp = ""
        #
        # while temp == "":
        #     temp = input("Are you ready? ")
        # count += 1
        clothes_add_url = r"https://webhooks.mongodb-stitch.com/api/client/v2.0/app/our_last_hackson-sfrvf/service" \
                          r"/add_cloth/incoming_webhook/ping_add_cloth"
        clothesreq = requests.get(clothes_add_url)

        print(clothesreq.text)
        if '{' in clothesreq.text:
            clothes_added_request = True
        else:
            clothes_added_request = False

        print(clothes_added_request)
        if clothes_added_request:
            Apparel.getApparel()
            #
            imurl = Apparel.get_clothing_url_string()
            cloth, colors = Apparel.finditemandcolor(imurl)
            pp.pprint(imurl)
            pp.pprint(cloth)
            pp.pprint(colors)

            clothes_database_url = r'https://webhooks.mongodb-stitch.com/api/client/v2.0/app/our_last_hackson-sfrvf/service/' \
                                   r'upload_img/incoming_webhook/upload_cloth_img'
            clothes_info = dict()
            clothes_info["name"] = nameofperson
            clothes_info["url"] = imurl
            clothes_info["cloth"] = cloth
            clothes_info["colors"] = colors

            requests.post(clothes_database_url, json=clothes_info)

        time.sleep(1)







