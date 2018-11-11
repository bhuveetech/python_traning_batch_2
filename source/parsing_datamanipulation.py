from util.logger import get_logger
import pandas as pd
from pprint import pprint
logger = get_logger()

# pyopenxl

# df = pd.read_excel("..\config\sample_superstore.xls")
#
# logger.info(df.describe())
# pprint(df.head())
# pprint(df.tail())
# pprint(df.Category)
# # df.iloc[start_row:end_row, start_column:end_column]
# pprint(df.iloc[0:10,2])
# #
# pprint(df.loc[(df.Category == "Furniture") & (df.Profit < 0), ["Product Name"]])

# df.sort_values(df.Category)
#


# ================= lxml - To parse xml and html files ================= #

# https://lxml.de/tutorial.html
import requests
rs = requests.get("http://google.com")
print(rs.content)

from lxml import etree as et
from io import StringIO

html_parser = et.HTMLParser()

parsed_cont = et.parse(StringIO(rs.text), html_parser)
logger.info(parsed_cont.getroot())
print(dir(parsed_cont))
for elm in parsed_cont.iter():
    print(elm.tag)
    print(elm.get("id"))
# elm = parsed_cont.xpath("/html/body/div/div[2]")
