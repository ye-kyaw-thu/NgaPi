"""
Ngapi is a semantic chunker based on fastText word embeddings for the Myanmar language.
This approach can also be applied to other languages.

About Ngapi: Ngapi is a traditional fermented fish or shrimp paste widely used in Myanmar cuisine,
known for its strong and distinctive smell.

Written by Ye Kyaw Thu, LU Lab., Myanmar
Last updated: 25 Dec 2024
Reference:
The 5 Levels Of Text Splitting For Retrieval, 
https://www.youtube.com/watch?v=8OJC21T2SL4&t=2112s  

How to Run:

Run ngapi.py with the --help option for usage details.
For more information, please refer to the two semantic chunking experiments
available here (https://github.com/ye-kyaw-thu/NgaPi/tree/main/test).

## Test-1
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thaung.txt \
--graph_filename ./exp2/tst2.distances-eg1 --chunk_filename ./exp2/ma_thaung.chunk1.txt \
--apply_syllable_break --chunks_per_line 3 \
--syllable_group_separator "_" --chunk_separator "|"

## Test-2
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thaung.txt \
--graph_filename ./exp2/tst2.distances-eg2 --chunk_filename ./exp2/ma_thaung.chunk2.txt \
--percentile_threshold 50 --apply_syllable_break \
--syllable_group_separator "_" --chunk_separator "|"

## Test-3
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thaung.txt \
--graph_filename ./exp2/tst2.distances-eg3 --chunk_filename ./exp2/ma_thaung.chunk3.txt \
--percentile_threshold 60 --y_upper_bound 0.6 --apply_syllable_break --chunks_per_line 2 \
--syllable_group_separator "_" --chunk_separator "|" 

"""

import argparse
import fasttext
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import re

def create_break_pattern():
    """Creates and returns the regular expression pattern for Myanmar syllable breaking."""
    my_consonant = r"က-အ"
    other_char = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
    subscript_symbol = r'္'
    a_that = r'်'

    # Regular expression pattern for Myanmar syllable breaking
    return re.compile(
        r"((?<!" + subscript_symbol + r")[" + my_consonant + r"]"
        r"(?!["
        + a_that + subscript_symbol + r"])"
        + r"|[" + other_char + r"])"
    )

def break_syllables(line, break_pattern, separator=' '):
    """Applies syllable breaking rules to a line."""
    line = re.sub(r'\s+', ' ', line.strip())
    segmented_line = break_pattern.sub(separator + r"\1", line)

    # Remove the leading delimiter if it exists
    if segmented_line.startswith(separator):
        segmented_line = segmented_line[len(separator):]

    # Replace delimiter+space+delimiter with a single space
    double_delimiter = separator + " " + separator
    segmented_line = segmented_line.replace(double_delimiter, " ")

    return segmented_line

def combine_sentences(sentences, buffer_size=1):
    for i in range(len(sentences)):
        combined_sentence = ''
        for j in range(i - buffer_size, i):
            if j >= 0:
                combined_sentence += sentences[j]['sentence'] + ' '
        for j in range(i + 1, i + 1 + buffer_size):
            if j < len(sentences):
                combined_sentence += ' ' + sentences[j]['sentence']

        sentences[i]['combined_sentence'] = combined_sentence
    return sentences

def process_file(file_path, group_length=2, break_pattern=None):
    result = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:

            # Apply syllable breaking
            if break_pattern:
                line = break_syllables(line, break_pattern)

            words = line.split()  # Split the line into words
            # Create variable-length word groups
            word_groups = [' '.join(words[i:i+group_length]) for i in range(0, len(words), group_length)]
            result.extend(word_groups)  # Add to the result list
    return result

def embed_documents(sentences, model):
    embeddings = [np.mean([model.get_word_vector(word) for word in sentence.split()], axis=0)
                  if sentence.strip() else np.zeros(model.get_dimension())
                  for sentence in sentences]
    return embeddings

def calculate_cosine_distances(sentences):
    distances = []
    for i in range(len(sentences) - 1):
        embedding_current = sentences[i]['combined_sentence_embedding']
        embedding_next = sentences[i + 1]['combined_sentence_embedding']

        similarity = cosine_similarity([embedding_current], [embedding_next])[0][0]
        distance = 1 - similarity
        distances.append(distance)
        sentences[i]['distance_to_next'] = distance

    return distances, sentences

def main():
    parser = argparse.ArgumentParser(description="Process text and visualize embeddings.")
    parser.add_argument('--model', required=True, help="Path to the FastText model file.")
    parser.add_argument('--input', required=True, help="Path to the input text file.")
    parser.add_argument('--buffer', type=int, default=3000, help="Buffer size for printing chunks. Default: 3000")
    parser.add_argument('--percentile_threshold', type=int, default=70, help="Breakpoint percentile threshold. Default: 70")
    parser.add_argument('--y_upper_bound', type=float, default=1.0, help="Upper bound for the Y-axis in the plot. Default: 1.0")
    parser.add_argument('--graph_filename', required=True, help="Filename for saving the graph (without extension). Default: 1.0")
    parser.add_argument('--chunk_filename', help="Filename to save the segmented chunks.")
    parser.add_argument('--syllable_group_length', type=int, default=6, help="Initial syllable group length. Default: 6")
    parser.add_argument('--apply_syllable_break', action='store_true', help="Apply Myanmar syllable breaking to the input file.")
    parser.add_argument('--syllable_group_separator', type=str, default="_", help="Separator for syllable group. Default is a newline ('_').")
    parser.add_argument('--chunk_separator', type=str, default="|", help="Separator for syllable group. Default is a newline ('|').")

    parser.add_argument('--chunks_per_line', type=int, default=None, 
                        help="Number of segments per line. If not specified, outputs as a single line.")

    args = parser.parse_args()

    # Load FastText model
    model = fasttext.load_model(args.model)

    # Create syllable break pattern if needed
    break_pattern = create_break_pattern() if args.apply_syllable_break else None

    # Process input file with optional syllable breaking
    #group_length = 6  # Default group length for splitting words
    word_groups = process_file(args.input, args.syllable_group_length, break_pattern)

    # Prepare sentences
    sentences2 = [{'sentence': x, 'index': i} for i, x in enumerate(word_groups)]
    sentences = combine_sentences(sentences2)

    # Embed documents
    embeddings = embed_documents([x['combined_sentence'] for x in sentences], model)
    for i, sentence in enumerate(sentences):
        sentence['combined_sentence_embedding'] = embeddings[i]

    # Calculate cosine distances
    distances, sentences = calculate_cosine_distances(sentences)

    # Plot distances
    plt.plot(distances)
    plt.ylim(0, args.y_upper_bound)
    plt.xlim(0, len(distances))
    breakpoint_distance_threshold = np.percentile(distances, args.percentile_threshold)
    plt.axhline(y=breakpoint_distance_threshold, color='r', linestyle='-')

    # Add text annotation for the number of chunks
    num_distances_above_threshold = len([d for d in distances if d > breakpoint_distance_threshold])-1
    plt.text(x=(len(distances) * 0.01), 
             y=args.y_upper_bound / 50, 
             s=f"{num_distances_above_threshold + 1} Chunks", 
             color='black', fontsize=10)

    # Add breakpoints and regions
    indices_above_thresh = [i for i, x in enumerate(distances) if x > breakpoint_distance_threshold]
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i, breakpoint_index in enumerate(indices_above_thresh):
        start_index = 0 if i == 0 else indices_above_thresh[i - 1]
        end_index = breakpoint_index if i < len(indices_above_thresh) - 1 else len(distances)
        plt.axvspan(start_index, end_index, facecolor=colors[i % len(colors)], alpha=0.25)

    if indices_above_thresh:
        last_breakpoint = indices_above_thresh[-1]
        if last_breakpoint < len(distances):
            plt.axvspan(last_breakpoint, len(distances), facecolor=colors[len(indices_above_thresh) % len(colors)], alpha=0.25)

    plt.title("Chunks Based On FastText Embedding Breakpoints")
    plt.xlabel("Index of Tokens (e.g. a group of syllables)")
    plt.ylabel("Cosine distance between sequential tokens")
    plt.savefig(f"{args.graph_filename}.png")
    plt.savefig(f"{args.graph_filename}.pdf")

    # Segment into chunks
    start_index = 0
    chunks = []
    for index in indices_above_thresh:
        end_index = index - 1
        group = sentences[start_index:end_index + 1]
        combined_text = args.syllable_group_separator.join([d['sentence'].replace(" ", "") for d in group])  # Remove spaces between syllables
        chunks.append(combined_text)
        start_index = index

    if start_index < len(sentences):
        combined_text = args.syllable_group_separator.join([d['sentence'].replace(" ", "") for d in sentences[start_index:]])  # Remove spaces between syllables
        chunks.append(combined_text)

    # Remove empty chunks
    chunks = [chunk for chunk in chunks if chunk]
    print("No. of chunks: ", len(chunks)) #; exit()
    #print("chunks[0]", chunks[0]); print("chunks[1]", chunks[1]); exit()

    # Apply word wrapping based on chunks_per_line
    if args.chunks_per_line:
        wrapped_chunks = []
        for i in range(0, len(chunks), args.chunks_per_line):
            wrapped_line = args.chunk_separator.join(chunks[i:i + args.chunks_per_line])
            wrapped_chunks.append(wrapped_line)
    else:
        wrapped_chunks = chunks  # No wrapping if chunks_per_line is not specified

   # Print wrapped chunks
    for i, line in enumerate(wrapped_chunks):
        print(f"Chunk line #{i + 1}")
        print(line[:args.buffer].strip())

    #print(wrapped_chunks[-1][-args.buffer:].strip())

    # Save wrapped chunks to file if specified
    if args.chunk_filename:
        with open(args.chunk_filename, 'w', encoding='utf-8') as f:
            for line in wrapped_chunks:
                if line.strip():  # Only write non-empty lines
                    f.write(line.strip() + "\n")  # Always use a newline to separate lines in the file
        print(f"Chunks saved to {args.chunk_filename}")


if __name__ == "__main__":
    main()

