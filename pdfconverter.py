from pdfconverter import argument
from pdfconverter import program
from pdfconverter.__variables__ import Var
from pdfconverter.program import folder_structure
from pdfconverter.settings import pandas


pandas.set_settings()

argument.set_arguments()

folder_structure.create()

Var.ConversionInfo.conversion_type()

program.finish()
