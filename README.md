# Personal Capital Code Challenge

Code challenge for [Personal Capital](https://www.personalcapital.com/)

## Getting started

### Quick start

This setup assumes that you've set up Anaconda. If not see the [Python Environment](#python-environment) section.

```bash
# Create virtual environment
conda env create -f environment.yml

# Activate environment
source activate pc_trials

# Run script
cd bin/
python main.py

```

### Repo structure

 - `main.py`: Entry point
 - instructions/2017 Java Engineer Challenge.docx: Instructions for code challenge
 - `confs.yaml`: Confs for program

### Python Environment
Python code in this repo utilizes packages that are not part of the common library. To make sure you have all of the 
appropriate packages, please install [Anaconda](https://www.continuum.io/downloads), and install the environment 
described in environment.yml (Instructions [here](http://conda.pydata.org/docs/using/envs.html), under *Use 
environment from file*, and *Change environments (activate/deactivate)*). 

## Tests

This program has unittests, located in `unittests.py`. To run these tests:

```bash
# Create virtual environment
conda env create -f environment.yml

# Activate environment
source activate pc_trials

# Run script
cd bin/
python unittest.py

```

## Confs

This program utilizes a `.yaml` conf file, located at `confs/confs.yaml`

## Contact
Feel free to contact me at 13herger <at> gmail <dot> com
