import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from config import file_path


def load_data() -> pd.DataFrame:
    """
    Load Gaia data.

    Returns:
        data: DataFrame containing Gaia data
    """
    data = pd.read_csv(file_path)
    return data


def subset_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Subset Gaia data so it only includes data relevant for plotting.

    Arguments:
        data: DataFrame containing Gaia data

    Returns:
        subsetted_data: subsetted DataFrame containing Gaia data
    """

    subsetted_data = data.dropna()
    subsetted_data = subsetted_data.loc[
        (subsetted_data["parallax_over_error"] > 20)
        & (subsetted_data["phot_g_mean_flux_over_error"] > 20)
        & (subsetted_data["phot_bp_mean_flux_over_error"] > 20)
        & (subsetted_data["phot_rp_mean_flux_over_error"] > 20)
    ]

    return subsetted_data


def convert_to_absolute_magnitude(
    apparent_magnitude: pd.Series, parallax: pd.Series
) -> pd.Series:
    """
    Convert apparent magnitude to absolute magnitude.

    Arguments:
        apparent_magnitude: pandas Series containing apparent magnitudes
        parallax: pandas Series containing parallax values

    Returns:
        absolute_magnitude: pandas Series containing absolute magnitudes
    """
    absolute_magnitude = apparent_magnitude - (5 * np.log10((1000 / parallax))) + 5

    return absolute_magnitude


def plot_color_magnitude():
    """
    Create color magnitude plot using Gaia data.
    """
    gaia_data = load_data()
    gaia_data = subset_data(gaia_data)

    absolute_magnitude = convert_to_absolute_magnitude(
        gaia_data["phot_g_mean_mag"], gaia_data["parallax"]
    )

    plt.scatter(gaia_data["bp_rp"], absolute_magnitude, s=0.01)
    plt.xlabel("Bp-Rp")
    plt.ylabel("Absolute Magnitude")
    plt.gca().invert_yaxis()
    plt.title("Color-Magnitude Diagram")
    plt.show()


# how to run run script:
plot_color_magnitude()
