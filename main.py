import sys

import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
from matplotlib import cm

import data_shaper
import data_visualizer
import states


def filter_covid_columns(df, columns):
    if not columns:
        raise ValueError(f'columns list was empty')

    if not data_shaper.does_df_contain_column(df, columns):
        raise KeyError(f'one of the columns in {columns} was not found!')

    temp = data_shaper.columns_to_lower(df, columns)
    temp = states.remove_territories_from_df(temp)
    temp = states.state_name_to_state_code(temp)
    return temp


def get_covid_df(columns_dict):
    covid_df = pd.read_csv('datasets/Covid-Data.csv').drop([0, 1])
    covid_df = data_shaper.fix_df_header(covid_df)
    covid_df.rename(columns=columns_dict,
                    inplace=True)
    return covid_df.sort_values('state')


def get_covid_time_data():
    all_states_history_df = pd.read_csv('datasets/all-states-history.csv')
    all_states_history_df = filter_covid_columns(all_states_history_df, ['date', 'state', 'hospitalized'])
    all_states_history_df = all_states_history_df[all_states_history_df['hospitalized'].notna()]
    all_states_history_df = data_shaper.convert_column_to_datetime(all_states_history_df, 'date')
    all_states_history_df = data_shaper.convert_column_to_numeric(all_states_history_df, 'hospitalized')
    return all_states_history_df


def generate_df_list(covid_time_data):
    df_list = []
    for i, k in enumerate(states.us_state_abbrev):
        df_list.append(covid_time_data[covid_time_data['state'] == states.us_state_abbrev[k]].sort_values('date'))
    return df_list


def generate_state_dict(df_list, vote):
    states_dict = {}
    counter = 0
    for temp_df in df_list:
        if not temp_df['state'].empty and len(temp_df['hospitalized'].to_list()) >= 200:
            if temp_df['vote'].iloc[0] == vote:
                states_dict[temp_df['state'].iloc[0]] = temp_df['hospitalized'].to_list()[:200]
                counter += 1
    return states_dict


def generate_political_cmap(vote):
    return cm.get_cmap('winter') if vote == 'dem' else cm.get_cmap('autumn')


def build_politicovid_line_plot(covid_time_data_df, political_df):
    covid_time_data = data_shaper.merge_df(covid_time_data_df, political_df, 'state')
    df_list = generate_df_list(covid_time_data)
    dem_state_dict = generate_state_dict(df_list, 'dem')
    rep_state_dict = generate_state_dict(df_list, 'rep')
    dem_cmap = generate_political_cmap('dem')
    rep_cmap = generate_political_cmap('rep')
    dem_title = 'Number of Individuals From Democratic States Hospitalized From Late January to late November'
    rep_title = 'Number of Individuals From Republican States Hospitalized From Late January to late November'
    x_label = 'State'
    y_label = 'Cases per 100,000'
    return (
        build_line_plot(dem_state_dict, dem_cmap, dem_title, x_label, y_label),
        build_line_plot(rep_state_dict, rep_cmap, rep_title, x_label, y_label)
    )


def show_politicovid_line_plot(covid_time_data_df, political_df):
    build_politicovid_line_plot(covid_time_data_df, political_df)
    plot.show()


def build_line_plot(dem_state_dict, dem_cmap, dem_title, x_label, y_label):
    return data_visualizer.display_line_plot(
        dem_state_dict,
        dem_cmap,
        dem_title,
        x_label,
        y_label
    )


def build_politicovid_bar_plot(covid_df, political_df):
    merged_df = data_shaper.merge_df(covid_df, political_df, 'state')
    merged_df = data_shaper.convert_column_to_numeric(merged_df, 'case rate per 100000')
    colors = (merged_df['vote'] == 'dem').map({True: 'b', False: 'r'})
    labels = ['Democrat', 'Republican']
    handlers = data_visualizer.generate_handles(['b', 'r'], labels)
    x_ticks_label = merged_df.state
    title = 'Case Rate per 100,000 by State'
    x_label = 'State'
    y_label = 'Cases per 100,000'
    return data_visualizer.display_bar_plot(
        merged_df['case rate per 100000'],
        colors,
        x_ticks_label,
        title,
        x_label,
        y_label,
        handlers
    )


def show_politicovid_bar_plot(covid_df, political_df):
    build_politicovid_bar_plot(covid_df, political_df)
    plot.show()


def build_politicovid_pie_plot(covid_df, political_df):
    covid_total_cases_df = data_shaper.merge_df(covid_df, political_df, 'state')
    dem_sum = np.sum(covid_total_cases_df[covid_total_cases_df['vote'] == 'dem']['total cases'])
    rep_sum = np.sum(covid_total_cases_df[covid_total_cases_df['vote'] == 'rep']['total cases'])
    segment_values = [dem_sum, rep_sum]
    segment_indicies = ['Democrat', 'Republican']
    y = 'Total Cases'
    colors = ['b', 'r']
    title = 'Total Cases for Democratic and Republic States'
    return data_visualizer.display_pie_plot(segment_values, segment_indicies, y, title, colors)


def show_politicovid_pie_plot(covid_df, political_df):
    build_politicovid_pie_plot(covid_df, political_df)
    plot.show()


def build_covid_df(column_dict, filter_columns_list):
    covid_case_rate_df = get_covid_df(column_dict)
    covid_case_rate_df = filter_covid_columns(covid_case_rate_df, filter_columns_list)
    return covid_case_rate_df


def main():
    covid_case_rate_df = build_covid_df(
        {'State/Territory': 'state', 'Case Rate per 100000': 'case rate per 100000'},
        ['state', 'case rate per 100000']
    )
    covid_total_cases_df = build_covid_df(
        {'State/Territory': 'state', 'Total Cases': 'total cases'},
        ['state', 'total cases']
    )
    covid_total_cases_df = data_shaper.convert_column_to_numeric(covid_total_cases_df, 'total cases')
    political_df = pd.read_csv('datasets/2020_Election_Results.csv').sort_values('state')
    if len(sys.argv) < 2:
        pdf = matplotlib.backends.backend_pdf.PdfPages("figures.pdf")
        line_plots = build_politicovid_line_plot(get_covid_time_data(), political_df)
        dem_line_figure = line_plots[0].get_figure()
        pdf.savefig(dem_line_figure)
        rep_line_figure = line_plots[1].get_figure()
        pdf.savefig(rep_line_figure)
        bar_figure = build_politicovid_bar_plot(covid_case_rate_df, political_df).get_figure()
        pdf.savefig(bar_figure)
        pie_figure = build_politicovid_pie_plot(covid_total_cases_df, political_df).get_figure()
        pdf.savefig(pie_figure)
        pdf.close()
    else:
        if sys.argv[1] == 'show':
            show_politicovid_line_plot(get_covid_time_data(), political_df)
            show_politicovid_bar_plot(covid_case_rate_df, political_df)
            show_politicovid_pie_plot(covid_total_cases_df, political_df)
        else:
            error_msg = 'Running the program without any arguments will save the plots to a pdf.\n'
            error_msg += 'Passing \'show\', without the quotes, as the first argument will display the plots.'
            print(error_msg, file=sys.stderr)


if __name__ == '__main__':
    main()
