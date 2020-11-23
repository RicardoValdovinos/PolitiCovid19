from datetime import datetime

import matplotlib.patches as mpatches
import pandas as pd


def generate_handles(colors, labels):
    if len(colors) != len(labels):
        raise ValueError(f'Colors list has different length than labels list! {len(colors)} != {len(labels)}')
    handles_list = []
    for c, l in zip(colors, labels):
        handles_list.append(mpatches.Patch(color=c, label=l))
    return handles_list


def display_line_plot(df_dict, color_map, title, x_label, y_label):
    date_list = pd.date_range(start=datetime(2020, 1, 23), end=datetime.today(), periods=200).tolist()
    line_plot_df = pd.DataFrame(df_dict, index=date_list)
    line_plot = line_plot_df.plot.line(figsize=(15, 10), cmap=color_map)
    line_plot.set_title(title)
    line_plot.set_xlabel(x_label)
    line_plot.set_ylabel(y_label)
    return line_plot


def display_bar_plot(bar_plot_column, colors, x_tick_labels, title, x_label, y_label, handles):
    bar_plot = bar_plot_column.plot(
        figsize=(15, 10),
        kind='bar',
        color=colors
    )
    bar_plot.set_xticklabels(x_tick_labels)
    bar_plot.set_title(title)
    bar_plot.set_xlabel(x_label)
    bar_plot.set_ylabel(y_label)
    bar_plot.legend(handles=handles, loc=2)
    return bar_plot


def display_pie_plot(segment_values, segment_indices, y, title, colors):
    df = pd.DataFrame({y: segment_values},
                      index=segment_indices)
    pie_plot = df.plot.pie(y=y, figsize=(15, 10), colors=colors)
    pie_plot.set_title(title)
    return pie_plot
