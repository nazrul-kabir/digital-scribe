import argparse
from evaluation.tokenizer import get_tokenizer

def main():
    parser = argparse.ArgumentParser(description='Clinical F1 Evaluation Tool')
    parser.add_argument('--lang_model', default='fi_core_news_sm', help='spaCy language model for tokenization')
    args = parser.parse_args()

    tokenizer = get_tokenizer(args.lang_model)
    print("Tokenizer loaded. Ready to process clinical text.")

if __name__ == '__main__':
    main()