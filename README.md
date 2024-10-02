# Setup and preliminary stuff
## Conda
Go to [Conda Website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) and install Anaconda or Miniconda.

## IDEs

- [Spyder](https://www.spyder-ide.org/) (recommended, described below)
- [PyCharm](https://www.jetbrains.com/pycharm/) (recommended, free pro versions for students, Jupyter Notebook support only in pro version) 
- [VSCode](https://code.visualstudio.com/)
- Jupyter in Browser (works, but not recommended)

## Python Environment

### Option 1: From conda file
```bash
conda env create -f environment.yml
```

### Option 2: Creating new conda env from scratch
```bash
conda create --name digital_modeling_and_big_data_lecture python=3.11
```

#### Activate environment
```bash
conda activate digital_modeling_and_big_data_lecture
```

#### Install dependencies
```bash
conda install anaconda::spyder anaconda::pandas anaconda::scikit-learn anaconda::matplotlib
conda install spyder-notebook -c conda-forge
```

## Activate your conda environment from shell
```bash
conda activate digital_modeling_and_big_data_lecture
```

## Test your conda setup
When running from a shell, activate your conda environment as described above, and the try to run `src/00_check_conda_setup.py`: 
```bash
python src/00_check_conda_setup.py
```
When using Spyder or any other IDE, activate the conda environment and open the file in IDE and press the play button.

Then try to open the Jupyter Notebook in either Spyder or a browser as described below and press the play button on the top.

## Jupyter usage in Spyder
[Spyder docs](https://docs.spyder-ide.org/current/plugins/notebook.html)

## Run Jupyter Notebooks in browser 
Activate the conda environment (see above).
```bash
jupyter notebook
```
This should open a browser window. (if not copy the link starting with http://128.0.0.1:8888 or http://localhost:8888 from the output and paste it in your browser.)




