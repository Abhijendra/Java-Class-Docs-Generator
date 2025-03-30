# Java Class Docs Generator

Java Class Docs Generator is a Streamlit application that allows you to upload Java files and generate documentation for the classes within them.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Description

This project uses the `javalang` library to parse Java code and extract class information, including methods and fields. It then uses the `ollama` library to generate easy-to-understand documentation for the class.

## Installation

To install the required dependencies, run the following command:

```bash
pip install javalang ollama streamlit
```

## Usage
To run the application, execute the following command:
```bash
streamlit run app.py
```
1. Upload a Java file using the file uploader.
2. Click the "Generate Documentation" button.
3. The generated documentation will be displayed in the text area.

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.