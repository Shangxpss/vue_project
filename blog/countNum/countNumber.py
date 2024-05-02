from collections import Counter
from docx import Document


def cuntWord(path: str):
    document = Document("passage.docx")
    para = document.add_paragraph("This is new")

    paragraph = document.paragraphs
    text:list[str] = []
    for item in paragraph:
        text.extend(item.text.lower().split(" "))
    
    result = Counter(text)
    print(result)


if __name__ == "__main__":
    cuntWord("")
