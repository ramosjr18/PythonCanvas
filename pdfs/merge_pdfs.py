import PyPDF2
import sys

def merge_pdfs(pdf_list, output):
    # Create a PDF object to write the merged output
    merger = PyPDF2.PdfFileMerger()

    # Loop through the list of PDF files
    for pdf in pdf_list:
        # Open each PDF file
        with open(pdf, "rb") as file:
            # Add each PDF file to the merger object
            merger.append(file)

    # Write the output to a new PDF file
    with open(output, "wb") as file:
        merger.write(file)

if __name__ == "__main__":
    # Get the list of PDF files from the command line
    pdf_list = sys.argv[1:-1]
    # Get the output file name from the command line
    output = sys.argv[-1]
    # Merge the PDF files
    merge_pdfs(pdf_list, output)