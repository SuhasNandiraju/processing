from summa import summarizer, keyword

def format_paragraphs_gc(text):
    return text.split("\n")

def format_paragraphs(text, max_keys=8):
    text = text.replace("\n", "").replace("\t", " ").split()
    paragraphs = []
    paragraph = ""
    for i in range(len(text)):
        paragraph+=text[i]
        if len(keywords.keywords(paragraph).split("\n")) >= 8 :
            paragraphs.append(paragraph)
            paragraph=""
        return paragraphs

def get_summary(text):
    bullets = []
    for i in format_paragraphs_gc(text):
        bullets.append(summarizer.summarize(i))

    return {"bullets" : bullets}

def get_summary_indiv(text):
    return {"bullet" : summarizer.summarize(text).replace("\n", "").replace("\t", " ")}
