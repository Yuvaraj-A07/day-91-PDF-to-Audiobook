# importing the modules
import PyPDF2
import pyttsx3


def pdf_to_text(pdf_path):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfReader object instead of PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the text
        texts = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            texts += page.extract_text()
    return texts


text = pdf_to_text("DBMS SET1.pdf")
print(text)

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()

# import requests
# import PyPDF2
#
# # Step 1: Extract text from PDF
# pdf_file_path = 'example.pdf'
# with open(pdf_file_path, 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#     extracted_text = ""
#     for page in pdf_reader.pages:
#         extracted_text += page.extract_text()
#
# # Step 2: Convert text to speech using iSpeech API
# url = "http://api.ispeech.org/api/rest"
# params = {
#     'apikey': 'YOUR_API_KEY',
#     'action': 'convert',
#     'text': extracted_text,
#     'voice': 'usenglishfemale',
#     'format': 'mp3',
#     'output': 'data'
# }
#
# response = requests.get(url, params=params)
#
# # Save the response as an audio file
# with open('output.mp3', 'wb') as audio_file:
#     audio_file.write(response.content)
#
# print("PDF text has been converted to speech and saved as 'output.mp3'.")
