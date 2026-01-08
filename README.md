# PDF Converter

A powerful and easy-to-use web application for converting PDF files to various formats and converting other formats to PDF.

## Features

- 🔄 **PDF to Images** - Convert PDF pages to PNG, JPG, and other image formats
- - 📄 **PDF to Text** - Extract text content from PDF documents
  - - 🖼️ **Image to PDF** - Convert images (JPG, PNG, etc.) to PDF format
    - - 🎯 **Simple Interface** - User-friendly web interface for easy conversions
      - - 📦 **Batch Processing** - Convert multiple files efficiently
        - - 💾 **Large File Support** - Handle files up to 50MB
         
          - ## Tech Stack
         
          - - **Backend**: Flask (Python)
            - - **PDF Processing**: PyPDF2, pdf2image
              - - **Image Processing**: Pillow
                - - **Frontend**: HTML, CSS, JavaScript
                 
                  - ## Prerequisites
                 
                  - Before you begin, ensure you have the following installed:
                  - - Python 3.7 or higher
                    - - pip (Python package manager)
                     
                      - ## Installation
                     
                      - 1. **Clone the repository**
                        2.    ```bash
                                 git clone https://github.com/kido205/pdf-converter.git
                                 cd pdf-converter
                                 ```

                              2. **Create a virtual environment** (recommended)
                              3.    ```bash
                                       # On Windows
                                       python -m venv venv
                                       venv\Scripts\activate

                                       # On macOS/Linux
                                       python3 -m venv venv
                                       source venv/bin/activate
                                       ```

                                    3. **Install dependencies**
                                    4.    ```bash
                                             pip install -r requirements.txt
                                             ```

                                          ## Usage

                                      1. **Start the Flask application**
                                      2.    ```bash
                                               python app.py
                                               ```

                                            2. **Open your browser** and navigate to:
                                            3.    ```
                                                     http://localhost:5000
                                                     ```

                                                  3. **Select a conversion type**:
                                                  4.    - Choose the file format you want to convert
                                                        -    - Upload your file
                                                             -    - Click convert and download the result
                                                              
                                                                  - ## API Endpoints
                                                              
                                                                  - ### POST `/convert`
                                                                  - Convert files using the API
                                                              
                                                                  - **Parameters**:
                                                                  - - `file` (file): The file to convert (required)
                                                                    - - `type` (string): The conversion type (required)
                                                                      -   - `pdf_to_image`: Convert PDF to PNG image
                                                                          -   - `pdf_to_text`: Convert PDF to plain text
                                                                              -   - `image_to_pdf`: Convert image to PDF
                                                                               
                                                                                  - **Example**:
                                                                                  - ```bash
                                                                                    curl -X POST http://localhost:5000/convert \
                                                                                      -F "file=@document.pdf" \
                                                                                      -F "type=pdf_to_text"
                                                                                    ```

                                                                                    ## Project Structure

                                                                                    ```
                                                                                    pdf-converter/
                                                                                    ├── app.py                 # Main Flask application
                                                                                    ├── requirements.txt       # Python dependencies
                                                                                    ├── .gitignore            # Git ignore file
                                                                                    ├── README.md             # This file
                                                                                    ├── templates/
                                                                                    │   └── index.html        # Web interface (to be created)
                                                                                    ├── static/
                                                                                    │   ├── css/
                                                                                    │   │   └── style.css     # Styling (to be created)
                                                                                    │   └── js/
                                                                                    │       └── script.js     # Frontend logic (to be created)
                                                                                    └── uploads/              # Temporary file storage
                                                                                    ```

                                                                                    ## Next Steps

                                                                                    1. Create `templates/index.html` - Web interface for file uploads
                                                                                    2. 2. Add `static/css/style.css` - Styling for the interface
                                                                                       3. 3. Add `static/js/script.js` - Frontend file handling logic
                                                                                          4. 4. Deploy to a web server (Heroku, AWS, etc.)
                                                                                            
                                                                                             5. ## Troubleshooting
                                                                                            
                                                                                             6. ### Issue: ImportError for pdf2image
                                                                                             7. **Solution**: Install system dependencies for pdf2image
                                                                                             8. - On macOS: `brew install poppler`
                                                                                                - - On Ubuntu: `sudo apt-get install poppler-utils`
                                                                                                  - - On Windows: Download poppler from https://github.com/oschwartz10612/poppler-windows/releases/
                                                                                                   
                                                                                                    - ### Issue: Large file uploads fail
                                                                                                    - **Solution**: Increase the `MAX_CONTENT_LENGTH` in `app.py` or configure your web server
                                                                                                   
                                                                                                    - ## Contributing
                                                                                                   
                                                                                                    - Contributions are welcome! Please feel free to:
                                                                                                    - - Report bugs by opening issues
                                                                                                      - - Suggest improvements
                                                                                                        - - Submit pull requests
                                                                                                         
                                                                                                          - ## License
                                                                                                         
                                                                                                          - This project is licensed under the MIT License - see the LICENSE file for details.
                                                                                                         
                                                                                                          - ## Support
                                                                                                         
                                                                                                          - If you encounter any issues or have questions, please:
                                                                                                          - 1. Check the troubleshooting section above
                                                                                                            2. 2. Review the project issues on GitHub
                                                                                                               3. 3. Create a new issue with detailed description
                                                                                                                 
                                                                                                                  4. ---
                                                                                                                 
                                                                                                                  5. **Happy converting!** 🚀
