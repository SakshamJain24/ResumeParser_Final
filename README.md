
# Resume Parser Pipeline

This Jupyter Notebook provides a full pipeline for parsing resumes and extracting key information such as names, emails, locations, skills, and work experience. The extracted data is then processed and can be used for various applications such as job matching, insights generation, or further analysis.

## Features
- Extracts entities like names, emails, locations, educational qualifications, skills (e.g., HTML, CSS, JS, Python), and work experience.
- Utilizes `spaCy` for natural language processing (NLP) and named entity recognition (NER).
- Processes API data for job recommendations and matches parsed resume data against job descriptions.

## Setup Instructions

1. Clone this repository or download the `.ipynb` file.
2. Install the required dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

3. Download and install the appropriate spaCy model:

    ```bash
    python -m spacy download en_core_web_sm
    ```

4. Run the Jupyter Notebook:

    ```bash
    jupyter notebook ResumeParser_FullPipeline.ipynb
    ```

## Dependencies

The required libraries are listed in the `requirements.txt` file. Install them before running the notebook.

## How to Use

1. Load your dataset in the format of JSON or text files that contain resumes.
2. The notebook processes each resume, extracting relevant details using NLP techniques.
3. The output displays the parsed information, and you can further match it with available job data.

## Acknowledgments

This project uses:
- [spaCy](https://spacy.io/) for Natural Language Processing
- [pandas](https://pandas.pydata.org/) for data manipulation
