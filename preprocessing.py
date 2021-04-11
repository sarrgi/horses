import pandas as pd
from sklearn import preprocessing

def remove_columns(dataframe):
    """
    Remove useless columns.
    """
    df = dataframe

    df = df.drop("RaceGroup", axis = 1)
    df = df.drop("MinWeight", axis = 1)
    df = df.drop("Traditionalmargin", axis = 1)
    df = df.drop("WeightDifference", axis = 1)
    df = df.drop("MeetingID", axis = 1)
    df = df.drop("Date", axis = 1)
    df = df.drop("JetBet", axis = 1)
    df = df.drop("MeetingType", axis = 1)
    df = df.drop("Club", axis = 1)
    df = df.drop("MeetingName", axis = 1)
    df = df.drop("RaceNumber", axis = 1)
    df = df.drop("RaceType", axis = 1)
    df = df.drop("Class", axis = 1)
    df = df.drop("ClassAge", axis = 1)
    df = df.drop("HorseID", axis = 1)
    df = df.drop("Barrier", axis = 1)
    df = df.drop("ToteNumber", axis = 1)
    df = df.drop("Stake", axis = 1)
    df = df.drop("Stake.1", axis = 1)
    df = df.drop("GearWorn", axis = 1)
    df = df.drop("RaceName", axis = 1)
    df = df.drop("Sire", axis = 1)
    df = df.drop("Dam", axis = 1)
    df = df.drop("HorseName", axis = 1)
    df = df.drop("Trainer", axis = 1)
    df = df.drop("JockeyName", axis = 1)

    df = df.drop("Actualtime", axis = 1)
    df = df.drop("Time", axis = 1)
    df = df.drop("Last600mTime", axis = 1)
    df = df.drop("RaceID",  axis = 1)
    df = df.drop("Rail",  axis = 1)
    df = df.drop("Decimalmargin",  axis = 1)
    df = df.drop("StartingPricePlace",  axis = 1)
    df = df.drop("TrackWeather",  axis = 1)
    df = df.drop("RaceClass",  axis = 1)

    return df



def read_all(start_ind, amount):
    """
    Read in data from multiple csv's at once.
    """
    dfs = []
    for f in range(1, amount):

        if start_ind == 49642: continue #bugged file

        # read in
        file_name = "".join(("data/", str(start_ind), ".csv"))
        df = pd.read_csv(file_name, index_col=False)
        dfs.append(df)
        # incr
        start_ind += 1

    df = pd.concat(dfs)
    return df



def fix_index(dataframe):
    """
    Fix for having to load in the indexs for each file at a time.
    """
    df = dataframe

    df = df.reset_index()
    df = df.drop('index', axis = 1)

    return df




def win_loss_conversion(dataframe):
    """
    Convert Finishingposition variable to a winloss category where:
        - 0 = Not the Winner
        - 1 = Winner
    """
    df = dataframe

    for i in range(len(df.index)):
        if df.loc[i, 'Finishingposition'] == 1:
            df.loc[i, 'Finishingposition'] = 1
        else:
            df.loc[i, 'Finishingposition'] = 0

    return df



def convert_strings(dataframe):
    df = dataframe
    columns = ["Track", "DayType", "TrackCondition", "NoAllowances", "ClassGender", "ClassWeight", "RaceTrackCondition", "RaceWeather", "Gender", "TrainerLocation"]

    le = preprocessing.LabelEncoder()
    for column_name in columns:
        if df[column_name].dtype == object:
            df[column_name] = le.fit_transform(df[column_name])
        else:
            pass

    return df


def convert_missing_to_string(dataframe, column):
    """
    Convert a missing value in a categorical field to "Unknown".
    This ensures all values in thge field are the same type.
    """
    df = dataframe

    for i in range(len(df.index)):
        if type(df.loc[i, column]) == float or type(df.loc[i, column]) == int:
            df.loc[i, column] = "Unknown"

    return df



if __name__ == "__main__":
    df = read_all(49601, 99)

    df = remove_columns(df)
    df = fix_index(df)
    df = win_loss_conversion(df)
    df = convert_missing_to_string(df, "TrainerLocation")
    df = convert_strings(df)

    # remove nan prices (useless values)
    df = df.dropna(subset = ["StartingPriceWin"])

    df.to_csv('pre_processed.csv', encoding='utf-8', index_label = "UniqueID")

    print(df)
