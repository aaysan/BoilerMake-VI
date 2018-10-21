# Mehmet Alp Aysan


import cognitive_face as CF


def get_face_id(url):

    result = CF.face.detect(url)

    if 'faceId' not in result[0]:
        print(result)
        print("Face ID Issue")
        return ""

    return result[0]['faceId']


##TODO: try catch ekle

def lookup_face(faceId, url):
    if faceId != "":

        listresponse = CF.face_list.get("smartdrobe")
        myname = "unknown name"

        if len(listresponse['persistedFaces']) > 0:
            res = CF.face.find_similars(face_id=faceId, face_list_id="smartdrobe")

            newperson = True
            # face_verif = "n"

            if len(res) > 0:

                for elem in listresponse["persistedFaces"]:
                    if elem["persistedFaceId"] == res[0]["persistedFaceId"]:
                        myname = elem["userData"]

                print("Welcome " + myname)
                return myname

        if myname == "unknown name":
            newperson = input("Should we add you to our directory?(y\\n) ")
        else:
            newperson = False

        name = ""
        if newperson == "y" or newperson == True:
            name = input("What is your name? ")
            CF.face_list.add_face(url,"smartdrobe",user_data=name)
        else:
            return ""

        return name


# if __name__ == "__main__":
#
#     api_key = '4451dd6234604147b336e729fd121333'
#     key = api_key  # Replace with a valid Subscription Key here.
#     CF.Key.set(key)
#
#     base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
#     CF.BaseUrl.set(base_url)
#
#     try:
#         CF.face_list.create("smartdrobe")
#     except:
#         print("The list exist.")
#
#     get_face.get_face()
#     url = get_face.get_url_string()
#     print(url)
#     faceId = get_face_id(url)
#     print(faceId)
#     lookup_face(faceId, url)








