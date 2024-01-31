import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader

url = "https://www.researchgate.net/publication/346468901_Comparative_Analysis_of_Comparison_and_Non_Comparison-based_Sorting_Algorithms"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

pdf_file_url = soup.find("a", {"href": re.compile(r".*\.pdf")})["href"]

pdf_file = requests.get(pdf_file_url)
pdf_reader = PdfFileReader(pdf_file.content)

text = ""
for page in pdf_reader.pages:
    text += page.extractText()

print(text)