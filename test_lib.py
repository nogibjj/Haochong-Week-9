from lib import (
    PlotHistOfTotalConfirmed,
    PlotHistTotalConfirmedVsDate,
    PlotScatter,
    LROfTotalConfirmedVsDate,
)
import pandas as pd

example_csv = "https://data.ca.gov/dataset/4a9a896a-e64e-48c2-bb35-5589f80e7c52/resource/5a3f496d-04be-4405-aea0-e83e26076efc/download/covid19dashboard.csv"
data = pd.read_csv(example_csv)

def test_plot1():
    PlotHistOfTotalConfirmed(example_csv)

def test_plot2():
    PlotHistTotalConfirmedVsDate(example_csv)

def test_plot3():
    PlotScatter(example_csv)

def test_plot4():
    LROfTotalConfirmedVsDate(example_csv)

