import requests
import json
import csv
import re
from bs4 import BeautifulSoup as bs

#
# soldier_portraits_australasian_traveller.csv
#

spat_data = []


def get_img_url(pid):
    return "http://bishop.slq.qld.gov.au/j2k/jpegNavMain.jsp?pid=" + pid


with open("CSV/soldier_portraits_australasian_traveller.csv") as f:
    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        print("Getting: '" +
              row["Full name and service number (from National Archives of Australia)"] + "'")
        spat_data.append({"default": {
            "pid": row["PID"],
            "image_title": row["Title of image"],
            "temporal": row["Temporal"],
            "image_caption": row["Image caption"],
            "full_name_serv_num": row["Full name and service number (from National Archives of Australia)"],
            "full_name": row["Full name from embarkation roll (from Australian War Memorial) 2"],
            "naa_ident": row["NAA identifier"],
            "embark_ship": row["Embarkation ship (from Australian War Memorial) 2"],
            "embark_date": row["Date of embarkation (from Australian War Memorial) 2"],
            "provenance": row["Provenance"],
            "img_num": row["Image number"],
            "source": row["Source"],
            "subjects": [
                row["Subject 1"],
                row["Subject 2"],
                row["Subject 3"],
                row["Subject 4"],
                row["Subject 5"]
            ],
            "perm_image_link": row["Link to permananent portrait image"]
        }, "extra": {"image_url": get_img_url(row["PID"])}})

with open("outputs/soldier_portraits_australasian_traveller.json", "w") as f:
    f.write(json.dumps(spat_data))
