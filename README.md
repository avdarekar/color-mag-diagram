# color-mag-diagram
## Description
This program uses data from the [Gaia archive](https://gea.esac.esa.int/archive/) to create a color-magnitude diagram of stars with a parallax greater than or equal to 10.  

## Table of Contents
* File Descriptions
* Obtaining Data
* Installation 
* Usage
* License

## File Descriptions


## Obtaining Data
Data was obtained from the [Gaia archive](https://gea.esac.esa.int/archive/). This SQL statement was used in the Gaia archive to extract the data:

```
SELECT gaia_source.parallax,gaia_source.parallax_over_error,gaia_source.phot_g_mean_flux_over_error,gaia_source.phot_g_mean_mag,gaia_source.phot_bp_mean_flux_over_error,gaia_source.phot_rp_mean_flux_over_error,gaia_source.bp_rp
FROM gaiadr2.gaia_source 
WHERE (gaiadr2.gaia_source.parallax>=10)
```

The Gaia archive allowed me to download this data as an excel file which I used in my program. 

