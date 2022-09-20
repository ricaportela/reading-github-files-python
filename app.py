import pandas as pd
import requests
from bs4 import BeautifulSoup
import io


def get_file_from_github():
    url = 'https://raw.githubusercontent.com/ricaportela/reading-github-files-python/main/Airflow/Cadastral/Carga/procedure1.sql'
    download = requests.get(url).content
    df = pd.read_csv(io.StringIO(download.decode('utf-8')))
    print (df.head())



# URL on the Github where the csv files are stored
github_url = 'https://github.com/ricaportela/reading-github-files-python/blob/main/Airflow/'  # change USERNAME, REPOSITORY and FOLDER with actual name

result = requests.get(github_url)

print(result)

