# Java Class Docs Generator

Java Class Docs Generator is a Streamlit application that allows you to upload Java files and generate documentation for the classes within them.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

This project uses the `javalang` library to parse Java code and extract class information, including methods and fields. It then uses the `ollama` library to generate easy-to-understand documentation for the class.

## Installation

To install the required dependencies, run the following command:

```bash
pip install javalang ollama streamlit


Usage
To run the application, execute the following command:
streamlit run app.py

Upload a Java file using the file uploader.
Click the "Generate Documentation" button.
The generated documentation will be displayed in the text area.