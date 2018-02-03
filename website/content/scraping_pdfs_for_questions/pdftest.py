from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import glob

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def parseString(plain_text):
    sentence = ''
    return_text = ''
    for c in plain_text:
        if(c != '\n'):
            if (c == '?'):
                sentence += '?\n'
                return_text += sentence
                sentence = ''
            else:
                sentence += c
        else:
            sentence = ''

    return return_text

def main():
    file = open("pdfresponse.txt", "w")

    for filename in glob.glob('pdf_only/*.pdf'):
        print(filename)
        plain_text = convert_pdf_to_txt(filename)
        file.write(parseString(plain_text))
        file.flush()

    file.close


if __name__ == '__main__':
    main()
