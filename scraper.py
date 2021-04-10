import requests

if __name__ == "__main__":

    race_id = 49600#49663

    for i in range(0, 99):
        # increment race_id
        race_id += 1
        # scrape url
        # "https://loveracing.nz/SystemTemplates/RaceInfo/ResultDownloads.ashx?DayID=49663&FileName=Race_49663.csv"
        csv_url = "".join(("https://loveracing.nz/SystemTemplates/RaceInfo/ResultDownloads.ashx?DayID=", str(race_id), "&FileName=Race_", str(race_id), ".csv"))
        req = requests.get(csv_url)
        url_content = req.content

        # remove header
        to_remove = "<-- Copyright Notice: (c) 2020 New Zealand Thoroughbred Racing. -->\r\n\r\n"
        url_content = url_content[len(to_remove):]

        # save url to local file
        file_name = "".join((str(race_id), ".csv"))
        csv_file = open(file_name, 'wb')
        csv_file.write(url_content)
        csv_file.close()
