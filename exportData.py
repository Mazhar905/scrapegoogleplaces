# -*- coding: utf-8 -*-

import xlwt
import csv

# data = {'Cruise Toronto': {'title': 'Cruise Toronto', 'Place ID': None, 'rating': '3.8', 'address': '249 Queens Quay W #111, Toronto, ON M5J 2N5, Canada', 'website': 'cruisetoronto.com', 'phone': 'cruisetoronto.com', 'url': 'https://www.google.com/maps/place/Cruise+Toronto/@43.6386424,-79.5300378,12z/data=!4m9!1m2!2m1!1sLandmarks+in+Toronto+on+canada!3m5!1s0x882b352a18ab8c27:0xa2f2389b54b21a54!8m2!3d43.6386424!4d-79.3858422!16s%2Fg%2F12jshvxsx', 'latitide': 43.6386424, 'longitude': -79.5300378}, 'Little Canada': {'title': 'Little Canada', 'Place ID': 'ChIJjy6Dvx41K4gR-EnZ_CNE1_E', 'rating': '4.9', 'address': '10 Dundas St E Basement2, Toronto, ON M5B 2G9, Canada', 'website': 'little-canada.ca', 'phone': 'little-canada.ca', 'url': 'https://www.google.com/maps/place/Little+Canada/@43.6386424,-79.5300378,12z/data=!3m1!5s0x882b34c51bbe1e97:0x6a8c2ebac3a9ebf8!4m9!1m2!2m1!1sLandmarks+in+Toronto+on+canada!3m5!1s0x882b351ebf832e8f:0xf1d74423fcd949f8!8m2!3d43.6567116!4d-79.3808532!16s%2Fg%2F11lgsnmkp2', 'latitide': 43.6386424, 'longitude': -79.5300378}, 'Toronto Old City Hall': {'title': 'Toronto Old City Hall', 'Place ID': 'ChIJ81rnZsw0K4gRHt0-k9sXvwA', 'rating': '4.5', 'address': '60 Queen St W, Toronto, ON M5H 2M3, Canada', 'website': None, 'phone': None, 'url': 'https://www.google.com/maps/place/Toronto+Old+City+Hall/@43.6386424,-79.5300378,12z/data=!4m10!1m2!2m1!1sLandmarks+in+Toronto+on+canada!3m6!1s0x882b34cc66e75af3:0xbf17db933edd1e!8m2!3d43.6525198!4d-79.3817156!15sCh5MYW5kbWFya3MgaW4gVG9yb250byBvbiBjYW5hZGFaICIebGFuZG1hcmtzIGluIHRvcm9udG8gb24gY2FuYWRhkgETaGlzdG9yaWNhbF9sYW5kbWFya5oBJENoZERTVWhOTUc5blMwVkpRMEZuU1VORGNXSlBTM0ZCUlJBQuABAA!16zL20vMDQ5Njhr', 'latitide': 43.6386424, 'longitude': -79.5300378}, 'Clock tower': {'title': 'Clock tower', 'Place ID': 'ChIJRRQkNjjL1IkRZlOJfSQC4LQ', 'rating': '4.9', 'address': '9 Trinity St Suite 200, Toronto, ON M5A 3C4, Canada', 'website': None, 'phone': None, 'url': 'https://www.google.com/maps/place/Clock+tower/@43.6386424,-79.5300378,12z/data=!4m10!1m2!2m1!1sLandmarks+in+Toronto+on+canada!3m6!1s0x89d4cb3836241445:0xb4e002247d895366!8m2!3d43.6499639!4d-79.3595384!15sCh5MYW5kbWFya3MgaW4gVG9yb250byBvbiBjYW5hZGGSARNoaXN0b3JpY2FsX2xhbmRtYXJr4AEA!16s%2Fg%2F11fhqncsw4', 'latitide': 43.6386424, 'longitude': -79.5300378}, 'Rat Alley': {'title': 'Rat Alley', 'Place ID': 'ChIJRTOhPcQ1K4gRdDwM3JS5qP4', 'rating': '4.8', 'address': '807 A Bathurst St, Toronto, ON M5R 3G2, Canada', 'website': None, 'phone': None, 'url': 'https://www.google.com/maps/place/Rat+Alley/@43.6654984,-79.5554777,12z/data=!4m10!1m2!2m1!1sLandmarks+in+Toronto+on+canada!3m6!1s0x882b35c43da13345:0xfea8b994dc0c3c74!8m2!3d43.6654984!4d-79.4112821!15sCh5MYW5kbWFya3MgaW4gVG9yb250byBvbiBjYW5hZGGSARNoaXN0b3JpY2FsX2xhbmRtYXJr4AEA!16s%2Fg%2F11j8h9xrcq', 'latitide': 43.6654984, 'longitude': -79.5554777}, 'Canadian Provinces Flags Alley': {'title': 'Canadian Provinces Flags Alley', 'Place ID': 'ChIJv_9FDWY1K4gR9QtfVy4DRPk', 'rating': '5.0', 'address': 'Bay St., Toronto, ON M5H 2N1, Canada', 'website': None, 'phone': None, 'url': 'https://www.google.com/maps/place/Canadian+Provinces+Flags+Alley/@43.6654984,-79.5554777,12z/data=!4m10!1m2!2m1!1sLandmarks+in+Toronto+on+canada!3m6!1s0x882b35660d45ffbf:0xf944032e575f0bf5!8m2!3d43.65294!4d-79.3828069!15sCh5MYW5kbWFya3MgaW4gVG9yb250byBvbiBjYW5hZGGSARNoaXN0b3JpY2FsX2xhbmRtYXJr4AEA!16s%2Fg%2F11j4q8dfd9', 'latitide': 43.6654984, 'longitude': -79.5554777}, 'Owl statue': {'title': 'Owl statue', 'Place ID': 'ChIJG2aebH3N1IkRt5RK1t8YnCg', 'rating': None, 'address': 'Toronto, ON M4L 1J1, Canada', 'website': 'torontopubliclibrary.ca', 'phone': 'torontopubliclibrary.ca', 'url': 'https://www.google.com/maps/place/Owl+statue/@43.6702607,-79.3660949,13z/data=!4m10!1m2!2m1!1sLandmarks+in+Toronto+on+canada!3m6!1s0x89d4cd7d6c9e661b:0x289c18dfd64a94b7!8m2!3d43.6702607!4d-79.298554!15sCh5MYW5kbWFya3MgaW4gVG9yb250byBvbiBjYW5hZGGSARNoaXN0b3JpY2FsX2xhbmRtYXJr4AEA!16s%2Fg%2F11gxmccwh9', 'latitide': 43.6702607, 'longitude': -79.3660949}, 'Lime Ridge Monument': {'title': 'Lime Ridge Monument', 'Place ID': 'ChIJFWdWt7k0K4gRyACiG0qcC_o', 'rating': '4.4', 'address': 'Toronto, ON M5S 3K3, Canada', 'website': 'veterans.gc.ca', 'phone': 'veterans.gc.ca', 'url': 'https://www.google.com/maps/place/Lime+Ridge+Monument/@43.662622,-79.4654025,13z/data=!4m10!1m2!2m1!1sLandmarks+in+Toronto+on+canada!3m6!1s0x882b34b9b7566715:0xfa0b9c4a1ba200c8!8m2!3d43.662622!4d-79.3933047!15sCh5MYW5kbWFya3MgaW4gVG9yb250byBvbiBjYW5hZGGSARNoaXN0b3JpY2FsX2xhbmRtYXJr4AEA!16s%2Fg%2F1hhkbxjc1', 'latitide': 43.662622, 'longitude': -79.4654025}, 'Governors Monument': {'title': 'Governors Monument', 'Place ID': 'ChIJceXMMLvM1IkRxQShvOAEIsg', 'rating': '4.7', 'address': 'Toronto, ON M4W 3X8, Canada', 'website': None, 'phone': None, 'url': 'https://www.google.com/maps/place/Governors+Monument/@43.6858053,-79.4370795,13z/data=!4m10!1m2!2m1!1sLandmarks+in+Toronto+on+canada!3m6!1s0x89d4ccbb30cce571:0xc82204e0bca104c5!8m2!3d43.6858053!4d-79.3649817!15sCh5MYW5kbWFya3MgaW4gVG9yb250byBvbiBjYW5hZGGSARNoaXN0b3JpY2FsX2xhbmRtYXJr4AEA!16s%2Fg%2F11g8p1s5k6', 'latitide': 43.6858053, 'longitude': -79.4370795}, 'CN Tower': {'title': 'CN Tower', 'Place ID': 'ChIJmzrzi9Y0K4gRgXUc3sTY7RU', 'rating': '4.6', 'address': '290 Bremner Blvd, Toronto, ON M5V 3L9, Canada', 'website': 'cntower.ca', 'phone': 'cntower.ca', 'url': 'https://www.google.com/maps/place/CN+Tower/@43.6425662,-79.4591546,13z/data=!3m1!5s0x882b34d819a55ff7:0xad7cf7bcaf4e239b!4m10!1m2!2m1!1sLandmarks+in+Toronto+on+canada!3m6!1s0x882b34d68bf33a9b:0x15edd8c4de1c7581!8m2!3d43.6425662!4d-79.3870568!15sCh5MYW5kbWFya3MgaW4gVG9yb250byBvbiBjYW5hZGFaICIebGFuZG1hcmtzIGluIHRvcm9udG8gb24gY2FuYWRhkgESdG91cmlzdF9hdHRyYWN0aW9umgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVJ6Y25CaFNuVkJSUkFC4AEA!16zL20vMDF0d3M', 'latitide': 43.6425662, 'longitude': -79.4591546}, 'Spadina Museum': {'title': 'Spadina Museum', 'Place ID': 'ChIJkQDc4500K4gReLP2DQUA_Tk', 'rating': '4.6', 'address': '285 Spadina Rd, Toronto, ON M5R 2V5, Canada', 'website': 'toronto.ca', 'phone': 'toronto.ca', 'url': 'https://www.google.com/maps/place/Spadina+Museum/@43.6789935,-79.480245,13z/data=!4m10!1m2!2m1!1sLandmarks+in+Toronto+on+canada!3m6!1s0x882b349de3dc0091:0x39fd00050df6b378!8m2!3d43.6789935!4d-79.4081472!15sCh5MYW5kbWFya3MgaW4gVG9yb250byBvbiBjYW5hZGFaICIebGFuZG1hcmtzIGluIHRvcm9udG8gb24gY2FuYWRhkgEOaGlzdG9yeV9tdXNldW2aASNDaFpEU1VoTk1HOW5TMFZKUTBGblNVUlNlSEY1T1U1bkVBReABAA!16zL20vMDJjZmww', 'latitide': 43.6789935, 'longitude': -79.480245}, 'Memorial - Old City Hall Cenotaph': {'title': 'Memorial - Old City Hall Cenotaph', 'Place ID': 'ChIJK44geI01K4gRTGUjWswOJic', 'rating': '5.0', 'address': '50 Queen St W, Toronto, ON M5H 2Y4, Canada', 'website': None, 'phone': None, 'url': 'https://www.google.com/maps/place/Memorial+-+Old+City+Hall+Cenotaph/@43.6521351,-79.4536266,13z/data=!4m10!1m2!2m1!1sLandmarks+in+Toronto+on+canada!3m6!1s0x882b358d78208e2b:0x27260ecc5a23654c!8m2!3d43.6521351!4d-79.3815288!15sCh5MYW5kbWFya3MgaW4gVG9yb250byBvbiBjYW5hZGGSARNoaXN0b3JpY2FsX2xhbmRtYXJr4AEA!16s%2Fg%2F11gxjyq80x', 'latitide': 43.6521351, 'longitude': -79.4536266}}
class ExportDataMaps:

    def __init__(self, fileName, para, placesList):
        self.fileName = fileName
        self.para = para
        self.placesList = placesList
        self.field_names = ['Title', 'Category', 'Place ID', 'Rating', 'Review Count', 'Address', 'Website', 'Phone', 'Open Hours', 'Latitude', 'Longitude']
        # print(type(self.placesList))
        # print(self.placesList)
        if placesList is not None or placesList == '':
            if self.fileName.endswith(".xlsx"):
                print("File is an Excel file (.xlsx)")
                self.exportExcel()
            elif self.fileName.endswith(".csv"):
                print("File is a CSV file (.csv)")
                self.exportCSV()
            else:
                print("File format is not recognized.")
        else:
            print("We dont have any data to export")
    def exportCSV(self):
        # Write the data to the CSV file
        with open(self.fileName, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.field_names)
            writer.writeheader()
            for place, details in self.placesList.items():
                writer.writerow({**details})

    def exportExcel(self):
        writeBook = xlwt.Workbook(encoding='utf-8')
        sheet = writeBook.add_sheet("document", cell_overwrite_ok=True)

        # Write header row
        # for i, col_name in enumerate(self.para):
        #      sheet.write(0, i, col_name.upper())

        # # Write data rows from a dictionary
        # # todo: the placesList is a dictionary
        # # dic=         {'St. James Park': {'Category': 'Park', 'Title': 'St. James Park', 'Rating': '4.5', 'Phone': '+1 416-392-2489'}}
        # row = 0
        # for place, attributes in self.placesList.items():
        #     col = 0
        #     for key, value in attributes.items():
        #         sheet.write(row+1, col, value)
        #         col+=1
        #     row += 1

        # writeBook.save(self.fileName)

        # def exportCSV(self):
        #     pass

        # def exportJSON(self):
        #     pass
        #headers
        for i, col_name in enumerate(self.para):
            sheet.write(0, i, col_name.upper())

            # sheet.write(0, 0, 'CATEGORY')
            # sheet.write(0, 1, 'TITLE')
            # sheet.write(0, 2, 'DESCRIPTION')
            # sheet.write(0, 3, 'RATING')
            # sheet.write(0, 4, 'ADDRESS')
            # sheet.write(0, 5, 'OPENING/CLOSING HOURS')
            # sheet.write(0, 6, 'WEBSITE')
            # sheet.write(0, 7, 'PHONE')
            # sheet.write(0, 5, 'Latitude')
            # sheet.write(0, 6, 'LONGITUDE')

            row = 1
            for i in self.placesList:
                for keys, data in i.items():
                    col = 0 
                    for k, value in data.items():
                        sheet.write(row, 0, value)
                        col +=1

                    # sheet.write(count, 5, location.latitude)
                    # sheet.write(count, 6, location.longitude)
                    row +=1 
        writeBook.save(self.fileName)


# ExportDataMaps(fileName='data.csv', para='', placesList=data)