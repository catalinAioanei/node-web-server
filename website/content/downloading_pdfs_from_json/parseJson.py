import json
import zipfile
import os

data = json.load(open('camdendata.json'))
path = 'zipdata/'

endpoint = "https://opendata.camden.gov.uk/views/j7mk-4ya8/files/"

fn = os.path.join(os.path.dirname(__file__))

txt_file = open("urls.txt", "w")

for item in data["data"]:
    zip_item = item[11]
    url = endpoint + zip_item[1] + "?filename=" + zip_item[2] + "&content_type=" + zip_item[0] + "\n"
    txt_file.write(url)

txt_file.close()
