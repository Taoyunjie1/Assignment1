import pandas as pd


def clean(input_file1,input_file2):
    df1= pd.read_csv(input_file1)
    df2=pd.read_csv(input_file2)
    df=pd.merge(df1,df2,left_on='respondent_id',right_on="id",how="left")
    df = df.dropna()
    df = df[df["job"].str.contains("insurance|Insurance") == False]
    df = df.drop(["id"], axis=1)
    return df


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='The path to the respondent_contact.csv file')
    parser.add_argument('other_info_file', help='The path to the respondent_other.csv file')
    parser.add_argument('output_file', help='The path to the output file')
    args = parser.parse_args()

    cleaned = clean(args.respondent_contact.csv,args.respondent_other.csv)
    cleaned.to_csv(args.respondent_cleaned.csv, index=False)
