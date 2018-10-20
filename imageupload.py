import pyimgur

CLIENT_ID = "Your_applications_client_id"
PATH = "A Filepath to an image on your computer"

def uploadimage(PATH):
    im = pyimgur.Imgur("100ef2fd6ae00e0")
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    return(uploaded_image.link)
    #print(uploaded_image.date)
    #print(uploaded_image.url)
    #print(uploaded_image.link)

if __name__ == "__main__":
    print(uploadimage("image1.jpg"))
    print(type(uploadimage("image1.jpg")))