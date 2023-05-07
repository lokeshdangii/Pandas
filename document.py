# importing the required module  
import pdfkit  
  
# configuring pdfkit to point to our installation of wkhtmltopdf  
config = pdfkit.configuration(wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")  
  
# converting html file to pdf file  
pdfkit.from_url('https://www.splashlearn.com/math-vocabulary/geometry/bar-graph', 'newoutput.pdf', configuration = config)  