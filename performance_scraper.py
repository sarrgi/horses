import preprocessing
import requests

# https://loveracing.nz/Breeding/357343/Oraka-Playboy-NZ-2016.aspx#bm-performance-profile

def calc_possible_birthyears(age, date):
    """
    Calculate the potential birth years of the horse based on the meeting date and age of horse.
    """
    year = date[:4]

    calc = int(year) - int(age)
    return calc, calc-1


if __name__ == "__main__":

    # read in files
    df = preprocessing.read_all(49601, 99)
    df = preprocessing.fix_index(df)


    url = "https://loveracing.nz/Common/SystemTemplates/Modal/EntryDetail.aspx?HorseID=357343&DisplayContext=Modal"
    req = requests.get(url)
    print(req.content)

    # for i in range(len(df.index)):
    #     name = df.loc[i, "HorseName"]
    #     age = df.loc[i, "Age"]
    #     date = df.loc[i, "Date"]
    #
    #     y1, y2 = calc_birthyear(age, date)
    #
    #     url = "".join(("https://loveracing.nz/Breeding/357343/", name, "-", str(y1), ".aspx#bm-performance-profile"))
    #
    # print(df)
