from imageupload import uploadimage
from Apparel import finditemandcolor
import pprint as pp

if __name__ == "__main__":
    imurl = uploadimage("image1.jpg")
    temp1, temp2 = finditemandcolor(imurl)
    pp.pprint(imurl)
    pp.pprint(temp1)
    pp.pprint(temp2)
