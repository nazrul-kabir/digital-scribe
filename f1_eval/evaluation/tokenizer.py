import spacy

def get_tokenizer(model_name='fi_core_news_sm'):
    try:
        return spacy.load(model_name)
    except Exception as e:
        raise RuntimeError(f"Could not load spaCy model '{model_name}': {e}")