# -*- coding: utf-8 -*-

import xlwt


class ExportDataMaps:

    def __init__(self, fileName, para, placesList):
        self.fileName = fileName
        self.para = para
        self.placesList = placesList

    def exportExcel(self):
        writeBook = xlwt.Workbook(encoding='utf-8')
        sheet = writeBook.add_sheet("document", cell_overwrite_ok=True)

        # Write header row
        for i, col_name in enumerate(self.para):
             sheet.write(0, i, col_name.upper())

        # Write data rows from a dictionary
        # todo: the placesList is a dictionary
        dic=         {'St. James Park': {'Category': 'Park', 'Title': 'St. James Park', 'Rating': '4.5', 'Phone': '+1 416-392-2489'}}
        row = 0
        for place, attributes in self.placesList.items():
            col = 0
            for key, value in attributes.items():
                sheet.write(row+1, col, value)
                col+=1
            row += 1

        writeBook.save(self.fileName)

    def exportCSV(self):
        pass

    def exportJSON(self):
        pass

        # sheet.write(0, 0, 'CATEGORY')
        # sheet.write(0, 1, 'TITLE')
        # sheet.write(0, 2, 'DESCRIPTION')
        # sheet.write(0, 3, 'RATING')
        # sheet.write(0, 4, 'ADDRESS')
        # sheet.write(0, 5, 'OPENING/CLOSING HOURS')
        # sheet.write(0, 6, 'WEBSITE')
        # sheet.write(0, 7, 'PHONE')
        # # sheet.write(0, 5, 'Latitude')
        # # sheet.write(0, 6, 'LONGITUDE')

        # count = 1
        # for i in self.placesList:
        #     for keys, data in i.items():
        #         sheet.write(count, 0, data['Category'])
        #         sheet.write(count, 1, data['Title'])
        #         sheet.write(count, 2, data['Description'])
        #         sheet.write(count, 3, data['Rating'])
        #         sheet.write(count, 4, data['Address'])
        #         sheet.write(count, 5, data['Hours'])
        #         sheet.write(count, 6, data['Website'])
        #         sheet.write(count, 7, data['Phone'])
        #         # sheet.write(count, 5, location.latitude)
        #         # sheet.write(count, 6, location.longitude)
        #         count += 1

        # writeBook.save(self.path+self.fileName)
