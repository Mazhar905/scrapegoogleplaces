# -*- coding: utf-8 -*-


import logger
import logging
import pandas as pd
from exportData import ExportDataMaps
from maps_data_scraper import GoogleMapsDataScraper
from threading import Thread
import sys
import os


def split_list(a, n):
    k, m = divmod(len(a), n)
    return list((a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)))


def scraperMaps(list, results, thread):
    scraper = GoogleMapsDataScraper()
    scraper.initDriver()

    listPlaces = []
    count = 1
    for l in list:
        # here we return the dictionories
        Place = scraper.scraperData(l)
        if (Place != None):
            logger.error(f'Thread # {thread} {count}/{len(list)} - OK - {l}')
            listPlaces.append(Place)
        else:
            logger.info(
                f'Thread # {thread} {count}/{len(list)} - ERROR - {l}')
            count += 1

    results[thread] = listPlaces


def mainGoogleMaps(keywords):
    threads = 1
    listthreads = [None] * threads
    listresults = [None] * threads
    divided = split_list(keywords, threads)
    try:
        for i in range(len(listthreads)):
            listthreads[i] = Thread(target=scraperMaps, args=(
                divided[i], listresults, i,))
            listthreads[i].start()
    except Exception as e:
        logger.exception("Exception occurred", exc_info=True)

    for i in range(len(listthreads)):
        listthreads[i].join()

    listFinal = []

    for i in range(len(listresults)):
        listFinal = listFinal + listresults[i]

    export = ExportDataMaps('ResultOutput.xlsx', '', listFinal)
    export.exportExcel()


if __name__ == "__main__":
    while True:
        filePath = "./test.txt"

        # filePath = input(
        # '----------\n[3] Introduce the path of the keywords txt file: ')
        if (os.path.isfile(filePath) == False):
            print(
                "----------\n** Error ** That is not a valid txt file. Enter a valid file\n")
            continue
        else:
            break

    # # Read the CSV file using pandas and extract the columns we need
    # data = pd.read_csv('canadacities.csv', usecols=['city', 'province_id'])

    # # Generate the list of search keywords
    # keywords = []

    with open(filePath, 'r', encoding='utf-8') as archive:
        listF = archive.read().splitlines()
    # for j in range(len(listF)):
    #     for i in range(len(data)):
    #         city = data.iloc[i][0]
    #         province = data.iloc[i][1]
    #         kw = listF[j]
    #         keyword = f"{kw} in {city}, {province}, canada"
    #         keywords.append(keyword)

    mainGoogleMaps(listF)
