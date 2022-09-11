import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

text_input = st.text_area('Text to summarize')

lex_rank_summarizer = LexRankSummarizer()

@st.cache
def summarize(string, no_of_sent):
    my_parser = PlaintextParser.from_string(string, Tokenizer('english'))
    summary = lex_rank_summarizer(my_parser.document, sentences_count=no_of_sent)
    return '. '.join([str(i) for i in summary])


no_on_sent = st.slider('No of Sentences', 0, 10, 3)
if st.button('Summarize'):
    summarized_text = summarize(text_input, no_on_sent)
    st.subheader('Summarized Text:')
    summarized_text
