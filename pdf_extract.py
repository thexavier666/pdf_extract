# Used for command line arguments
import sys

# Used for extracting PDF contents
import pdfquery

def main():
	# Number of arguments must be 2
	# Otherwise error will be thrown

	if len(sys.argv) < 3:
		print "\nUsage : python pdf_extract <file_name>.pdf <output_file>"
		print "Note  : XML file will be created. No need to put .xml extension in output file name\n"

	else:
		try:
			# Takes the PDF file from command line argument
			pdf = pdfquery.PDFQuery(sys.argv[1])
		except:
			print "File doesn't exists in the specified directory!"
			return 0

		# Loads page 0 into memory
		# Use pdf.load() to load entire file
		# Use pdf.load(1,3,5) to load select pages
		pdf.load(0)

		# Outputs the entire contents into output file
		# Use jQuery to extract data
		pdf.tree.write(str(sys.argv[2] + ".xml"),pretty_print=True)

	return 0

if __name__ == '__main__':
	main()