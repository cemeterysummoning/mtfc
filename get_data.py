import requests
import bs4
import pandas as pd

def get_html():

    r = requests.get('https://waterdata.usgs.gov/ca/nwis/water_use?format=html_table&rdb_compression=file&wu_area=County&wu_year=ALL&wu_county=ALL&wu_category=ALL&wu_county_nms=--ALL%2BCounties--&wu_category_nms=--ALL%2BCategories--')
    df_list = pd.read_html(r.text)
    df_list[1].to_csv("data.csv")


def parse_html():
    with open("data.html") as file:
        soup = bs4.BeautifulSoup(file, "html.parser")
        table = soup.find("table", attrs={'id': 'waterUseHTMLOutput'})
        print(table)
get_html()