import PyPDF2  # Import the PyPDF2 library for reading PDF files
import re  # Import the re library for regular expressions
import sys  # Import the sys library for command-line arguments

def get_links(pdf_file):
    """Extract URLs from a PDF file and return them as a set."""
    with open(pdf_file, 'rb') as file:
        # Create a PdfReader object from the PDF file
        pdf = PyPDF2.PdfReader(file)
        # Get the total number of pages in the PDF document
        num_of_pages = len(pdf.pages)
        # Initialize an empty set to store the extracted URLs
        links = set()
        # Loop through each page of the PDF document
        for p in range(num_of_pages):
            page = pdf.pages[p]
            # Check if the page contains annotations
            if '/Annots' in page:
                # Loop through each annotation on the page
                for annot in page['/Annots']:
                    # Get the subtype of the annotation
                    subtype = annot.get_object()['/Subtype']
                    # Check if the subtype is '/Link'
                    if subtype == '/Link':
                        try:
                            # Extract the URL from the '/URI' key of the annotation object
                            url = annot.get_object()['/A']['/URI']
                            # Add the URL to the links set
                            links.add(url)
                        except KeyError:
                            # If the '/URI' key is not present, ignore the annotation
                            pass
        # Use regular expressions to extract URLs from the text of each page
        page_texts = (page.extract_text() for page in pdf.pages)
        urls = (re.findall(r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text) for text in page_texts)
        # Update the links set with the extracted URLs
        links.update(url for url_list in urls for url in url_list)
        # Return the links set
        return links

# Check if the user has provided a PDF file as a command-line argument
if len(sys.argv) > 1 and sys.argv[1].endswith('.pdf'):
    print("processing...")
    pdf_file = sys.argv[1]
    # Call the get_links() function with the PDF file path and print the extracted URLs
    all_links = get_links(pdf_file)
    print(all_links)
else:
    print("Please enter a pdf file as the second argument\n"/
          "Example: python link_extractor.py sample.pdf\n")
    sys.exit()