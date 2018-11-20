import pyutils.csv

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# TODO: Move this to lib?
def plot_correlation(
    x_data,
    y_data,
    x_label='',
    y_label='',
    fig_title=''
):
    # TODO: Read column names from spec
    fig = plt.figure(fig_title, figsize=(15, 10))

    ax11 = fig.add_subplot(1, 2, 1)
    ax11.set_xlabel(x_label)
    ax11.set_ylabel(y_label)
    ax11.scatter(x_data, y_data)

    ax12 = fig.add_subplot(1, 2, 2)
    ax12.hist2d(x_data, y_data, bins=100)
    ax12.set_xlabel(x_label)
    ax12.set_ylabel(y_label)

    plt.show()


def plot_histogram_1d(
    data,
    x_label='',
    fig_title='',
    bin_count=10,
    bin_min='auto',
    bin_max='auto'
):
    fig = plt.figure(fig_title, figsize=(10, 7))

    # Compute bins
    if bin_min is 'auto':
        bin_min = min(data)
    if bin_max is 'auto':
        bin_max = max(data)
    bins = np.linspace(bin_min, bin_max, bin_count)

    # TODO: Think about what API to allow multiple histograms in one figure
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel(x_label)
    ax.set_ylabel('Count')
    # TODO: Set suptitle
    # TODO: Think about how to set bins
    ax.hist(
        data,
        bins=bins)

    plt.show()


# TODO: Move this to lib
# TODO: Rename this to 'data_frame_set_max'
def data_frame_set_max(
    data_frame,
    column_name,
    value
):
    data_frame = data_frame.dropna()
    return data_frame[data_frame[column_name] < value]


def analyze_pancakes_covariances():
    # TODO: Make a plotting spec file (as key value)
    # TODO: Make the spec file use relative paths
    data_source_path = 'C:/data/temp/kpis_covariance_ios_monte_carlo/individual_metrics_per_spatial_anchor.csv'

    # Read data
    data_frame = pd.read_csv(data_source_path)

    # Setup data
    # Setup x
    x_column_name = 'TranslationErrorMeters'

    # Setup y
    # TODO: Support custom columns
    custom_column = pd.Series(
        data_frame['sk_dev_translation'] + data_frame['pk_dev_translation'],
        index=data_frame.index)
    y_column_name = 'dev_translation'
    data_frame[y_column_name] = custom_column

    # Filter
    # data_frame = data_frame[data_frame[x_column_name] < 0.3]
    data_frame = data_frame_set_max(
        data_frame,
        y_column_name,
        0.1
    )

    # Plot
    x_data = data_frame[x_column_name]
    x_label = 'Translation Error (m)'
    y_data = data_frame[y_column_name]
    y_label = 'Translation Deviation'
    fig_title = 'Translation Standard Deviation vs Translation Error'

    plot_correlation(
        x_data,
        y_data,
        x_label,
        y_label,
        fig_title
    )


def analyze_synthetic_covariances():
    # TODO: Make a plotting spec file (as key value)
    # TODO: Make the spec file use relative paths
    data_source_path = 'C:/data/temp/kpis_covariance_sx_monte_carlo/individual_metrics.csv'

    # Read data
    data_frame = pd.read_csv(data_source_path)
    data_frame = data_frame.dropna()

    # Setup data
    # Setup x
    x_column_name = 'HologramOffset (m)'

    # Setup y
    y_column_name = 'TranslationDeviation'

    # Filter
    data_frame = data_frame_set_max(
        data_frame,
        x_column_name,
        0.01
    )
    data_frame = data_frame_set_max(
        data_frame,
        y_column_name,
        0.02
    )

    # Plot
    x_data = data_frame[x_column_name]
    x_label = 'Translation Error (m)'
    y_data = data_frame[y_column_name]
    y_label = 'Translation Deviation'
    fig_title = 'Translation Standard Deviation vs Translation Error'

    plot_correlation(
        x_data,
        y_data,
        x_label,
        y_label,
        fig_title
    )


def analyze_pancakes_pose_distribution():
    '''
    Histogram the poses
    '''
    # TODO: Make a plotting spec file (as key value)
    # TODO: Make the spec file use relative paths
    data_source_path = 'C:/data/temp/kpis_covariance_ios_pose_distribution/monte_carlo_poses_3.csv'

    # Read data
    data_frame = pd.read_csv(data_source_path)
    data_frame = data_frame.dropna()

    # Setup data
    # Setup x
    data_column_name = 'tx'

    # Filter
    # data_frame = data_frame_set_max(
    #     data_frame,
    #     data_column_name,
    #     0.01
    # )

    # Plot
    data = data_frame[data_column_name]
    data_label = 'tx (meters)'
    fig_title = 'Distribution of sim3'

    plot_histogram_1d(
        data=data,
        x_label=data_label,
        fig_title=fig_title,
        bin_count=30
    )


def analyze_synthetic_pose_distribution():
    '''
    Histogram the poses
    '''
    # TODO: Make a plotting spec file (as key value)
    # TODO: Make the spec file use relative paths
    data_source_path = 'C:/data/temp/kpis_covariance_sx_pose_distribution/monte_carlo_poses_40.csv'

    # Read data
    data_frame = pd.read_csv(data_source_path)
    data_frame = data_frame.dropna()

    # Setup data
    # Setup x
    data_column_name = 'tx'

    # Filter
    # data_frame = data_frame_set_max(
    #     data_frame,
    #     data_column_name,
    #     0.01
    # )

    # Plot
    data = data_frame[data_column_name]
    data_label = 'X'
    fig_title = 'Distribution of sim3'

    plot_histogram_1d(
        data,
        data_label,
        fig_title
    )
        

if __name__ == '__main__':
    # analyze_pancakes_covariances()
    # analyze_synthetic_covariances()
    analyze_pancakes_pose_distribution()
    # analyze_synthetic_pose_distribution()