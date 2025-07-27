# color-mag-diagram
## Description
This program uses data from the [Gaia archive](https://gea.esac.esa.int/archive/) to create a color-magnitude diagram of stars with a parallax greater than or equal to 10.  

## Table of Contents
* File Descriptions
* Obtaining Data
* Installation 
* Usage

## File Descriptions
* colormag.py: this is the Python program I wrote to create the color-magnitude diagram
* colormag_diagram.png: this is a screenshot of the color-magnitude diagram that colormag.py created

## Obtaining Data
Data was obtained from the [Gaia archive](https://gea.esac.esa.int/archive/). This SQL statement was used in the Gaia archive to extract the data:

```
SELECT gaia_source.phot_g_mean_mag,gaia_source.bp_rp,gaia_source.parallax,gaia_source.parallax_over_error,gaia_source.phot_g_mean_flux_over_error,gaia_source.phot_bp_mean_flux_over_error,gaia_source.phot_rp_mean_flux_over_error
FROM gaiadr2.gaia_source 
WHERE (gaiadr2.gaia_source.parallax>=10)
```

The Gaia archive allowed me to download this data as a csv file.

## Installation 
To successfully run this program locally:
1. Run the SQL statement above in the [Gaia archive](https://gea.esac.esa.int/archive/). 
2. Download the data as a csv file. 
3. Clone this repo and install requirements in a virtual environment using the requirements.txt file. 

## Usage
After installation, run the plot_color_magnitude() function in colormag.py.


