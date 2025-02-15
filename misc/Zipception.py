import zipfile

for i in range(3000, 0, -1):
    with zipfile.ZipFile('./zippa/flag' + str(i) + '.zip', 'r') as zip_ref:
        zip_ref.extractall('./zippa')

