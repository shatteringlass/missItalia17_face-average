import os

proj_name = 'missItalia17_face-average'

year = [2017]

baseURL = 'http://www.missitalia.it/'
endURL = 'finale' + str(year[0]) + "/fotofinaliste/thumbs/"
URL = baseURL + endURL

finaliste = 30
filetype = '.jpg'

def filetypeNoDots(filetype):
    return filetype.replace('.', '')

path = os.path.join(os.path.expanduser('~'), proj_name, filetypeNoDots(filetype))

def main():
    downloadURLs(buildURLList(URL, finaliste), path)


def buildURLList(URL, elNum):
    return [URL + '{0:0=2d}'.format(i) + filetype for i in range(1, elNum + 1)]


def downloadURLs(URLList, path):
    import requests
    import shutil
    if not os.path.exists(path):
        os.makedirs(path)
    for url in URLList:
        img_data = requests.get(url, stream=True)
        file = os.path.join(path, '{0:0=2d}'.format(URLList.index(url)+1) + filetype)
        with open(file, 'wb') as handler:
            shutil.copyfileobj(img_data.raw, handler)
    del img_data


if __name__ == '__main__':
    main()
