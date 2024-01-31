# run this on sheet1 to get the DOIs
# just change the file names in the third to last line and the last line
from habanero import Crossref
import metadata_parser,pikepdf,requests
from io import BytesIO
import pandas as pd
from bs4 import BeautifulSoup
from crossref_commons import retrieval
from tqdm.auto import tqdm
import pdftitle,pdf2doi,doi

tqdm.pandas()
def get_metadata(url):
    try:
        page=metadata_parser.MetadataParser(url)
        return page.metadata['og']
    except:
        return {}
def nex(url,pos,symbols):
    return min([url.find(s,pos) if s in url[pos:] else len(url) for s in symbols])
def get_DOI(row):
    try:
        if doi.validate_doi(row.DOI)!=None:
            return row.DOI
    except:
        pass
    try:
        # title=row["Algorithm Name"]
        url=row["Paper/Reference Link"]
        if doi.find_doi_in_text(url)!=None:
            return doi.find_doi_in_text(url)
        if "10." in url:
            pos=url.find("10.")
            DOI=url[pos:nex(url,pos,"?&")]
            return DOI
        if "acm" in url:
            return ""
        if url[:21]=="https://arxiv.org/pdf":
            url=url[:18]+"abs"+url[21:-4]
        if url[:33]=="https://ieeexplore.ieee.org/stamp":
            url="https://ieeexplore.ieee.org/abstract/document/"+url[url.rfind("=")+1:]
        response=requests.get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        if "pdf" in url:
            with open('./tmp.pdf','wb') as f:
                f.write(response.content)
            return doi.pdf_to_doi("tmp.pdf")
        else:
            return doi.find_doi_in_text(response.text)
            """ if title!="":
                cr=Crossref()
                result=cr.works(query=title)
                DOI=result['message']['items'][0]['DOI']
            if DOI in response.text:
                return DOI """
    except:
        pass
    return ""
def get_title_from_url(url):
    try:
        if "10." in url:
            DOI=url[url.find("10."):url.rfind("?") if "?" in url else len(url)]
            return retrieval.get_publication_as_json(DOI)['title'][0]
        if "acm" in url:
            return ""
        if url[:21]=="https://arxiv.org/pdf":
            url=url[:18]+"abs"+url[21:-4]
        if url[:33]=="https://ieeexplore.ieee.org/stamp":
            url="https://ieeexplore.ieee.org/abstract/document/"+url[url.rfind("=")+1:]
        response=requests.get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        if "pdf" in url:
            pdf=pikepdf.Pdf.open(BytesIO(response.content))
            metadata=pdf.docinfo
            if "\Title" in metadata:
                return metadata["\Title"]
            return pdftitle.get_title_from_io(BytesIO(response.content))
        else:
            soup=BeautifulSoup(response.text,"html.parser")
            if soup.findAll("title"):
                return soup.find("title").string
    except:
        pass
    return ""
def bad(title):
    return title in ["nan","Just a moment...","Redirecting","ACM Error: IP blocked"]
pdf2doi.config.set("save_identifier_metadata",False)
pdf2doi.config.set("verbose",False)
data=pd.read_csv("AlgoWiki algorithms (our copy) - Sheet1.csv")
data["DOI"]=data.progress_apply(get_DOI,axis=1)
data.to_csv("authors_dataset_doi.csv",index=False)