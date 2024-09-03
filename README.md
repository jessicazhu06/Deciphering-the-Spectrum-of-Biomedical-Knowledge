# Deciphering the Spectrum of Biomedical Knowledge through PubMed Data Mining - Additional Materials

This repository contains additional materials for the extended research project submitted to the University of Manchester for the degree of MSc Data Science in the Faculty of Humanities.

Student ID: 11338635

## Project Overview

This project develops a comprehensive pipeline for analysing drug-target interactions through text mining of PubMed data. It integrates advanced text mining techniques with network analysis to identify novel drug targets and investigate polypharmacological interactions.

## Repository Structure

- `code/`: Folder containing all project scripts
  - `1_data_collection.ipynb`: Notebook for collecting PubMed data
  - `2_data_preparation.ipynb`: Notebook for data preparation
  - `3_fine_tune_bio_bert.ipynb`: Notebook for fine-tuning BioBERT model
  - `4_data_preprocessing_cleaning_NER_and_RE.ipynb`: Notebook for data preprocessing, cleaning, NER, and RE
  - `5_exploratory_data_analysis.ipynb`: Notebook for exploratory data analysis
  - `6_novel_targets_identification_and_polypharmacology_analysis_(network_construction).ipynb`: Notebook for network analysis
  - `7_validation.ipynb`: Notebook for validation
- `DrugProt_dataset/`: Folder containing the DrugProt training dataset
- `validation_dataset/`: Folder containing the validation dataset
- `requirements.txt`: List of required Python packages
- `Additional Materials.pdf`: Detailed guide for reproducing the research

## Data Sources

- PubMed: https://pubmed.ncbi.nlm.nih.gov/download/
- DrugProt Training Dataset: https://zenodo.org/records/5042151#.YNwojm7tbzA

The DrugProt training dataset is included in the `DrugProt_dataset/` folder.
The validation dataset can be found in the `validation_dataset/` folder.

## Getting Started

1. Clone this repository
2. Install required packages: `pip install -r requirements.txt`
3. Follow the steps outlined in the Additional Materials document

## Computational Requirements

- Python 3.7+
- NVIDIA GPU with at least 8GB of VRAM
- CUDA-enabled GPU (CUDA 10.1 or higher)

For a complete list of requirements, see the `requirements.txt` file.

## Running the Code

The code in this project was developed and tested in a Google Colab environment. On a local machine, you'll need to adjust these paths to match your local directory structure.

To run the code:
1. Start with `1_data_collection.ipynb` and proceed through the numbered scripts in order.
2. For Jupyter notebooks, open them in your preferred environment (local Jupyter, Google Colab, etc.) and run the cells in order.
