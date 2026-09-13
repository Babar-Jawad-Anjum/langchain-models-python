from langchain_community.document_loaders import WebBaseLoader

url = "https://www.amazon.com/Charger-Adapter-Charging-Cigarette-Lighter/dp/B0CRY1MG68?pf_rd_p=0cc671e6-2b8b-40f1-9be0-d5410868f3af&pf_rd_r=8WERFWSDAM5BXRQSZETF&ref_=ss26-essentialsfront_B0CRY1MG68&th=1"

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)