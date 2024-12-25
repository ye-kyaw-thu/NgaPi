#!/bin/bash

## Test commands run by Ye, LU Lab., Myanmar
## Test input filename is ma_thaung.txt.
## Date: 25 Dec 2024

mkdir exp2;
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

## Test-4
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thaung.txt \
--graph_filename ./exp2/tst2.distances-eg4 --chunk_filename ./exp2/ma_thaung.chunk4.txt \
--percentile_threshold 70 --y_upper_bound 0.6 --syllable_group_length 5 --apply_syllable_break \
--chunks_per_line 10 --syllable_group_separator "_" --chunk_separator "|"

## Test-5
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thaung.txt \
--graph_filename ./exp2/tst2.distances-eg5 --chunk_filename ./exp2/ma_thaung.chunk5.txt \
--percentile_threshold 30 --y_upper_bound 0.5 --syllable_group_length 1 --apply_syllable_break \
--chunks_per_line 10 --syllable_group_separator "_" --chunk_separator "|"
