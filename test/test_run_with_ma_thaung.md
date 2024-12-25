# Test Run with ma_thaung.txt

ma_thaung.txt ဖိုင်ထဲမှာက အောက်မှာ မြင်ရတဲ့အတိုင်း word segmentation မလုပ်ထားဘူး။ ပြီးတော့ blank line တချို့လည်း ပါဝင်ပါတယ်။  

```
(base) ye@lst-gpu-server-197:~/ye/exp/sem-chunk/4github$ cat ma_thaung.txt
ပန်းသည် မသောင်းက အသက်က ၁၆နှစ်၊ ယဉ်စစနဲ့ နုပျိုမှုခြင်းမှာ မသိန်းထက် အပုံကြီးသာသပေါ့။ ဒီတော့ တက္ကသိုလ်ကျောင်းသားတွေက ပန်းသည် မသောင်းဆိုင်မှာ ပြောင်းပြီး ပန်းဝယ်ကြ၊ စကားတွေ ဖောင်ဖွဲ့ကြတာပေါ့။

မသိန်းပန်းဆိုင် အရင်လို မရောင်းရတော့ဘဲ ခြောက်ကပ်လာတာပေါ့။ ဒီလိုနဲ့ တနေ့ သူ့ပန်းဆိုင်နားကို လင်မယားနှစ်ယောက် ကလေးလေး လက်ဆွဲပြီးရောက်လာ။ အမျိုးသားဖြစ်သူက တပ်ထားတဲ့ မျက်မှန်ချွတ်လိုက်ပြီး ကျနော့်မှတ်မိလားမေး။ မောင်သိန်းခိုင် ဖြစ်နေ။ ပန်းသည်မသိန်းနဲ့ ယောကျ်ားဖြစ်သူ ကိုသိန်းခိုင်တို့ စကားတွေ တရင်းတနှီး ဖောင်ဖွဲ့နေကြတာကြည့်ပြီး ဇနီးဖြစ်သူက အံ့တွေသြ။

သိပ္ပံမောင်ဝက ဒီမှာတင် ပန်းသည် စာမူကို ရပ်ခဲ့တယ်။
```

## Experiment-2

Experiment-2 setting က အောက်ပါအတိုင်း...  
Bash Filename: exp2.sh 

```bash
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

```

```
(base) ye@lst-gpu-server-197:~/ye/exp/sem-chunk/4github$ time ./exp2.sh | tee exp2.log
...
...
...
Chunk line #6
ခြောက်|ကပ်_လာ_တာ_ပေါ့_။_ဒီ|လို|နဲ့|တ|နေ့|သူ့|ပန်း|ဆိုင်|နား
Chunk line #7
ကို|လင်|မ_ယား_နှစ်_ယောက်_က_လေး_လေး|လက်|ဆွဲ_ပြီး_ရောက်_လာ|။_အ_မျိုး_သား_ဖြစ်|သူ|က|တပ်|ထား
Chunk line #8
တဲ့|မျက်|မှန်|ချွတ်|လိုက်|ပြီး|ကျ|နော့်|မှတ်|မိ
Chunk line #9
လား|မေး|။|မောင်|သိန်း|ခိုင်|ဖြစ်|နေ|။|ပန်း
Chunk line #10
သည်|မ|သိန်း_နဲ့_ယော_ကျ်ား_ဖြစ်|သူ|ကို|သိန်း|ခိုင်|တို့_စ_ကား|တွေ|တ
Chunk line #11
ရင်း|တ|နှီး|ဖောင်|ဖွဲ့|နေ_ကြ|တာ_ကြ|ည့်|ပြီး_ဇ_နီး_ဖြစ်_သူ|က
Chunk line #12
အံ့|တွေ|သြ|။|သိပ္ပံ|မောင်|ဝ_က_ဒီ|မှာ|တင်|ပန်း
Chunk line #13
သည်|စာ|မူ|ကို_ရပ်|ခဲ့|တယ်_။
Chunks saved to ./exp2/ma_thaung.chunk5.txt

real    0m2.047s
user    0m4.401s
sys     0m3.630s

real    0m9.526s
user    0m21.184s
sys     0m18.095s
```

exp2.sh shell script ကို run ပြီးထွက်လာတဲ့ output ဖိုင်တွေက အောက်ပါအတိုင်း ...  

```
(base) ye@lst-gpu-server-197:~/ye/exp/sem-chunk/4github$ ls ./exp2/
ma_thaung.chunk1.txt  ma_thaung.chunk5.txt    tst2.distances-eg2.png  tst2.distances-eg4.png
ma_thaung.chunk2.txt  tst2.distances-eg1.pdf  tst2.distances-eg3.pdf  tst2.distances-eg5.pdf
ma_thaung.chunk3.txt  tst2.distances-eg1.png  tst2.distances-eg3.png  tst2.distances-eg5.png
ma_thaung.chunk4.txt  tst2.distances-eg2.pdf  tst2.distances-eg4.pdf
```

## Check on Segmented Outputs

### Command no. 1
 
```bash
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thaung.txt \
--graph_filename ./exp2/tst2.distances-eg1 --chunk_filename ./exp2/ma_thaung.chunk1.txt \
--apply_syllable_break --chunks_per_line 3 \
--syllable_group_separator "_" --chunk_separator "|"

```

ma_thuaung_chunk1.txt:  

```
ပန်းသည်မသောင်းကအ_သက်က၁၆နှစ်၊_ယဉ်စစနဲ့နုပျို|မှုခြင်းမှာမသိန်းထက်_အပုံကြီးသာသပေါ့_။ဒီတော့တက္ကသိုလ်ကျောင်း_သားတွေကပန်းသည်မ_သောင်းဆိုင်မှာပြောင်းပြီးပန်း_ဝယ်ကြ၊စကားတွေ_ဖောင်ဖွဲ့ကြတာပေါ့။_မသိန်းပန်းဆိုင်အရင်_လိုမရောင်းရတော့ဘဲ_ခြောက်ကပ်လာတာပေါ့။_ဒီလိုနဲ့တနေ့သူ့_ပန်းဆိုင်နားကိုလင်မ_ယားနှစ်ယောက်ကလေးလေး|လက်ဆွဲပြီးရောက်လာ။_အမျိုးသားဖြစ်သူက_တပ်ထားတဲ့မျက်မှန်ချွတ်_လိုက်ပြီးကျနော့်မှတ်မိ
လားမေး။မောင်သိန်းခိုင်_ဖြစ်နေ။ပန်းသည်မ|သိန်းနဲ့ယောကျ်ားဖြစ်သူ_ကိုသိန်းခိုင်တို့စကား_တွေတရင်းတနှီးဖောင်|ဖွဲ့နေကြတာကြည့်
ပြီးဇနီးဖြစ်သူက|အံ့တွေသြ။_သိပ္ပံမောင်ဝကဒီမှာ|တင်ပန်းသည်စာမူကို_ရပ်ခဲ့တယ်။

```

### Command no.2 

```bash
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thaung.txt \
--graph_filename ./exp2/tst2.distances-eg2 --chunk_filename ./exp2/ma_thaung.chunk2.txt \
--percentile_threshold 50 --apply_syllable_break \
--syllable_group_separator "_" --chunk_separator "|"

```

ma_thaung_chunk2.txt:  

```
ပန်းသည်မသောင်းကအ_သက်က၁၆နှစ်၊
ယဉ်စစနဲ့နုပျို
မှုခြင်းမှာမသိန်းထက်
အပုံကြီးသာသပေါ့
။ဒီတော့တက္ကသိုလ်ကျောင်း_သားတွေကပန်းသည်မ_သောင်းဆိုင်မှာပြောင်းပြီးပန်း_ဝယ်ကြ၊စကားတွေ_ဖောင်ဖွဲ့ကြတာပေါ့။_မသိန်းပန်းဆိုင်အရင်_လိုမရောင်းရတော့ဘဲ_ခြောက်ကပ်လာတာပေါ့။_ဒီလိုနဲ့တနေ့သူ့_ပန်းဆိုင်နားကိုလင်မ_ယားနှစ်ယောက်ကလေးလေး
လက်ဆွဲပြီးရောက်လာ။_အမျိုးသားဖြစ်သူက_တပ်ထားတဲ့မျက်မှန်ချွတ်_လိုက်ပြီးကျနော့်မှတ်မိ
လားမေး။မောင်သိန်းခိုင်_ဖြစ်နေ။ပန်းသည်မ
သိန်းနဲ့ယောကျ်ားဖြစ်သူ
ကိုသိန်းခိုင်တို့စကား
တွေတရင်းတနှီးဖောင်
ဖွဲ့နေကြတာကြည့်
ပြီးဇနီးဖြစ်သူက
အံ့တွေသြ။
သိပ္ပံမောင်ဝကဒီမှာ
တင်ပန်းသည်စာမူကို_ရပ်ခဲ့တယ်။

```

### Command no.3

```bash
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thaung.txt \
--graph_filename ./exp2/tst2.distances-eg3 --chunk_filename ./exp2/ma_thaung.chunk3.txt \
--percentile_threshold 60 --y_upper_bound 0.6 --apply_syllable_break --chunks_per_line 2 \
--syllable_group_separator "_" --chunk_separator "|"

```

```
ပန်းသည်မသောင်းကအ_သက်က၁၆နှစ်၊_ယဉ်စစနဲ့နုပျို|မှုခြင်းမှာမသိန်းထက်_အပုံကြီးသာသပေါ့_။ဒီတော့တက္ကသိုလ်ကျောင်း_သားတွေကပန်းသည်မ_သောင်းဆိုင်မှာပြောင်းပြီးပန်း_ဝယ်ကြ၊စကားတွေ_ဖောင်ဖွဲ့ကြတာပေါ့။_မသိန်းပန်းဆိုင်အရင်_လိုမရောင်းရတော့ဘဲ_ခြောက်ကပ်လာတာပေါ့။_ဒီလိုနဲ့တနေ့သူ့_ပန်းဆိုင်နားကိုလင်မ_ယားနှစ်ယောက်ကလေးလေး
လက်ဆွဲပြီးရောက်လာ။_အမျိုးသားဖြစ်သူက_တပ်ထားတဲ့မျက်မှန်ချွတ်_လိုက်ပြီးကျနော့်မှတ်မိ|လားမေး။မောင်သိန်းခိုင်_ဖြစ်နေ။ပန်းသည်မ
သိန်းနဲ့ယောကျ်ားဖြစ်သူ|ကိုသိန်းခိုင်တို့စကား
တွေတရင်းတနှီးဖောင်|ဖွဲ့နေကြတာကြည့်
ပြီးဇနီးဖြစ်သူက|အံ့တွေသြ။
သိပ္ပံမောင်ဝကဒီမှာ|တင်ပန်းသည်စာမူကို_ရပ်ခဲ့တယ်။

```

### Command no.4 

```
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thaung.txt \
--graph_filename ./exp2/tst2.distances-eg4 --chunk_filename ./exp2/ma_thaung.chunk4.txt \
--percentile_threshold 70 --y_upper_bound 0.6 --syllable_group_length 5 --apply_syllable_break \
--chunks_per_line 10 --syllable_group_separator "_" --chunk_separator "|"

```

```
ပန်းသည်မသောင်းက_အသက်က၁၆_နှစ်၊ယဉ်စစ_နဲ့နုပျိုမှုခြင်း|မှာမသိန်းထက်အ_ပုံကြီးသာသပေါ့_။ဒီတော့တက္ကသိုလ်_ကျောင်းသားတွေကပန်း_သည်မသောင်းဆိုင်မှာ_ပြောင်းပြီးပန်းဝယ်ကြ_၊စကားတွေဖောင်_ဖွဲ့ကြတာပေါ့။_မသိန်းပန်းဆိုင်အ_ရင်လိုမရောင်းရ_တော့ဘဲခြောက်ကပ်လာ_တာပေါ့။ဒီလို_နဲ့တနေ့သူ့ပန်း_ဆိုင်နားကိုလင်မ_ယားနှစ်ယောက်ကလေး_လေးလက်ဆွဲပြီးရောက်_လာ။အမျိုးသား_ဖြစ်သူကတပ်ထား_တဲ့မျက်မှန်ချွတ်လိုက်_ပြီးကျနော့်မှတ်မိ|လားမေး။မောင်သိန်း_ခိုင်ဖြစ်နေ။ပန်း_သည်မသိန်းနဲ့ယော_ကျ်ားဖြစ်သူကိုသိန်း|ခိုင်တို့စကားတွေ|တရင်းတနှီးဖောင်|ဖွဲ့နေကြတာကြ|ည့်ပြီးဇနီးဖြစ်|သူကအံ့တွေသြ|။|သိပ္ပံမောင်ဝကဒီ
မှာတင်ပန်းသည်စာ_မူကိုရပ်ခဲ့တယ်_။

```

### Command no.5
 
```bash
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thaung.txt \
--graph_filename ./exp2/tst2.distances-eg5 --chunk_filename ./exp2/ma_thaung.chunk5.txt \
--percentile_threshold 30 --y_upper_bound 0.5 --syllable_group_length 1 --apply_syllable_break \
--chunks_per_line 10 --syllable_group_separator "_" --chunk_separator "|"
```

ma_thaung_chunk5.txt:  

```
ပန်း|သည်|မ|သောင်း|က_အ|သက်|က|၁|၆|နှစ်
၊_ယဉ်|စ_စ|နဲ့|နု|ပျို|မှု_ခြင်း|မှာ|မ|သိန်း|ထက်_အ
ပုံ|ကြီး_သာ|သ|ပေါ့_။|ဒီ_တော့_တက္က_သိုလ်_ကျောင်း_သား_တွေ|က|ပန်း|သည်|မ|သောင်း
ဆိုင်|မှာ|ပြောင်း|ပြီး|ပန်း|ဝယ်|ကြ_၊|စ|ကား|တွေ
ဖောင်|ဖွဲ့|ကြ_တာ_ပေါ့|။|မ|သိန်း|ပန်း|ဆိုင်_အ_ရင်_လို_မ_ရောင်း_ရ|တော့|ဘဲ
ခြောက်|ကပ်_လာ_တာ_ပေါ့_။_ဒီ|လို|နဲ့|တ|နေ့|သူ့|ပန်း|ဆိုင်|နား
ကို|လင်|မ_ယား_နှစ်_ယောက်_က_လေး_လေး|လက်|ဆွဲ_ပြီး_ရောက်_လာ|။_အ_မျိုး_သား_ဖြစ်|သူ|က|တပ်|ထား
တဲ့|မျက်|မှန်|ချွတ်|လိုက်|ပြီး|ကျ|နော့်|မှတ်|မိ
လား|မေး|။|မောင်|သိန်း|ခိုင်|ဖြစ်|နေ|။|ပန်း
သည်|မ|သိန်း_နဲ့_ယော_ကျ်ား_ဖြစ်|သူ|ကို|သိန်း|ခိုင်|တို့_စ_ကား|တွေ|တ
ရင်း|တ|နှီး|ဖောင်|ဖွဲ့|နေ_ကြ|တာ_ကြ|ည့်|ပြီး_ဇ_နီး_ဖြစ်_သူ|က
အံ့|တွေ|သြ|။|သိပ္ပံ|မောင်|ဝ_က_ဒီ|မှာ|တင်|ပန်း
သည်|စာ|မူ|ကို_ရပ်|ခဲ့|တယ်_။

```
