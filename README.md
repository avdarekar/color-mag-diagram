# color-mag-diagram
## Description
This program uses data from the [Gaia archive](https://gea.esac.esa.int/archive/) to create a color-magnitude diagram of stars with a parallax greater than or equal to 10.  

## Table of Contents
* [File Descriptions] (##filedescriptions)
* Obtaining Data
* Installation 
* Usage
* License

## File Descriptions
* Colormag.py: this is the Python program I wrote to create the color-magnitude diagram
* Colormag_diagram.png: this is a screenshot of the color-magnitude diagram that Colormag.py created

## Obtaining Data
Data was obtained from the [Gaia archive](https://gea.esac.esa.int/archive/). This SQL statement was used in the Gaia archive to extract the data:

```
SELECT gaia_source.phot_g_mean_mag,gaia_source.bp_rp,gaia_source.parallax,gaia_source.parallax_over_error,gaia_source.phot_g_mean_flux_over_error,gaia_source.phot_bp_mean_flux_over_error,gaia_source.phot_rp_mean_flux_over_error
FROM gaiadr2.gaia_source 
WHERE (gaiadr2.gaia_source.parallax>=10)
```

The Gaia archive allowed me to download this data as a csv file.

## Installation 
To successfully run this program on your local computer:
1. Run the SQL statement above in the [Gaia archive](https://gea.esac.esa.int/archive/). 
2. Download the data as a csv file. 
3. Save the csv file as a .xlsx file. 
4. Download the Colormag.py file to your computer.
5. Install xlrd, matplotlib.pyplot, and math python libraries.
6. Replace the location of the .xlsx file with the location of the .xlsx file on your computer. 

## Usage
After installation, run the program. Keep in mind that it will take some time for the program to run due to the large amount of data.

## License



