"""
For building fastText model with a segmented corpus.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 25 Dec 2024
How to run:
python ./build-fasttext-model.py --input ./data/myWord_myPOS_myPara_myNovel1v1_wordseg.shuf.cleaned.syl.normalized --model skipgram --output ./model/myfasttext_v1.bin  
python ./build-fasttext-model.py --help
"""

import argparse
import fasttext
import logging
import os

def train_fasttext_model(input_file, output_file, model_type, dim, epoch, lr, ws, logger):
    """Train and save a FastText model."""
    if not os.path.exists(input_file):
        logger.error(f"Input file '{input_file}' does not exist.")
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

    logger.info(f"Starting FastText model training with model_type={model_type}, dim={dim}, epoch={epoch}, lr={lr}, ws={ws}...")

    model = fasttext.train_unsupervised(
        input=input_file,
        model=model_type,
        dim=dim,
        epoch=epoch,
        lr=lr,
        ws=ws
    )

    logger.info(f"Saving FastText model to '{output_file}'...")
    model.save_model(output_file)
    logger.info("FastText model training completed successfully.")

def main():
    parser = argparse.ArgumentParser(description="Build a FastText model from word-segmented text.")
    parser.add_argument("--input", required=True, help="Path to the training text file (word-segmented UTF-8).")
    parser.add_argument("--output", default="fasttext_model.bin", help="Filename for saving the FastText model (default: fasttext_model.bin).")
    parser.add_argument("--model", choices=["skipgram", "cbow"], default="skipgram", help="Model type: skipgram or cbow (default: skipgram).")
    parser.add_argument("--dim", type=int, default=100, help="Dimensionality of word vectors (default: 100).")
    parser.add_argument("--epoch", type=int, default=5, help="Number of epochs (default: 5).")
    parser.add_argument("--lr", type=float, default=0.05, help="Learning rate (default: 0.05).")
    parser.add_argument("--ws", type=int, default=5, help="Context window size (default: 5).")

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
    logger = logging.getLogger()

    try:
        train_fasttext_model(
            input_file=args.input,
            output_file=args.output,
            model_type=args.model,
            dim=args.dim,
            epoch=args.epoch,
            lr=args.lr,
            ws=args.ws,
            logger=logger
        )
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

