# Test Run with ma_thein.txt

ma_thein.txt ဖိုင်ထဲမှာက အောက်မှာ မြင်ရတဲ့အတိုင်း word segmentation မလုပ်ထားဘူး။ ပြီးတော့ blank line တချို့လည်း ပါဝင်ပါတယ်။  

```
(base) ye@lst-gpu-server-197:~/ye/exp/sem-chunk/4github$ cat ma_thein.txt
ရွှေတိဂုံဘုရား အနောက်ဘက်စောင်းတန်းမှာ မသိန်း ဆိုတဲ့ ပန်းသည်တယောက်ရှိတယ်။ ပန်းသည်မသိန်းပုံကို သိပ္ပံမောင်ဝ ရေးဖွဲခဲ့ပုံက …။

“မသိန်းသည် ပန်းသည်တို့အနက် အတော်ပင် ယဉ်စစ ရှိ၏။ အပြောလည်း ကောင်း၊ သဘောလည်း ကောင်း၊ အပြုအပြင်ကလည်း ကောင်း၊ သူ့မှာ အကောင်းချည်း စုနေလေတော့သည်။ သို့ဖြစ်သောကြောင့် တက္ကသိုလ်ကျောင်းသားတွေ သူ့ဆိုင်မှာချည်း ပန်းဝယ်ကြလေသည်။”

အဲ့ဒီခေတ်က တက္ကသိုလ်ကျောင်းသားတွေဟာ စနေ၊ တနင်္ဂနွေနေ့တွေမှာ အုပ်စုလိုက် ဘုရားတက်ပြီး မသိန်းဆိုင်က ပန်းတွေဝယ်၊ မသိန်းဆိုင်ရှေ့က ခုံမှာထိုင်ပြီး စကားတွေ ဖောင်ဖွဲ့ကြပါသတဲ့။

တချို့ရက်တွေဆို ရှေ့ကအဖွဲ့ ဖောင်ဖွဲ့နေတုန်း နောက်တဖွဲ့ရောက်လာလို့ မထချင် ထချင်နဲ့ နေရာဖယ်ပေးရဆိုပဲ။ ဒီထဲ မောင်သိန်းခိုင်ဆိုတဲ့ ကျောင်းသားကတော့ တကိုယ်တော်။

သူက မသိန်း ဆိုင်သိမ်းချိန်အထိနေပြီး ဆိုင်သိမ်းပြီးရင် အတူပြန်တဲ့ထိ မသိန်းနဲ့ ရင်းနှီးတယ်။ ဒီလိုနဲ့ ကျောင်းသားဟောင်းတွေက ကျောင်းပြီးသွားလို့ နေရပ်အသီသီးဆီ ဘဝခရီးချီတက်ကြ။

နောက် ကျောင်းသားအသစ်တွေ ရောက်လာပြီး မသိန်းဆိုင်မှာ ပန်းဝယ်ကြ၊ စကားတွေဖောင်ဖွဲ့ကြနဲ့။ ဆယ်စုနှစ် နှစ်ခုလောက်ရှိတော့ မသိန်းဆိုင်နားမှာ မသောင်း ပန်းဆိုင် ပေါ်လာ။
(base) ye@lst-gpu-server-197:~/ye/exp/sem-chunk/4github$
```

## Experiment-1

Experiment-1 setting က အောက်ပါအတိုင်း...  
Bash Filename: exp1.sh  

```bash
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

```

Running exp1.sh ...  

```
(base) ye@lst-gpu-server-197:~/ye/exp/sem-chunk/4github/exp1$ time ./exp1.sh | tee exp1.log
...
...
...
Chunk line #8
တယ်_။_ဒီ_လို_နဲ့_ကျောင်း_သား_ဟောင်း_တွေ_က_ကျောင်း_ပြီး_သွား_လို့_နေ_ရပ်_အ_သီ_သီး_ဆီ_ဘ_ဝ_ခ_ရီး|ချီ_တက်_ကြ|။_နောက်_ကျောင်း_သား_အ_သစ်_တွေ_ရောက်_လာ|ပြီး_မ_သိန်း|ဆိုင်_မှာ|ပန်း|ဝယ်|ကြ_၊_စ|ကား|တွေ
Chunk line #9
ဖောင်|ဖွဲ့|ကြ|နဲ့|။|ဆယ်_စု_နှစ်_နှစ်_ခု_လောက်_ရှိ_တော့_မ_သိန်း_ဆိုင်_နား|မှာ|မ|သောင်း|ပန်း
Chunk line #10
ဆိုင်_ပေါ်_လာ_။
Chunks saved to ./exp1/ma_thein.chunk5.txt

real    0m2.037s
user    0m4.363s
sys     0m3.650s

real    0m9.624s
user    0m21.594s
sys     0m18.364s
```

```
(base) ye@lst-gpu-server-197:~/ye/exp/sem-chunk/4github/exp1$ ls
ma_thein.chunk1.txt  ma_thein.chunk5.txt     tst1.distances-eg2.png  tst1.distances-eg4.png
ma_thein.chunk2.txt  tst1.distances-eg1.pdf  tst1.distances-eg3.pdf  tst1.distances-eg5.pdf
ma_thein.chunk3.txt  tst1.distances-eg1.png  tst1.distances-eg3.png  tst1.distances-eg5.png
ma_thein.chunk4.txt  tst1.distances-eg2.pdf  tst1.distances-eg4.pdf
(base) ye@lst-gpu-server-197:~/ye/exp/sem-chunk/4github/exp1$
```

## Check on Segmented Outputs

### Command no. 1

```bash
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thein.txt \
--graph_filename ./exp1/tst1.distances-eg1 --chunk_filename ./exp1/ma_thein.chunk1.txt  --apply_syllable_break \
--syllable_group_separator "_" --chunk_separator "|"

```

ma_thein.chunk1.txt:  

```
ရွှေတိဂုံဘုရားအ
နောက်ဘက်စောင်းတန်းမှာမ_သိန်းဆိုတဲ့ပန်းသည်တ_ယောက်ရှိတယ်။ပန်းသည်
မသိန်းပုံကိုသိပ္ပံမောင်_ဝရေးဖွဲခဲ့ပုံက
…။
“မသိန်းသည်ပန်းသည်
တို့အနက်အတော်ပင်_ယဉ်စစရှိ၏။_အပြောလည်းကောင်း၊သ_ဘောလည်းကောင်း၊အပြု_အပြင်ကလည်းကောင်း၊_သူ့မှာအကောင်းချည်းစု_နေလေတော့သည်။သို့_ဖြစ်သောကြောင့်တက္ကသိုလ်
ကျောင်းသားတွေသူ့ဆိုင်မှာ_ချည်းပန်းဝယ်ကြလေသည်_။”_အဲ့ဒီခေတ်ကတက္ကသိုလ်
ကျောင်းသားတွေဟာစနေ_၊တနင်္ဂနွေနေ့တွေ
မှာအုပ်စုလိုက်ဘုရား_တက်ပြီးမသိန်းဆိုင်က_ပန်းတွေဝယ်၊မသိန်း
ဆိုင်ရှေ့ကခုံမှာထိုင်_ပြီးစကားတွေဖောင်ဖွဲ့_ကြပါသတဲ့။_တချို့ရက်တွေဆိုရှေ့_ကအဖွဲ့ဖောင်ဖွဲ့နေ_တုန်းနောက်တဖွဲ့ရောက်လာ_လို့မထချင်ထချင်_နဲ့နေရာဖယ်ပေးရ_ဆိုပဲ။ဒီထဲမောင်_သိန်းခိုင်ဆိုတဲ့ကျောင်းသား
ကတော့တကိုယ်တော်။_သူကမသိန်းဆိုင်သိမ်း_ချိန်အထိနေပြီးဆိုင်_သိမ်းပြီးရင်အတူပြန်_တဲ့ထိမသိန်းနဲ့ရင်း_နှီးတယ်။ဒီလိုနဲ့
ကျောင်းသားဟောင်းတွေကကျောင်း
ပြီးသွားလို့နေရပ်အ
သီသီးဆီဘဝခ
ရီးချီတက်ကြ။_နောက်ကျောင်းသားအသစ်တွေ_ရောက်လာပြီးမသိန်းဆိုင်
မှာပန်းဝယ်ကြ၊စ_ကားတွေဖောင်ဖွဲ့ကြနဲ့_။ဆယ်စုနှစ်နှစ်ခု_လောက်ရှိတော့မသိန်းဆိုင်_နားမှာမသောင်းပန်းဆိုင်_ပေါ်လာ။
```

<p align="center">
<img src="https://github.com/ye-kyaw-thu/NgaPi/blob/main/test/exp1/tst1.distances-eg1.png" alt="tst1.distances-eg1.png" width="600"/>  
</p>  
<div align="center">
  Fig.1 Semantic Chunking Based on Cosine Distance of FastText Embeddings  
</div> 

### Command no.2

```bash
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thein.txt \
--graph_filename ./exp1/tst1.distances-eg2 --chunk_filename ./exp1/ma_thein.chunk2.txt --percentile_threshold 40 \
--apply_syllable_break --chunks_per_line 5 \
--syllable_group_separator "_" --chunk_separator "|"
```

ma_thein.chunk2.txt:  

```
ရွှေတိဂုံဘုရားအ|နောက်ဘက်စောင်းတန်းမှာမ|သိန်းဆိုတဲ့ပန်းသည်တ_ယောက်ရှိတယ်။ပန်းသည်|မသိန်းပုံကိုသိပ္ပံမောင်|ဝရေးဖွဲခဲ့ပုံက
…။|“မသိန်းသည်ပန်းသည်|တို့အနက်အတော်ပင်_ယဉ်စစရှိ၏။_အပြောလည်းကောင်း၊သ_ဘောလည်းကောင်း၊အပြု_အပြင်ကလည်းကောင်း၊|သူ့မှာအကောင်းချည်းစု_နေလေတော့သည်။သို့_ဖြစ်သောကြောင့်တက္ကသိုလ်|ကျောင်းသားတွေသူ့ဆိုင်မှာ_ချည်းပန်းဝယ်ကြလေသည်
။”|အဲ့ဒီခေတ်ကတက္ကသိုလ်|ကျောင်းသားတွေဟာစနေ|၊တနင်္ဂနွေနေ့တွေ|မှာအုပ်စုလိုက်ဘုရား
တက်ပြီးမသိန်းဆိုင်က|ပန်းတွေဝယ်၊မသိန်း|ဆိုင်ရှေ့ကခုံမှာထိုင်_ပြီးစကားတွေဖောင်ဖွဲ့_ကြပါသတဲ့။|တချို့ရက်တွေဆိုရှေ့_ကအဖွဲ့ဖောင်ဖွဲ့နေ_တုန်းနောက်တဖွဲ့ရောက်လာ|လို့မထချင်ထချင်
နဲ့နေရာဖယ်ပေးရ_ဆိုပဲ။ဒီထဲမောင်|သိန်းခိုင်ဆိုတဲ့ကျောင်းသား|ကတော့တကိုယ်တော်။_သူကမသိန်းဆိုင်သိမ်း_ချိန်အထိနေပြီးဆိုင်_သိမ်းပြီးရင်အတူပြန်_တဲ့ထိမသိန်းနဲ့ရင်း_နှီးတယ်။ဒီလိုနဲ့|ကျောင်းသားဟောင်းတွေကကျောင်း|ပြီးသွားလို့နေရပ်အ
သီသီးဆီဘဝခ|ရီးချီတက်ကြ။|နောက်ကျောင်းသားအသစ်တွေ_ရောက်လာပြီးမသိန်းဆိုင်|မှာပန်းဝယ်ကြ၊စ|ကားတွေဖောင်ဖွဲ့ကြနဲ့
။ဆယ်စုနှစ်နှစ်ခု_လောက်ရှိတော့မသိန်းဆိုင်_နားမှာမသောင်းပန်းဆိုင်_ပေါ်လာ။
```

<p align="center">
<img src="https://github.com/ye-kyaw-thu/NgaPi/blob/main/test/exp1/tst1.distances-eg2.png" alt="tst1.distances-eg2.png" width="600"/>  
</p>  
<div align="center">
  Fig.1 Semantic Chunking Based on Cosine Distance of FastText Embeddings  
</div> 

### Command no.3 

```bash
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thein.txt \
--graph_filename ./exp1/tst1.distances-eg3 --chunk_filename ./exp1/ma_thein.chunk3.txt --percentile_threshold 30 \
--y_upper_bound 0.5 --apply_syllable_break --chunks_per_line 5 \
--syllable_group_separator "_" --chunk_separator "|"

```

ma_thein.chunk3.txt:  

```
ရွှေတိဂုံဘုရားအ|နောက်ဘက်စောင်းတန်းမှာမ|သိန်းဆိုတဲ့ပန်းသည်တ_ယောက်ရှိတယ်။ပန်းသည်|မသိန်းပုံကိုသိပ္ပံမောင်|ဝရေးဖွဲခဲ့ပုံက
…။|“မသိန်းသည်ပန်းသည်|တို့အနက်အတော်ပင်_ယဉ်စစရှိ၏။_အပြောလည်းကောင်း၊သ_ဘောလည်းကောင်း၊အပြု_အပြင်ကလည်းကောင်း၊|သူ့မှာအကောင်းချည်းစု_နေလေတော့သည်။သို့_ဖြစ်သောကြောင့်တက္ကသိုလ်|ကျောင်းသားတွေသူ့ဆိုင်မှာ
ချည်းပန်းဝယ်ကြလေသည်|။”|အဲ့ဒီခေတ်ကတက္ကသိုလ်|ကျောင်းသားတွေဟာစနေ|၊တနင်္ဂနွေနေ့တွေ
မှာအုပ်စုလိုက်ဘုရား|တက်ပြီးမသိန်းဆိုင်က|ပန်းတွေဝယ်၊မသိန်း|ဆိုင်ရှေ့ကခုံမှာထိုင်|ပြီးစကားတွေဖောင်ဖွဲ့_ကြပါသတဲ့။
တချို့ရက်တွေဆိုရှေ့|ကအဖွဲ့ဖောင်ဖွဲ့နေ_တုန်းနောက်တဖွဲ့ရောက်လာ|လို့မထချင်ထချင်|နဲ့နေရာဖယ်ပေးရ|ဆိုပဲ။ဒီထဲမောင်
သိန်းခိုင်ဆိုတဲ့ကျောင်းသား|ကတော့တကိုယ်တော်။_သူကမသိန်းဆိုင်သိမ်း_ချိန်အထိနေပြီးဆိုင်_သိမ်းပြီးရင်အတူပြန်_တဲ့ထိမသိန်းနဲ့ရင်း|နှီးတယ်။ဒီလိုနဲ့|ကျောင်းသားဟောင်းတွေကကျောင်း|ပြီးသွားလို့နေရပ်အ
သီသီးဆီဘဝခ|ရီးချီတက်ကြ။|နောက်ကျောင်းသားအသစ်တွေ_ရောက်လာပြီးမသိန်းဆိုင်|မှာပန်းဝယ်ကြ၊စ|ကားတွေဖောင်ဖွဲ့ကြနဲ့
။ဆယ်စုနှစ်နှစ်ခု_လောက်ရှိတော့မသိန်းဆိုင်_နားမှာမသောင်းပန်းဆိုင်_ပေါ်လာ။

```

<p align="center">
<img src="https://github.com/ye-kyaw-thu/NgaPi/blob/main/test/exp1/tst1.distances-eg3.png" alt="tst1.distances-eg3.png" width="600"/>  
</p>  
<div align="center">
  Fig.1 Semantic Chunking Based on Cosine Distance of FastText Embeddings  
</div> 

### Command no.4 

```bash
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thein.txt \
--graph_filename ./exp1/tst1.distances-eg4 --chunk_filename ./exp1/ma_thein.chunk4.txt --percentile_threshold 70 \
--y_upper_bound 0.5 --syllable_group_length 5 --apply_syllable_break \
--chunks_per_line 10 --syllable_group_separator "_" --chunk_separator "|"

```

ma_thein.chunk4.txt:  

```
ရွှေတိဂုံဘုရား|အနောက်ဘက်စောင်းတန်း_မှာမသိန်းဆိုတဲ့_ပန်းသည်တယောက်ရှိ_တယ်။ပန်းသည်မ|သိန်းပုံကိုသိပ္ပံမောင်_ဝရေးဖွဲခဲ့ပုံ_က…။_“မသိန်းသည်ပန်း_သည်တို့အနက်အ_တော်ပင်ယဉ်စစ_ရှိ၏။အပြော_လည်းကောင်း၊သဘော_လည်းကောင်း၊အပြု_အပြင်ကလည်းကောင်း_၊သူ့မှာအကောင်း|ချည်းစုနေလေတော့|သည်။သို့ဖြစ်သော|ကြောင့်တက္ကသိုလ်ကျောင်း|သားတွေသူ့ဆိုင်မှာ_ချည်းပန်းဝယ်ကြလေ_သည်။”_အဲ့ဒီခေတ်ကတက္က_သိုလ်ကျောင်းသားတွေဟာ|စနေ၊တနင်္ဂ_နွေနေ့တွေမှာအုပ်_စုလိုက်ဘုရားတက်|ပြီးမသိန်းဆိုင်က_ပန်းတွေဝယ်၊မ_သိန်းဆိုင်ရှေ့ကခုံ_မှာထိုင်ပြီးစကား_တွေဖောင်ဖွဲ့ကြပါ_သတဲ့။_တချို့ရက်တွေဆို_ရှေ့ကအဖွဲ့ဖောင်_ဖွဲ့နေတုန်းနောက်တ_ဖွဲ့ရောက်လာလို့မ|ထချင်ထချင်နဲ့
နေရာဖယ်ပေးရ|ဆိုပဲ။ဒီထဲ_မောင်သိန်းခိုင်ဆိုတဲ့_ကျောင်းသားကတော့တ_ကိုယ်တော်။_သူကမသိန်းဆိုင်_သိမ်းချိန်အထိနေ_ပြီးဆိုင်သိမ်းပြီးရင်_အတူပြန်တဲ့ထိ_မသိန်းနဲ့ရင်းနှီး_တယ်။ဒီလိုနဲ့|ကျောင်းသားဟောင်းတွေက_ကျောင်းပြီးသွားလို့နေ|ရပ်အသီသီးဆီ_ဘဝခရီးချီ|တက်ကြ။|နောက်ကျောင်းသားအသစ်|တွေရောက်လာပြီးမ|သိန်းဆိုင်မှာပန်းဝယ်|ကြ၊စကားတွေ_ဖောင်ဖွဲ့ကြနဲ့။_ဆယ်စုနှစ်နှစ်ခု_လောက်ရှိတော့မသိန်း_ဆိုင်နားမှာမသောင်း_ပန်းဆိုင်ပေါ်လာ။
```

<p align="center">
<img src="https://github.com/ye-kyaw-thu/NgaPi/blob/main/test/exp1/tst1.distances-eg4.png" alt="tst1.distances-eg4.png" width="600"/>  
</p>  
<div align="center">
  Fig.1 Semantic Chunking Based on Cosine Distance of FastText Embeddings  
</div> 

### Command no. 5

```bash
time python ./ngapi.py --model ./model/myfasttext_v1.bin --input ./ma_thein.txt \
--graph_filename ./exp1/tst1.distances-eg5 --chunk_filename ./exp1/ma_thein.chunk5.txt --percentile_threshold 70 \
--y_upper_bound 0.1 --syllable_group_length 1 --apply_syllable_break \
--chunks_per_line 10 --syllable_group_separator "_" --chunk_separator "|"

```

```
'_တိုက်|ပွဲ|ဝင်|ခြင်|တွေ|'|နဲ့|စ|ကူ|တာ
ဗုံး|-|မော်_စ_ကို_အ_ထိ_ရောက်_နေ_တဲ့|ယူ|က_ရိန်း|ထောက်_လှမ်း|ရေး|ယူ|က_ရိန်း_လုံ_ခြုံ_ရေး|နဲ့
ထောက်_လှမ်း_ရေး_ဌာ_န|က_အေး_ဂျင့်_တွေ_ဟာ_စစ်_ပွဲ_မှာ_ပါ_ဝင်_တဲ့_ရု_ရှား_စစ်_တပ်|ထိပ်_ပိုင်း_အ_ရာ_ရှိ_တွေ_နဲ့_တ|ခြား|ထိပ်_ပိုင်း_အ_ရာ_ရှိ_တွေ_"_ဘယ်_နေ_ရာ_မှာ_ရှိ_နေ_ပါ_စေ_"_အဲ_ဒီ_သူ_တွေ_ကို_တိုက်_ခိုက်|နေ_ကြောင်း_အဲ_ဒီ_ဌာ_န_ထဲ_မှာ_ရှိ_တဲ့_ဘီ_ဘီ_စီ|ယူ|က_ရိန်း_ရဲ့_သ|တင်း|ရင်း_မြစ်
တွေ_က_အ_တည်_ပြု_ပြော_ပါ_တယ်_။_အဲ_ဒီ_နေ_ရာ_တွေ_ထဲ_မှာ_သိမ်း_ပိုက်_ခံ_ယူ|က|ရိန်း_နယ်|မြေ|တွေ|၊|ရု_ရှား_နဲ့_တ_ခြား_နိုင်_ငံ_ရပ်_ခြား_တွေ_ပါ_ဝင်_ပါ_တယ်|။|စ|ကူ_တာ_လေး_ထဲ_မှာ_ထည့်_ထား_ပုံ
ရ|တဲ့|ဗုံး|နဲ့|ရု_ရှား_ဒု_တိ_ယ_ဗိုလ်_ချုပ်|ကြီး|အစ်|ဂေါ|ကီ_လီ_လော့ဗ်|ကို_တိုက်_ခိုက်_သတ်_ဖြတ်_လိုက်_တာ_ဟာ_ပြီး_ခဲ့_တဲ့_လ_ပိုင်း_တွေ_အ
တွင်း|မှာ|မော့|ဆက်_အ_ဖွဲ့|က|ပေ|ဂျာ_တွေ|နဲ့|ဟစ်ဇ်|ဘို
လာ_တို့_ကို_တိုက်_ခိုက်|ပုံ|နဲ့|နှိုင်း|ယှ|ဥ်_နိုင်_တယ်_လို့|ယူ|က_ရိန်း_လုံ_ခြုံ_ရေး_ဌာ_န|(|Security
Service|of|Ukraine|-|SBU_)_က_အ_ရာ|ရှိ|ဟောင်း|အိုင်|ဗင်|စ
တု|ပက်ခ်_က_ပြော_ပါ_တယ်|။_"_သူ့_ကို_ပစ်_သတ်_မ|လား|၊|ဗုံး_နဲ့_တိုက်_ခိုက်_မ_လား|၊|အ|ဆိပ်|ပေး_မ_လား_ဆို_တာ_ကို
ယူ|က_ရိန်း_လျှို့_ဝှက်|ထောက်_လှမ်း_ရေး_ဌာ_န_က_ဆုံး_ဖြတ်|တာ_ပါ_"_လို့_သူ_က_ပြော_ပါ_တယ်_။_ဒီ_အ_ဖြစ်_နဲ့_ပတ်_သက်_ပြီး_ယူ|က|ရိန်း|အ_စိုး_ရ_အာ_ဏာ_ပိုင်_တွေ_က_တ_ရား_ဝင်_မှတ်_ချက်_ချ_တာ_မျိုး_မ_ရှိ_ပါ_ဘူး_။
```

<p align="center">
<img src="https://github.com/ye-kyaw-thu/NgaPi/blob/main/test/exp1/tst1.distances-eg5.png" alt="tst1.distances-eg5.png" width="600"/>  
</p>  
<div align="center">
  Fig.1 Semantic Chunking Based on Cosine Distance of FastText Embeddings  
</div> 
