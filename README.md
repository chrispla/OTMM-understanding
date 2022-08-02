# Analysis of melody in Ottoman Turkish Makam Music

##### R.Oğuz Araz - Christos Plachouras

Course project for **Audio and Music Processing Lab** - Sound and Music Computing Master's 2021-2022, Universitat Pompeu Fabra

### Motivation

The Ottoman-Turkish Makam Music (OTMM) tradition has been practiced, developed, and passed on between generations for many centuries. Still, there are many aspects of it that are not well understood to non-practitioners. One of those is the concept of *Makam*, which is often mistakenly used interchangeably with *scale*. Ottoman-Turkish
makam music is also underrepresented in the Music Information Retrieval field, which is dominated by research and tools built to deal with 12-tone equal-tempered eurogenic music.
In this project, we employ statistical methods to analyze Ottoman-Turkish Makam Music scores. We draw inspiration from musicological approaches to design processes
for extracting various statistics for each makam, centered around their differences in note and interval occurrence and development. We show how some of our results might suggest how some of the melodic conventions of makams might manifest in the scores. Our work makes a small contribution to the quest of understanding makam music by suggesting pathways for further research in this music tradition.

### Methods

We conduct our experiments on the [**SymbTr** Turkish Makam Music Symbolic Data Collection](https://github.com/sertansenturk/SymbTr), a collection from 2200 pieces from 155 makams and 88 usuls. We extract several statistics related to the pitch classes, melodic progressions, and interval progressions in each song to explore whether there are any melodic conventions across pieces in the same makam.

### Running

We recommend viewers of this repository to start from reading the paper [Statistical Analysis of Melody in Turkish Makam Music](https://github.com/chrispla/OTMM-understanding/blob/main/Statistical%20Analysis%20of%20Melody%20in%20Turkish%20Makam%20Music.pdf) in the repository and then investigate the details of the experiments on the [makam_exploration](https://github.com/chrispla/OTMM-understanding/blob/main/makam_exploration.ipynb) notebook.

To ensure everything runs as intended, it is recommended that the code is run in a [venv](https://docs.python.org/3/library/venv.html) or a [conda env](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) with at minimum python 3.7 and the requirements specified in `requirements.txt`. Alternatively, the project is light on external dependencies so if your environment has `numpy`, `scipy`, and `matplotlib` it will likely be suitable. 

Before running the experiments, download the [dataset]([https://github.com/sertansenturk/SymbTr/tree/master/MusicXML) of symbolic music in the MusicXML format. 

* The experiments and explanations are present in the `makam_exploration.ipynb` notebook, and can be run linearly there. 

* The `makam_information.py` script contains information such as the tonic and dominant of each makam, the perde (note) names and their 53-TET values, the 53-TET approximations of accidentals, and others. This information is important and ultimately determines the output of the analyses. At the same time, OTMM is not a theory-first tradition, and so some of this information is the result of an after-the-fact attempt at standardization. We've included the sources we used to gather this information, but if you disagree on a particular interpretation then you can edit the information in this script.

* The `makam_parser.py` script contains a parser for the OTMM MusicXML scores that focuses on the extraction and conversion of pitch information and provides some methods useful for extracting information about melodic progressions.

### Disclaimer

This is very much still a work in progress, and hence we can't draw any concrete conclusions from this project yet. However, we still hope the experiments and preliminary results can be useful to someone.