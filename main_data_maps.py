# -*- coding: utf-8 -*-
import mylogger
import tkinter as tk
# import pandas as pd
from exportData import ExportDataMaps
from maps_data_scraper import GoogleMapsDataScraper
from threading import Thread
import sys
import os
logger = mylogger.MyLogger().get_logger()


class mainGoogleMaps:
    def __init__(self, filePath,filename, parameters):

        self.filePath = filePath
        self.filename = filename
        self.parameters = parameters
        self.thread = None


        with open(self.filePath, 'r', encoding='utf-8') as archive:
            self.listF = archive.read().splitlines()

        self.threads = 1
        listthreads = [None] * self.threads
        listresults = [None] * self.threads
        divided = self.split_list(self.listF, self.threads)
        try:
            for i in range(len(listthreads)):
                listthreads[i] = Thread(target=self.scraperMaps, args=(
                    divided[i], listresults, i))
                listthreads[i].start()
        except Exception as e:
            logger.exception("Exception occurred", exc_info=True)

        for i in range(len(listthreads)):
            listthreads[i].join()

        listFinal = []

        for i in range(len(listresults)):
            listFinal = listFinal + listresults[i]

        export = ExportDataMaps(filename, parameters, listFinal)
        export.exportExcel()

    def split_list(self,a, n):
        k, m = divmod(len(a), n)
        return list((a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)))


    def scraperMaps(self,list, results, thread):
        self.scraper = GoogleMapsDataScraper()
        self.scraper.initDriver()

        listPlaces = []
        count = 1
        for l in list:
            # here we return the dictionories
            Place = self.scraper.scraperData(l, self.parameters)
            if (Place != None):
                logger.error(f'Thread # {thread} {count}/{len(list)} - OK - {l}')
                listPlaces.append(Place)
            else:
                logger.info(
                    f'Thread # {thread} {count}/{len(list)} - ERROR - {l}')
                count += 1

        results[thread] = listPlaces



# if __name__ == "__main__":
#     while True:
#         # filePath = "./test.txt"

#         filePath = input('----------\n[1] Introduce the path of the keywords txt file: ')
#         if (os.path.isfile(filePath) == False):
#             print(
#                 "----------\n** Error ** That is not a valid txt file. Enter a valid file\n")
#             continue
#         else:
#             break

#     parameters = input('----------\n[2] Add parameters (address, website, category, hours): ')
#     filename = input('----------\n[3] Introduce the name of your output file: ')
#     fileformat = input('----------\n[4] Introduce the fileformat of your output file: ')

    

#     # # Read the CSV file using pandas and extract the columns we need
#     # data = pd.read_csv('canadacities.csv', usecols=['city', 'province_id'])

#     # # Generate the list of search keywords
#     # keywords = []

#     with open(filePath, 'r', encoding='utf-8') as archive:
#         listF = archive.read().splitlines()
#     # for j in range(len(listF)):
#     #     for i in range(len(data)):
#     #         city = data.iloc[i][0]
#     #         province = data.iloc[i][1]
#     #         kw = listF[j]
#     #         keyword = f"{kw} in {city}, {province}, canada"
#     #         keywords.append(keyword)

#     mainGoogleMaps(listF)
