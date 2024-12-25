#!/bin/bash

## Test commands run by Ye, LU Lab., Myanmar
## Test input filename is ma_thein.txt.
## Date: 25 Dec 2024

mkdir exp1;

## Test-1
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thein.txt \
--graph_filename ./exp1/tst1.distances-eg1 --chunk_filename ./exp1/ma_thein.chunk1.txt  --apply_syllable_break \
--syllable_group_separator "_" --chunk_separator "|"

## Test-2
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thein.txt \
--graph_filename ./exp1/tst1.distances-eg2 --chunk_filename ./exp1/ma_thein.chunk2.txt --percentile_threshold 40 \
--apply_syllable_break --chunks_per_line 5 \
--syllable_group_separator "_" --chunk_separator "|"

## Test-3
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thein.txt \
--graph_filename ./exp1/tst1.distances-eg3 --chunk_filename ./exp1/ma_thein.chunk3.txt --percentile_threshold 30 \
--y_upper_bound 0.5 --apply_syllable_break --chunks_per_line 5 \
--syllable_group_separator "_" --chunk_separator "|"

## Test-4
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thein.txt \
--graph_filename ./exp1/tst1.distances-eg4 --chunk_filename ./exp1/ma_thein.chunk4.txt --percentile_threshold 70 \
--y_upper_bound 0.5 --syllable_group_length 5 --apply_syllable_break \
--chunks_per_line 10 --syllable_group_separator "_" --chunk_separator "|"

## Test-5
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thein.txt \
--graph_filename ./exp1/tst1.distances-eg5 --chunk_filename ./exp1/ma_thein.chunk5.txt --percentile_threshold 70 \
--y_upper_bound 0.1 --syllable_group_length 1 --apply_syllable_break \
--chunks_per_line 10 --syllable_group_separator "_" --chunk_separator "|"
