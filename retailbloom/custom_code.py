import datetime
from datetime import date, timedelta
import csv, codecs


def handle_uploaded_file(f, fileName):
    #converts the file name to include today's date
    # time = datetime.datetime.today().strftime('%d-%m-%y')
    fileLocation = 'media/retailbloom/uploads/{}'.format(fileName)
    with open(fileLocation, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return fileLocation
