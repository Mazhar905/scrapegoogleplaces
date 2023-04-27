# Google Maps Places Scraper 🌎📊

This is script is a scraping script developed with Python and its automation library Selenium. **Consists of reading a list of keywords, searching them in the Google Maps search, and getting its data**.

The script goes one by one searching for the keyword, and storing the data in a list, to finally export it to an Excel file located in the folder specified by the user when running the script.

## How to Run It

To execute this script you need to run it in the command prompt.

    ```bash
    python3 main_data_maps.py
    ```

Then, question will appear, which are necessary to run script:


1. You need to specify where is located the *.txt* file with the keywords to search. For example: *D:\Projects\canada\places.txt*

    ```bash
    [1] Introduce the path of the keywords txt file:
    ```

Then the script starts to work, and when it finished, the Excel file would appear in the output folder.

---

## Requirements

The used requirements are specified in the requierements.txt file. If you want to execute the *.py* script from python, you can install the dependencies with the next command:

```bash
pip install -r requirements.txt
```

<!-- ## Contact

mazhar921345@gmail.com
whatsapp: +923414313217 -->

# scraperGooglePlaces
