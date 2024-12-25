"""
To convert a binary fastText model into a vector format.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 25 Dec 2024
How to run:
python bin2vec.py --binary_file ./model/myfasttext_v1.bin --vector_file ./model/myfasttext_v1.vec
"""
import argparse
import fasttext

# Set up argument parser
parser = argparse.ArgumentParser(description="Convert FastText binary model to vector format in pure text.")
parser.add_argument("--binary_file", type=str, required=True, help="Path to the binary FastText model file.")
parser.add_argument("--vector_file", type=str, required=True, help="Path to save the text format file.")
args = parser.parse_args()

# Load binary model and save as text vector format
try:
    ft_model = fasttext.load_model(args.binary_file)  # Load the binary FastText model
    
    # Save the model to a pure text vector format
    with open(args.vector_file, "w", encoding="utf-8") as f:
        words = ft_model.get_words()  # Get all words in the vocabulary
        vector_size = ft_model.get_dimension()  # Get vector size
        f.write(f"{len(words)} {vector_size}\n")  # Write header: number of words and vector size
        for word in words:
            vector = ft_model.get_word_vector(word)  # Get the vector for each word
            vector_str = " ".join(map(str, vector))  # Convert vector to space-separated string
            f.write(f"{word} {vector_str}\n")  # Write word and its vector
    print(f"Converted {args.binary_file} to {args.vector_file} in pure text format successfully.")
except Exception as e:
    print(f"Error: {e}")

