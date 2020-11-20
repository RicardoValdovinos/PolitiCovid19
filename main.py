import pandas as pd


def main():
    covid_df = pd.read_csv('datasets/all-states-history.csv')
    political_df = pd.read_csv('datasets/president_county_candidate.csv')

if __name__ == '__main__':
    main()
