# Mehmet Alp Aysan

import re
import requests
import pprint as pp
import json

def make_suggestions(weather,name,cloth_type):

    # get inputs about the occasion

    rainpattern = r"rain|snow|shower|flurries|storm"
    coldpattern = r"sweat|hoodie|cardigan"
    verycoldpattern = r"coat|jacket|turtleneck"
    warmpattern = r"short|t-shirt|tshirt"

    suggestions = set()

    occasion = input("What is the occasion? ((B)usiness,Casual,Sportwear\n->")

    # get personal info
    persons_url = r"https://webhooks.mongodb-stitch.com/api/client/v2.0/app/our_last_hackson-sfrvf/service/upload_" \
                  r"img/incoming_webhook/find_cloth"

    if cloth_type is None:
        params = {'name':name}
    else:
        params = {'name':name, 'cloth_type':cloth_type}
    a = requests.get(persons_url, params=params)
    possible_attires = json.loads(a.text)

    # TODO:: Weather Suggestions

    for elem in possible_attires:
        # print(elem['url'],elem['cloth'])
        if int(weather["Temperature"]) < 15:
            cold_match = re.search(coldpattern, elem['cloth']['name'])
            if cold_match is not None:
                print("its cold. Would you like a sweater? ")
                suggestions.add(elem['cloth']['name'])

        if int(weather["Temperature"]) < 8:
            very_cold_match = re.search(verycoldpattern, elem['cloth']['name'])
            print("its too cold. Would you like a jacket? " );
            if very_cold_match is not None:
                suggestions.add(elem['cloth']['name'])

        if int(weather["Temperature"]) > 25:
            warm_match = re.search(warmpattern, elem['cloth']['name'])
            if warm_match is not None:
                suggestions.add(elem['cloth']['name'])

        isRainy = re.search(rainpattern,weather["Description"].lower())
        if isRainy is not None:
           suggestions.add("Umbrealla")

    # Occasion Suggestions


        if elem['cloth']['Occasion'] == occasion:
            suggestions.add(elem['cloth']['name'])

    final_url_list = []

    for elem in possible_attires:

        if elem['cloth']['name'] in suggestions:
            final_url_list.append(elem['url'])

    return final_url_list

weather = dict()
weather["Description"] = "Partly Cloudy"
weather["Temperature"] = "22"
res = make_suggestions(weather, "Alp", None)
# print("--done--")
print(res)
