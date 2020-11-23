us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands': 'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    'Republic of Marshall Islands': 'MH',
    'Palau': 'PW',
    'U.S. Minor Outlying Islands': 'UM',
    'Federated States of Micronesia': 'FM',
    'United States of America': 'US',
    'New York City': 'NYC'
}

inverted_dict = dict(map(reversed, us_state_abbrev.items()))


def remove_territories_from_df(df):
    us_territories = ['AS', 'GU', 'MH', 'MP', 'PR', 'PW', 'VI', 'UM', 'DC', 'FM', 'US', 'NYC']
    for territory in us_territories:
        df = df[df['state'] != inverted_dict[territory]]
    return df.sort_values('state')


def state_name_to_state_code(df):
    if len(df.iloc[0]['state']) > 2:
        for i in range(len(df)):
            df.iloc[i]['state'] = us_state_abbrev[df.iloc[i]['state']]
    return df
