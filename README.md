# Information-Retrieval-System Damasucs_University

## Project Overview

This project involves building a search engine capable of handling two different datasets, representing them according to the Vector Space Model (VSM), performing data retrieval operations, ranking the results, and responding to user queries. The system is designed to work with various datasets, and two datasets will be used for testing purposes:

1. [TREC-TOT 2023 Train](https://ir-datasets.com/trec-tot.html#trec-tot/2023/train)
2. [WikiR En1k Training](https://ir-datasets.com/wikir.html#wikir/en1k/training)

## What Can This System Do?

This IR project allows you to:

- **Search through two different datasets:**\
   You can choose between two pre-loaded datasets or potentially integrate your own in the future.

- **Refine results:**\
  The system preprocesses the data (e.g., stemming, lemmatization) to ensure a more accurate understanding of your search query.

- **Retrieve data quickly and efficiently:**\
  By building indexes for each dataset, the system retrieves relevant documents rapidly.

- **Rank results:**\
  The system ranks the retrieved documents based on their relevance to your query, placing the most pertinent results at the top.

---

## Project Structure

We've tried to make the structure modular, clear, and easy to develop on.

Here is the final structure of the project files:

```bash
├── src
    ├── app
    ├── core
    ├── database
    ├── evaluations
    ├── measures
    ├── offline_req1.py
    ├── offline_req2.py
    ├── pre_processors
    ├── services
    ├── start_app.py
    ├── start_services.py
    └── utils
```

### Structure Breakdown

1. **app**:\
   Contains the core functionality of the project, including:
   - `__init__.py`: Initialization file.
   - `home.py`: Script for handling home page functionality.
   - `results.py`: Script for managing search results.
   - `templates/`: Directory containing HTML templates for the user interface, including:
     - `base.html`: Base template for other HTML files.
     - `home.html`: Template for the home page.
     - `results.html`: Template for displaying search results.
2. **core**:\
   Contains the constants used over the system.

   - `base_urls.py`: Defines base URLs.
   - `datasets.py`: Imports and loads different datasets required for testing and development.
   - `endpoints.py`: Defines endpoint URLs for different functionalities of the system.
   - `ports.py`: Specifies port numbers used in the system.

3. **database**:\
   Manages the database functionalities of the project, structured as follows:

   - `create_db.py`: Creates database tables.
   - `load_docs.py`: Loads documents into the database tables.
   - `store_docs.py`: Stores documents into the database.

4. **measures**:\
    Handles evaluation measures for assessing the performance of the retrieval system.
   - `map.py`: Computes the Mean Average Precision (MAP) measure.
   - `mrr.py`: Computes the Mean Reciprocal Rank (MRR) measure.
   - `precision.py`: Computes precision measures at various cutoff points to evaluate the relevance of retrieved documents.
   - `recall.py`: Computes recall measures to evaluate the comprehensiveness of retrieved documents in relation to relevant documents.
5. **pre_processors**:\
    Manages the preprocessing of datasets before they are stored and indexed.

   - `ds1_prep.py`: Preprocesses the first dataset before storing it in the database.
   - `ds2_prep.py`: Preprocessesthe second dataset before storing it in the database.

6. **services**:\
   Contains various services essential for processing, indexing, querying, matching, and searching through the datasets.

   - `text_processing.py`: Handles text preprocessing, including tokenization, stopword removal, stemming, and lemmatization.
   - `searching.py`: Manages the searching functionality, interacting with the query processing and matching services to retrieve relevant documents.
   - `indexing.py`: Builds indexes for the documents using a combination of TF-IDF vectors and BERT embeddings and clusters them using K-Means clustering.
   - `matching.py`: Matches the processed query with the relevant documents using cosine similarity and clustering.
   - `preprocessing.py`: Preprocesses the datasets and structures them for further use.
   - `query_processing.py`: Processes the query to transform it into a format suitable for matching.

7. **utils**:\
   Contains utility functions for various common tasks.
   - `converting.py`: convert data between different formats.
   - `extracting.py`:extract specific information from data.
   - `loading.py`: load data from various file formats.
   - `storing.py`: store data in various file formats.

## Setup Instructions

To set up and run the project, follow these steps:

1. Clone the repository.

```sh
git clone https://github.com/aseel776/ir-project.git
```

2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Donwload the two datasets:

- [TREC-TOT 2023 Train](https://ir-datasets.com/trec-tot.html#trec-tot/2023/train)
- [WikiR En1k Training](https://ir-datasets.com/wikir.html#wikir/en1k/training).

4. Run the services:

```sh
py src/start_services.py
```

5. Run the app :

```sh
py src/start_app.py
```
