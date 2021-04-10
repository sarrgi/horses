import pandas as pd


def remove_columns(dataframe):
    df = dataframe
    df = df.drop('Stake', axis=1)
    df = df.drop('Stake.1', axis=1)
    df = df.drop('GearWorn', axis=1)
    df = df.drop('RaceName', axis=1)
    df = df.drop('Sire', axis=1)
    df = df.drop('Dam', axis=1)
    df = df.drop('HorseName', axis=1)
    df = df.drop('Trainer', axis=1)
    df = df.drop('JockeyName', axis=1)

    return df


def read_all(start_ind, amount):
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




if __name__ == "__main__":

    df = read_all(49601, 99)
    print(df)

    # for key in df.keys():
    #     print(key)
    #     print(df[key])
    #     print("---------")

    #
    df = remove_columns(df)
    #
    df.to_csv('for_weka.csv', encoding='utf-8')

    # print(df.keys())
