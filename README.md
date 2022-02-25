# BISICLES Stats Analysis

Functions which relate to the BISICLES stats file tool. 

#### Required libraries:

* joblib
* multiprocessing
* pandas
* subprocess
* matplotlib

### `amrstats_functions.py`

Functions which run the stats file tool and output a pandas dataframe, can be run both with or without a mask file. 

### `LRF_functions.py`

Functions that use the output from `amrstats_functions.py` and creates additional columns calculating the Linear Response functions from [Levermann et al. (2020)]( https://esd.copernicus.org/articles/11/35/2020/) as well as a 10-year running mean. 
