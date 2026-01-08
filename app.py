from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
import PyPDF2
from pdf2image import convert_from_path
from PIL import Image
import io

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf', 'txt', 'jpg', 'jpeg', 'png', 'docx', 'doc'}

def allowed_file(filename):
      return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
      return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
      if 'file' not in request.files:
                return {'error': 'No file provided'}, 400

      file = request.files['file']
      conversion_type = request.form.get('type')

    if file.filename == '':
              return {'error': 'No file selected'}, 400

    if not allowed_file(file.filename):
              return {'error': 'File type not allowed'}, 400

    try:
              filename = secure_filename(file.filename)
              filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
              file.save(filepath)

        # PDF to Images conversion
              if conversion_type == 'pdf_to_image':
                            images = convert_from_path(filepath)
                            img_io = io.BytesIO()
                            images[0].save(img_io, format='PNG')
                            img_io.seek(0)
                            os.remove(filepath)
                            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='converted.png')

              # PDF to Text conversion
              elif conversion_type == 'pdf_to_text':
                            text_content = ""
                            with open(filepath, 'rb') as f:
                                              reader = PyPDF2.PdfReader(f)
                                              for page in reader.pages:
                                                                    text_content += page.extract_text()

                                          text_io = io.BytesIO(text_content.encode())
                            os.remove(filepath)
                            return send_file(text_io, mimetype='text/plain', as_attachment=True, download_name='converted.txt')

              # Image to PDF conversion
              elif conversion_type == 'image_to_pdf':
                            image = Image.open(filepath)
                            pdf_io = io.BytesIO()
                            image.convert('RGB').save(pdf_io, format='PDF')
                            pdf_io.seek(0)
                            os.remove(filepath)
                            return send_file(pdf_io, mimetype='application/pdf', as_attachment=True, download_name='converted.pdf')

              else:
                            return {'error': 'Invalid conversion type'}, 400

except Exception as e:
          return {'error': f'Conversion failed: {str(e)}'}, 500

if __name__ == '__main__':
      app.run(debug=True, port=5000)
