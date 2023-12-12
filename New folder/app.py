

# import openai
# from flask import Flask, render_template, request
# from PyPDF2 import PdfReader
# import os
# import re

# app = Flask(__name__)

# # Set your OpenAI API key
# openai.api_key = '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'

# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'pdf'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# def extract_text_from_pdf(file_path):
#     with open(file_path, 'rb') as file:
#         pdf_reader = PdfReader(file)
#         text = ''
#         for page_num in range(len(pdf_reader.pages)):
#             text += pdf_reader.pages[page_num].extract_text()
#     return text


# def answer_user_question(user_text, user_prompt):
#     prompt = f"{user_text}\nUser's Prompt: {user_prompt}\nAnswer:"

#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=200,
#         stop=["\n"]  # Stop generation at the first line break to get a concise answer
#     )

#     answer = response['choices'][0]['text'].strip()
#     return answer



# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if 'file' in request.files and request.files['file']:
#             # User uploaded a file
#             pdf_file = request.files['file']
#             if pdf_file and allowed_file(pdf_file.filename):
#                 # Save the uploaded PDF temporarily
#                 pdf_file_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
#                 pdf_file.save(pdf_file_path)

#                 # Extract text from the PDF
#                 pdf_content = extract_text_from_pdf(pdf_file_path)

#                 # Delete the temporary PDF file
#                 os.remove(pdf_file_path)
#             else:
#                 return "Invalid file type. Please upload a PDF file."
#         else:
#             return "No file uploaded. Please upload a PDF file."

#         # User's prompt
#         user_prompt = request.form.get('user_prompt', '')

#         # Handle the case where the user doesn't enter a prompt
#         if not user_prompt:
#             return "Please enter a prompt."

#         # Get the answer based on the user's text and prompt
#         answer = answer_user_question(pdf_content, user_prompt)
#         return render_template('index.html', pdf_content=pdf_content, user_prompt=user_prompt, answer=answer)

#     return render_template('index.html')


# if __name__ == '__main__':
#     # Create the 'uploads' folder if it doesn't exist
#     if not os.path.exists(app.config['UPLOAD_FOLDER']):
#         os.makedirs(app.config['UPLOAD_FOLDER'])

#     app.run(debug=True)


# import openai
# from flask import Flask, render_template, request
# from PyPDF2 import PdfReader
# import os
# import re

# app = Flask(__name__)

# # Set your OpenAI API key
# openai.api_key = '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'

# # Hardcode the PDF file path from your local system
# PDF_FILE_PATH = './uploads/sodapdf-converted.pdf'

# def extract_text_from_pdf(file_path):
#     with open(file_path, 'rb') as file:
#         pdf_reader = PdfReader(file)
#         text = ''
#         for page_num in range(len(pdf_reader.pages)):
#             text += pdf_reader.pages[page_num].extract_text()
#     return text

# def answer_user_question(user_text, user_prompt):
#     prompt = f"{user_text}\nUser's Prompt: {user_prompt}\nAnswer:"

#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=200,
#         stop=["\n"]
#     )

#     answer = response['choices'][0]['text'].strip()
#     return answer

# @app.route('/')
# def index():
#     # Extract text from the hardcoded PDF file
#     pdf_content = extract_text_from_pdf(PDF_FILE_PATH)

#     # User's prompt (you can set this to any default prompt you want)
#     user_prompt = "What information is available about the sofa set?"

#     # Get the answer based on the user's text and prompt
#     answer = answer_user_question(pdf_content, user_prompt)
#     return render_template('index.html', pdf_content=pdf_content, user_prompt=user_prompt, answer=answer)

# if __name__ == '__main__':
#     app.run(debug=True)


import openai
from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

# Hardcode the PDF file path from your local system
PDF_FILE_PATH = './uploads/sodapdf-converted.pdf'

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def answer_user_question(user_text, user_prompt):
    prompt = f"{user_text}\nUser's Prompt: {user_prompt}\nAnswer:"

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=200,
        stop=["\n"]
    )

    answer = response['choices'][0]['text'].strip()
    return answer

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract text from the hardcoded PDF file
        pdf_content = extract_text_from_pdf(PDF_FILE_PATH)

        # User's prompt entered through the form
        user_prompt = request.form.get('user_prompt', '')

        # Handle the case where the user doesn't enter a prompt
        if not user_prompt:
            return "Please enter a question."

        # Get the answer based on the user's text and prompt
        answer = answer_user_question(pdf_content, user_prompt)
        return render_template('index.html', pdf_content=pdf_content, user_prompt=user_prompt, answer=answer)

    return render_template('index.html', pdf_content='', user_prompt='', answer='')

if __name__ == '__main__':
    app.run(debug=True)
