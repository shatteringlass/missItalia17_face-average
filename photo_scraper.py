import os

proj_name = 'missItalia_face-average'

year = [x for x in range(2015,2017+1)]

URLdict = {'2017': 'http://www.missitalia.it/finale2017/fotofinaliste/thumbs/',
           '2016': 'http://web.archive.org/web/20170717170823im_/http://www.missitalia.it/finale2016/fotofinaliste16/',
           '2015': 'http://web.archive.org/web/20150926162637if_/http://www.missitalia.it/finale2015/fotofinaliste15/'}

finaliste = {'2017': 30,
             '2016': 40,
             '2015': 33}

filetype = '.jpg'

def filetypeNoDots(filetype):
    return filetype.replace('.', '')

path = os.path.join(os.path.expanduser('~'), proj_name, filetypeNoDots(filetype))

def getURL(URLdict, year):
    return URLdict.get(year)

def getFinaliste(finaliste, year):
    return finaliste.get(year)

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

def main():
    for i in year:
        yp = os.path.join(path, str(i))
        u = getURL(URLdict, str(i))
        f = getFinaliste(finaliste, str(i))
        ul = buildURLList(u, f)
        downloadURLs(ul, yp)

if __name__ == '__main__':
    main()
