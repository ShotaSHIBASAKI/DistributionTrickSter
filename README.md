# DistributionTrickSter
Data and codes of Shibasaki et al (2024) analyzing the distributions of trickster animals and real animals.
The preprint will be available from EcoevoRxiv.
The manuscript has been accepted by the Royal Society Open Science.

Note that the p-values in the permutation tests may differ from the manuscript, but this does change the conclusion.


## TrickSter_data3.csv
This files contain the GPS data, categories of animals, climate data, correspinding hex grids, 
whether correpsonding real animals exist or not in the grids, and the normalized climate data of each tricksters.
Some data missing the climate data, if, for example,  the GPS points at small islands.
TrickSter_data4.csv corresponds to the data with high resolution of the grid

## Real_annimal_hex_biome.csv
This files summarize the hex grids where atleast one corresponding real animals is observed and average climate data in each grid. 
The first two columns show from which GPS data we obtained the hex grids.

## For_gbif_trickster.csv
This file is used to match common and scientific names of animals. See also Supporting data.xlsx, which is a human-frinedly vesion file.

## Biome_distributions.csv
This file summarize hex grid and their climate data where either real animals (RA) of trickster animals (TS) exist. The category of the animals is also showmn.

## AnalysisNote6.pdf
This file provides the codes and maps that show distributions of real and trickster animals over the world.

## AnalysisNote8.pdf
This file vizualizes the results of permutation tests where we tested whether the trickster animals randomly exist on places that corresponding real animals were observedor trickster animals were clogged. In the manuscript, we cannot provide theses figures due to the regulations of a submitted journal.

# AnalysisNote9R.pdf
This file vizualizes the distributions of trickster and real animals over Whitakker biome.

## Analysis_Python
This jupyter notebook provides python codes that we used in the analysis.

## Analysis_R
This jupyter notebook provides R codes that we used in the analysis.

## Supporting data
Common and scientific names of animals analyzed in the manuscript. 

## high_resoplution_analysis.py high_resoliution _analysis2.py
These two python codes were used to obtain the data and perform analysis with high resolution of grids in h3 package

## addtional analysis_R.ipynb additional_analysis_python,ipynb
These notebook explain the detail of analysis with high resolution of grid in h3 package.
