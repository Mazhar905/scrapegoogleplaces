# -*- coding: utf-8 -*-

import xlwt


class ExportDataMaps:

    def __init__(self, fileName, path, placesList):
        self.fileName = fileName
        self.path = path
        self.placesList = placesList

    def exportExcel(self):
        writeBook = xlwt.Workbook(encoding='utf-8')
        sheet = writeBook.add_sheet("document", cell_overwrite_ok=True)
        style = xlwt.XFStyle()
        sheet.write(0, 0, 'CATEGORY')
        sheet.write(0, 1, 'TITLE')
        sheet.write(0, 2, 'DESCRIPTION')
        sheet.write(0, 3, 'RATING')
        sheet.write(0, 4, 'ADDRESS')
        sheet.write(0, 5, 'OPENING/CLOSING HOURS')
        sheet.write(0, 6, 'WEBSITE')
        sheet.write(0, 7, 'PHONE')
        # sheet.write(0, 5, 'Latitude')
        # sheet.write(0, 6, 'LONGITUDE')

        # Category	Title	Description	Address	Lat	Long	Phone	Website	Opening Hours	Closing Hours	Rating
        count = 1
        for i in self.placesList:
            for keys, data in i.items():
                # for i, values in data.items():
                sheet.write(count, 0, data['Category'])
                sheet.write(count, 1, data['Title'])
                sheet.write(count, 2, data['Description'])
                sheet.write(count, 3, data['Rating'])
                sheet.write(count, 4, data['Address'])
                sheet.write(count, 5, data['Hours'])
                sheet.write(count, 6, data['Website'])
                sheet.write(count, 7, data['Phone'])
                # sheet.write(count, 7, location.phoneNumber)
                # sheet.write(count, 5, location.latitude)
                # sheet.write(count, 6, location.longitude)
                count += 1

        writeBook.save(self.path+self.fileName)
