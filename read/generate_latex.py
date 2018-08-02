import os
import sort
import pandas as pd

from pylatex.utils import italic, NoEscape
from pylatex.basic import NewLine
from pylatex.base_classes import Arguments
from pylatex import Document, Section, Itemize, Command, Package, Subsection


sort.main()

geometry_options = {'margin': '1in'}

document = Document('.', geometry_options=geometry_options)
document.packages.append(Package('hyperref'))
document.preamble.append(Package('biblatex', options=['sorting=none']))
document.preamble.append(Command('addbibresource', arguments=['books/read.bib,papers/read.bib']))

document.preamble.append(Command('title', 'Reading List'))
document.preamble.append(Command('author', 'Daniel Saunders'))
document.preamble.append(Command('date', NoEscape(r'\today')))
document.append(NoEscape(r'\maketitle'))

document.append('Note: Work in progress. Some dates before mid-July 2018 are approximate.')


def create_read_section(document, medium):
	with document.create(Subsection('Read')):
		with document.create(Itemize()) as itemize:
			try:
				df = pd.read_csv(os.path.join(medium, 'read.csv'))
			except pd.errors.EmptyDataError:
				return

			for _, row in df.iterrows():
				title = row.Title
				read = row.Read
				link = row.Link
				bibtex = row['BibTex Identifier']
				synopsis = row.Synopsis

				itemize.add_item(italic(title))
				itemize.append(NewLine())
				itemize.append(f'Read date: {read}')
				itemize.append(NewLine())

				arguments = Arguments(link, link)
				itemize.append(Command('href', arguments=arguments))
				itemize.append(NewLine())
				itemize.append(f'Synopsis: {synopsis}')


def create_reading_section(document, medium):
	with document.create(Subsection('Reading')):
		with document.create(Itemize()) as itemize:
			try:
				df = pd.read_csv(os.path.join(medium, 'reading.csv'))
			except pd.errors.EmptyDataError:
				return

			for _, row in df.iterrows():
				title = row.Title
				link = row.Link
				bibtex = row['BibTex Identifier']

				itemize.add_item(italic(title))
				itemize.append(NewLine())

				arguments = Arguments(link, link)
				itemize.append(Command('href', arguments=arguments))


for medium in ['books', 'papers']:
	with document.create(Section(medium.capitalize())):
		if medium == 'books':
			create_read_section(document, medium)
			create_reading_section(document, medium)

		elif medium == 'papers':
			create_read_section(document, medium)

document.append(Command('printbibliography'))
document.generate_tex('read')
document.generate_pdf('read', compiler='pdflatex', clean_tex=False)