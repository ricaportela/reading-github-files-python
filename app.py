import base64
import requests

main = "https://raw.githubusercontent.com/ricaportela/reading-github-files-python/main/Airflow/Cadastral/Carga/procedure1.sql"
main = 'https://github.com/ricaportela/reading-github-files-python/blob/main/Airflow/Cadastral/Carga/procedure1.sql'
req = requests.get(main)
req = req.text
print(req)