# Mehmet Alp Aysan

import re
import requests
import pprint as pp
import json

def make_suggestions(weather,name,cloth_type):

    # get inputs about the occasion

    rainpattern = r"rain|snow|shower|flurries|storm"

    suggestions = []

    occasion = input("What is the occasion? ((B)usiness,Casual,Sportwear\n->")

    # TODO:: get the clothes available for that person based on that name
    persons_url = r"https://webhooks.mongodb-stitch.com/api/client/v2.0/app/our_last_hackson-sfrvf/service/upload_" \
                  r"img/incoming_webhook/find_cloth"

    if cloth_type is None:
        params = {'name':name}
    else:
        params = {'name':name, 'cloth_type':cloth_type}
    a = requests.get(persons_url, params=params)
    possible_attires = json.loads(a.text)

    # TODO:: Weather Suggestions

    if int(weather["Temperature"]) < 15:
        print("suggest something like a sweater")


    if int(weather["Temperature"]) < 8:
        print("suggest a jacket")


    isRainy = re.search(rainpattern,weather["Description"].lower())
    if isRainy is not None:
        print("suggest an umbrealla")

    # TODO:: Occasion Suggestions

    for elem in possible_attires:
        pp.pprint(elem)

    if occasion == "Business":
        print("suggest what is on the business in his/her clothes list")


    if occasion == "Casual":
        print("suggest what is on the casual in his/her clothes list")


    if occasion == "Sportwear":
        print("suggest what is on the sportwear in his/her clothes list")


    return suggestions

weather = dict()
weather["Description"] = "Partly Cloudy"
weather["Temperature"] = "22"
make_suggestions(weather, "Natat", None)