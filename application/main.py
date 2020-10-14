import os
import pdftotext
from summarize import summarize
from csv import DictWriter
## make sure i have download 'stopwords', 'punkt' 
import nltk
nltk.download(['stopwords', 'punkt'])

with open("./cvs/demo.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)



def get_text(filename):
    with open(filename, 'rb') as in_file:
        pdf = pdftotext.PDF(in_file)

    return "\n\n".join(pdf)


def get_summary(text):
    return summarizer.summarize(text, language='spanish')   

def get_keywords(text):
    return keywords.keywords(text)

directory = 'cvs'
result_analyzer = []

for filename in os.listdir(directory):
    if filename.endswith(".pdf"): 
        text_cv = get_text(os.path.join(directory, filename))
        # summary = get_summary(text_cv)
        # try:
        #     keywords = get_keywords(text_cv)
        # except AttributeError as e:
        #     keywords = ''
        dict_analyzer = {"filename": filename, 'full': text_cv}
        result_analyzer.append(dict_analyzer)


with open('result.csv','w') as outfile:
    writer = DictWriter(outfile, ('filename','full'))
    writer.writeheader()
    writer.writerows(result_analyzer)
