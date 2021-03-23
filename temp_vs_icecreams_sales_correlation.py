import plotly.express as px
import csv
import numpy as np

def get_data_source(data_path):
    ice_cream_sales = []
    temperature = []

    with open(data_path) as f:
        reader = csv.DictReader(f)

        for row in reader:
            temperature.append(float(row["Temperature"]))
            ice_cream_sales.append(float(row["Ice-cream Sales"]))

    return {"x" : temperature, "y" : ice_cream_sales}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between temperature vs ice-cream sales is : \n--->", correlation[0,1])

def setup():
    data_path = "py2/data/icecreams sales vs temp data.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)

setup()