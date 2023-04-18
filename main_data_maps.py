# -*- coding: utf-8 -*-


from exportData import ExportDataMaps
from maps_data_scraper import GoogleMapsDataScraper
from threading import Thread
import sys
import os


def split_list(a, n):
    # print("a and n", a, n)
    # a = ["Liam's restaurant San Francisco", 'Toronto Ontario Canada'], n = 5
    k, m = divmod(len(a), n)
    # print(k, m) (0, 2)
    return list((a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)))


def scraperMaps(list, results, thread):
    # print(list, results, threads)
    scraper = GoogleMapsDataScraper()
    scraper.initDriver()

    listPlaces = []
    count = 1
    for l in list:
        # here we return the dictionories
        Place = scraper.scraperData(l)
        if (Place != None):
            print('Thread # '+str(thread)+' ' + str(count) +
                  '/' + str(len(list)) + ' - OK - ' + l)
            listPlaces.append(Place)
        else:
            print('Thread # '+str(thread)+' ' + str(count) +
                  '/' + str(len(list)) + ' - ERROR - ' + l)
            count += 1

    results[thread] = listPlaces


def mainGoogleMaps(filePath):
    with open(filePath, 'r', encoding='utf-8') as archive:
        listF = archive.read().splitlines()

    threads = 1
    listthreads = [None] * threads
    listresults = [None] * threads
    divided = split_list(listF, threads)
    # print("divided", divided)
    for i in range(len(listthreads)):
        listthreads[i] = Thread(target=scraperMaps, args=(
            divided[i], listresults, i,))
        listthreads[i].start()

    for i in range(len(listthreads)):
        listthreads[i].join()

    listFinal = []

    for i in range(len(listresults)):
        listFinal = listFinal + listresults[i]
    export = ExportDataMaps('ResultOutput.xlsx', '', listFinal)
    export.exportExcel()


if __name__ == "__main__":
    while True:
        filePath = "/home/mazhar/Documents/scrap_google_places/google_maps_scraper/test.txt"

        # filePath = input(
        # '----------\n[3] Introduce the path of the keywords txt file: ')
        if (os.path.isfile(filePath) == False):
            print(
                "----------\n** Error ** That is not a valid txt file. Enter a valid file\n")
            continue
        else:
            break

    mainGoogleMaps(filePath)
