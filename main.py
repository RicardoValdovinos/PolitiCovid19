import pandas as pd


def main():
    covid_df = pd.read_csv('datasets/all-states-history.csv')
    political_df = pd.read_csv('datasets/president_county_candidate.csv')
    # print(covid_df)
    print(filtered_covid(covid_df))


def filtered_covid(covid_df):
    filtered_result = covid_df['2020-11-18':'2020-11-19']
    return filtered_result


if __name__ == '__main__':
    main()
