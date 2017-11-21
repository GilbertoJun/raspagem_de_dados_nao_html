from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator

fp = open('Lista_samurai_X.pdf', 'rb')

parser = PDFParser(fp)
doc = PDFDocument()
parser.set_document(doc)
doc.set_parser(parser)
doc.initialize('')

resource_manager = PDFResourceManager()
laparams = LAParams()
laparams.line_margin = 0.3
laparams.word_margin = 0.3

device = PDFPageAggregator(resource_manager, laparams=laparams)

interpreter = PDFPageInterpreter(resource_manager, device)

for page in doc.get_pages():
    interpreter.process_page(page)
    layout = device.get_result()
    for ltobject in layout:
        print(ltobject.get_text())
