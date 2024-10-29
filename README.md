![Architecture](https://github.com/FaisalxWattoo/Restaurant-Name-Generator-Web-Application-Using-Langchain/blob/main/streamlit_resaturant_name_generator.png)
... 
# Restaurant Name Generator Web Application Using Langchain & OPENAI_API_KEY
====================================================

## Overview
This application is a Streamlit web app that generates restaurant names and menu items based on selected cuisines using the LangChain library, which interfaces with OpenAI's models. The application allows users to choose a cuisine type and generates both a restaurant name and suggested menu items for that cuisine.
## Setup Instructions
---------------

### Obtain an API Key
Register with OpenAI to obtain an API key necessary for querying their models. This API key will be used by LangChain to generate responses.

### Configure Environment Variable
```plaintext
Create or update `.env` file in the project directory with:
OPENAI_API_KEY=<your-openai-api-key>
```

### Install Required Libraries
Ensure your environment is prepared by installing the necessary dependencies:
```bash
pip install -r requirements.txt
```

### Run the App
Activate the Streamlit application using:
```bash
streamlit run app.py
```
