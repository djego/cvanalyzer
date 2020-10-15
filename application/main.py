import os
import pdftotext
from summarize import summarize
from csv import DictWriter
import nltk

## make sure i have download 'stopwords', 'punkt' 
nltk.download(['stopwords', 'punkt'])

with open("./cvs/demo.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)


def get_text(filename):
    with open(filename, 'rb') as in_file:
        pdf = pdftotext.PDF(in_file)

    return "\n\n".join(pdf)


def get_summary(text):
    return summarize(text,sentence_count=5, language='spanish')   

# def get_cloud(text):
#     return keywords.keywords(text)

directory = 'cvs'
result_analyzer = []

for filename in os.listdir(directory):
    if filename.endswith(".pdf"): 
        text_cv = get_text(os.path.join(directory, filename))
        summary = get_summary(text_cv)
        dict_analyzer = {"filename": filename, 'full': text_cv, 'summary': summary}
        result_analyzer.append(dict_analyzer)


with open('output.csv','w') as outfile:
    writer = DictWriter(outfile, ('filename','full','summary'))
    writer.writeheader()
    writer.writerows(result_analyzer)
