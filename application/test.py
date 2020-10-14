import pdftotext
with open("./cvs/demo.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

print(type("\n\n".join(pdf)))
