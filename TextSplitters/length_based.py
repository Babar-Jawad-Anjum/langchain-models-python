from langchain_text_splitters import CharacterTextSplitter

text = """
Data acquired in wellbores is intricate, varied, and represents a significant investment. 
It is imperative to capitalize on that investment, whether you are working on your first 
deepwater exploration well or delivering a comprehensive drilling program in a shale gas 
play. With Techlog wellbore software, you can bring all of your wellbore data into one 
highly intuitive application to carry out analyses. In addition to offering advanced modules 
for domain experts, Techlog wellbore software provides a solid foundation for generalist users 
to review and analyze the data. It supports complex workflows across multiple disciplines.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator="" # i.e ["\n\n", "\n", " ", ""]
)

result = splitter.split_text(text)

print(result)