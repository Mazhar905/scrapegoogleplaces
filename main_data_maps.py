# -*- coding: utf-8 -*-
import time
import mylogger
import tkinter as tk
from exportData import ExportDataMaps
from maps_data_scraper import GoogleMapsDataScraper
from threading import Thread
import sys
import os
logger = mylogger.MyLogger().get_logger()


class mainGoogleMaps:
    def __init__(self, filePath,filename, parameters):

        self.filePath = filePath
        self.outputFileName = filename
        self.parameters = parameters
        # self.thread = None


        with open(self.filePath, 'r', encoding='utf-8') as archive:
            self.listF = archive.read().splitlines()

        try:
            for i in self.listF:
                data = self.scraperMaps(i)
        except Exception as e:
            logger.exception("Exception occurred", exc_info=True)

        print(data)

        ExportDataMaps(filename, parameters, data)

    def split_list(self,a, n):
        k, m = divmod(len(a), n)
        return list((a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)))


    def scraperMaps(self,kw):
        self.scraper = GoogleMapsDataScraper()
        self.scraper.initDriver()
        place_data = self.scraper.scraperData(kw, self.parameters, self.outputFileName)
        return place_data



if __name__ == "__main__":
    while True:
        filePath = "./test.txt"

        # filePath = input('----------\n[1] Introduce the path of the keywords txt file: ')
        if (os.path.isfile(filePath) == False):
            print(
                "----------\n** Error ** That is not a valid txt file. Enter a valid file\n")
            continue
        else:
            break

#     parameters = input('----------\n[2] Add parameters (address, website, category, hours): ')
#     filename = input('----------\n[3] Introduce the name of your output file: ')
#     fileformat = input('----------\n[4] Introduce the fileformat of your output file: ')

    parameters = ['title', 'coords', 'website',  'address']
    Outputfilename= 'result1.csv'
    # Outputfilename= 'result.xlsx'
    start_time = time.time()
    formatted_time = time.strftime("%H:%M:%S", time.localtime(start_time))
    print(f"Starting Time:  {formatted_time}")
    mainGoogleMaps(filePath,Outputfilename, parameters )
    elapsed_time = time.time()
    f_time = time.strftime("%H:%M:%S", time.localtime(elapsed_time))

    print(f"Starting Time: {formatted_time}\nEnding Time: {f_time}")
    
    # end_time = time.strftime("%H:%M:%S", time.localtime(elapsed_time))

    # print("time:", elapsed_time/60, 'minutes')
    t = time.time()
    # f_time = time.strftime("%H:%M:%S", time.localtime(t))
    print(f"Elapsed time: {(elapsed_time- start_time):0.4f} seconds")
    print(f"Elapsed time: {(elapsed_time- start_time)/60:0.4f} minutes")
