SUPPORTED_METRICS = ['verbmem_f', 'privleak', 'knowmem_f', 'knowmem_r']

CORPORA = ['news', 'books']

LLAMA_DIR = "meta-llama/Llama-2-7b-hf"

DEFAULT_DATA = {
    'news': {
        'verbmem_forget_file': "/lus/eagle/projects/PBML/yingdan/data/news/verbmem/forget.json",
        'privleak_forget_file': "/lus/eagle/projects/PBML/yingdan/data/news/privleak/forget.json",
        'privleak_retain_file': "/lus/eagle/projects/PBML/yingdan/data/news/privleak/retain.json",
        'privleak_holdout_file': "/lus/eagle/projects/PBML/yingdan/data/news/privleak/holdout.json",
        'knowmem_forget_qa_file': "/lus/eagle/projects/PBML/yingdan/data/news/knowmem/forget_qa.json",
        'knowmem_forget_qa_icl_file': "/lus/eagle/projects/PBML/yingdan/data/news/knowmem/forget_qa_icl.json",
        'knowmem_retain_qa_file': "/lus/eagle/projects/PBML/yingdan/data/news/knowmem/retain_qa.json",
        'knowmem_retain_qa_icl_file': "/lus/eagle/projects/PBML/yingdan/data/news/knowmem/retain_qa_icl.json",
    },
    'books': {
        'verbmem_forget_file': "/lus/eagle/projects/PBML/yingdan/data/books/verbmem/forget.json",
        'privleak_forget_file': "/lus/eagle/projects/PBML/yingdan/data/books/privleak/forget.json",
        'privleak_retain_file': "/lus/eagle/projects/PBML/yingdan/data/books/privleak/retain.json",
        'privleak_holdout_file': "/lus/eagle/projects/PBML/yingdan/data/books/privleak/holdout.json",
        'knowmem_forget_qa_file': "/lus/eagle/projects/PBML/yingdan/data/books/knowmem/forget_qa.json",
        'knowmem_forget_qa_icl_file': "/lus/eagle/projects/PBML/yingdan/data/books/knowmem/forget_qa_icl.json",
        'knowmem_retain_qa_file': "/lus/eagle/projects/PBML/yingdan/data/books/knowmem/retain_qa.json",
        'knowmem_retain_qa_icl_file': "/lus/eagle/projects/PBML/yingdan/data/books/knowmem/retain_qa_icl.json",
    }
}

AUC_RETRAIN = {
    'news': {
        "forget_forget_PPL": 0.5,
        "forget_forget_PPL/ref": 0.5,
        "forget_forget_PPL/lower": 0.5,
        "forget_forget_PPL/zlib": 0.5,
        "forget_forget_Min-5%": 0.5,
        "forget_forget_Min-10%": 0.5,
        "forget_forget_Min-20%": 0.5,
        "forget_forget_Min-30%": 0.5,
        "forget_forget_Min-40%": 0.5,
        "forget_forget_Min-50%": 0.5,
        "forget_forget_Min-60%": 0.5,
        "forget_retain_PPL": 0.9682000000000001,
        "forget_retain_PPL/ref": 0.9875,
        "forget_retain_PPL/lower": 0.9266999999999999,
        "forget_retain_PPL/zlib": 0.9677999999999999,
        "forget_retain_Min-5%": 0.9686999999999999,
        "forget_retain_Min-10%": 0.9716,
        "forget_retain_Min-20%": 0.9705,
        "forget_retain_Min-30%": 0.9689,
        "forget_retain_Min-40%": 0.9689000000000001,
        "forget_retain_Min-50%": 0.9676000000000001,
        "forget_retain_Min-60%": 0.9683,
        "forget_holdout_PPL": 0.4652,
        "forget_holdout_PPL/ref": 0.27549999999999997,
        "forget_holdout_PPL/lower": 0.3542,
        "forget_holdout_PPL/zlib": 0.43279999999999996,
        "forget_holdout_Min-5%": 0.5116,
        "forget_holdout_Min-10%": 0.5021,
        "forget_holdout_Min-20%": 0.49310000000000004,
        "forget_holdout_Min-30%": 0.48399999999999993,
        "forget_holdout_Min-40%": 0.47719999999999996,
        "forget_holdout_Min-50%": 0.4711,
        "forget_holdout_Min-60%": 0.4671,
        "retain_forget_PPL": 0.031800000000000016,
        "retain_forget_PPL/ref": 0.012500000000000011,
        "retain_forget_PPL/lower": 0.0733,
        "retain_forget_PPL/zlib": 0.03220000000000002,
        "retain_forget_Min-5%": 0.03130000000000001,
        "retain_forget_Min-10%": 0.028400000000000016,
        "retain_forget_Min-20%": 0.029500000000000023,
        "retain_forget_Min-30%": 0.031100000000000023,
        "retain_forget_Min-40%": 0.031100000000000017,
        "retain_forget_Min-50%": 0.03240000000000001,
        "retain_forget_Min-60%": 0.03170000000000002,
        "retain_retain_PPL": 0.5,
        "retain_retain_PPL/ref": 0.5,
        "retain_retain_PPL/lower": 0.5,
        "retain_retain_PPL/zlib": 0.5,
        "retain_retain_Min-5%": 0.5,
        "retain_retain_Min-10%": 0.5,
        "retain_retain_Min-20%": 0.5,
        "retain_retain_Min-30%": 0.5,
        "retain_retain_Min-40%": 0.5,
        "retain_retain_Min-50%": 0.5,
        "retain_retain_Min-60%": 0.5,
        "retain_holdout_PPL": 0.03450000000000001,
        "retain_holdout_PPL/ref": 0.0047000000000000045,
        "retain_holdout_PPL/lower": 0.05150000000000001,
        "retain_holdout_PPL/zlib": 0.02910000000000002,
        "retain_holdout_Min-5%": 0.03360000000000001,
        "retain_holdout_Min-10%": 0.031100000000000017,
        "retain_holdout_Min-20%": 0.03240000000000002,
        "retain_holdout_Min-30%": 0.03230000000000002,
        "retain_holdout_Min-40%": 0.03200000000000002,
        "retain_holdout_Min-50%": 0.033000000000000015,
        "retain_holdout_Min-60%": 0.03360000000000001,
        "holdout_forget_PPL": 0.5348,
        "holdout_forget_PPL/ref": 0.7245,
        "holdout_forget_PPL/lower": 0.6458,
        "holdout_forget_PPL/zlib": 0.5672000000000001,
        "holdout_forget_Min-5%": 0.48839999999999995,
        "holdout_forget_Min-10%": 0.4979,
        "holdout_forget_Min-20%": 0.5069,
        "holdout_forget_Min-30%": 0.516,
        "holdout_forget_Min-40%": 0.5227999999999999,
        "holdout_forget_Min-50%": 0.5289,
        "holdout_forget_Min-60%": 0.5329,
        "holdout_retain_PPL": 0.9654999999999999,
        "holdout_retain_PPL/ref": 0.9953,
        "holdout_retain_PPL/lower": 0.9485,
        "holdout_retain_PPL/zlib": 0.9709,
        "holdout_retain_Min-5%": 0.9663999999999999,
        "holdout_retain_Min-10%": 0.9689,
        "holdout_retain_Min-20%": 0.9676,
        "holdout_retain_Min-30%": 0.9676999999999999,
        "holdout_retain_Min-40%": 0.9680000000000001,
        "holdout_retain_Min-50%": 0.9670000000000001,
        "holdout_retain_Min-60%": 0.9663999999999999,
        "holdout_holdout_PPL": 0.5,
        "holdout_holdout_PPL/ref": 0.5,
        "holdout_holdout_PPL/lower": 0.5,
        "holdout_holdout_PPL/zlib": 0.5,
        "holdout_holdout_Min-5%": 0.5,
        "holdout_holdout_Min-10%": 0.5,
        "holdout_holdout_Min-20%": 0.5,
        "holdout_holdout_Min-30%": 0.5,
        "holdout_holdout_Min-40%": 0.5,
        "holdout_holdout_Min-50%": 0.5,
        "holdout_holdout_Min-60%": 0.5
    },
    'books': {
        "forget_forget_PPL": 0.5,
        "forget_forget_PPL/ref": 0.5,
        "forget_forget_PPL/lower": 0.5,
        "forget_forget_PPL/zlib": 0.5,
        "forget_forget_Min-5%": 0.5,
        "forget_forget_Min-10%": 0.5,
        "forget_forget_Min-20%": 0.5,
        "forget_forget_Min-30%": 0.5,
        "forget_forget_Min-40%": 0.5,
        "forget_forget_Min-50%": 0.5,
        "forget_forget_Min-60%": 0.5,
        "forget_retain_PPL": 1,
        "forget_retain_PPL/ref": 1,
        "forget_retain_PPL/lower": 1,
        "forget_retain_PPL/zlib": 1,
        "forget_retain_Min-5%": 1,
        "forget_retain_Min-10%": 1,
        "forget_retain_Min-20%": 1,
        "forget_retain_Min-30%": 1,
        "forget_retain_Min-40%": 1,
        "forget_retain_Min-50%": 1,
        "forget_retain_Min-60%": 1,
        "forget_holdout_PPL": 0.4746,
        "forget_holdout_PPL/ref": 0.3403,
        "forget_holdout_PPL/lower": 0.39570000000000005,
        "forget_holdout_PPL/zlib": 0.27730000000000005,
        "forget_holdout_Min-5%": 0.5325000000000001,
        "forget_holdout_Min-10%": 0.5424000000000001,
        "forget_holdout_Min-20%": 0.5582,
        "forget_holdout_Min-30%": 0.557,
        "forget_holdout_Min-40%": 0.5392999999999999,
        "forget_holdout_Min-50%": 0.5167,
        "forget_holdout_Min-60%": 0.48410000000000003,
        "retain_forget_PPL": 0,
        "retain_forget_PPL/ref": 0,
        "retain_forget_PPL/lower": 0,
        "retain_forget_PPL/zlib": 0,
        "retain_forget_Min-5%": 0,
        "retain_forget_Min-10%": 0,
        "retain_forget_Min-20%": 0,
        "retain_forget_Min-30%": 0,
        "retain_forget_Min-40%": 0,
        "retain_forget_Min-50%": 0,
        "retain_forget_Min-60%": 0,
        "retain_retain_PPL": 0.5,
        "retain_retain_PPL/ref": 0.5,
        "retain_retain_PPL/lower": 0.5,
        "retain_retain_PPL/zlib": 0.5,
        "retain_retain_Min-5%": 0.5,
        "retain_retain_Min-10%": 0.5,
        "retain_retain_Min-20%": 0.5,
        "retain_retain_Min-30%": 0.5,
        "retain_retain_Min-40%": 0.5,
        "retain_retain_Min-50%": 0.5,
        "retain_retain_Min-60%": 0.5,
        "retain_holdout_PPL": 0,
        "retain_holdout_PPL/ref": 0,
        "retain_holdout_PPL/lower": 0,
        "retain_holdout_PPL/zlib": 0,
        "retain_holdout_Min-5%": 0,
        "retain_holdout_Min-10%": 0,
        "retain_holdout_Min-20%": 0,
        "retain_holdout_Min-30%": 0,
        "retain_holdout_Min-40%": 0,
        "retain_holdout_Min-50%": 0,
        "retain_holdout_Min-60%": 0,
        "holdout_forget_PPL": 0.5254,
        "holdout_forget_PPL/ref": 0.6597000000000001,
        "holdout_forget_PPL/lower": 0.6043000000000001,
        "holdout_forget_PPL/zlib": 0.7227,
        "holdout_forget_Min-5%": 0.46749999999999997,
        "holdout_forget_Min-10%": 0.45759999999999995,
        "holdout_forget_Min-20%": 0.44179999999999997,
        "holdout_forget_Min-30%": 0.443,
        "holdout_forget_Min-40%": 0.4607,
        "holdout_forget_Min-50%": 0.4833,
        "holdout_forget_Min-60%": 0.5159,
        "holdout_retain_PPL": 1,
        "holdout_retain_PPL/ref": 1,
        "holdout_retain_PPL/lower": 1,
        "holdout_retain_PPL/zlib": 1,
        "holdout_retain_Min-5%": 1,
        "holdout_retain_Min-10%": 1,
        "holdout_retain_Min-20%": 1,
        "holdout_retain_Min-30%": 1,
        "holdout_retain_Min-40%": 1,
        "holdout_retain_Min-50%": 1,
        "holdout_retain_Min-60%": 1,
        "holdout_holdout_PPL": 0.5,
        "holdout_holdout_PPL/ref": 0.5,
        "holdout_holdout_PPL/lower": 0.5,
        "holdout_holdout_PPL/zlib": 0.5,
        "holdout_holdout_Min-5%": 0.5,
        "holdout_holdout_Min-10%": 0.5,
        "holdout_holdout_Min-20%": 0.5,
        "holdout_holdout_Min-30%": 0.5,
        "holdout_holdout_Min-40%": 0.5,
        "holdout_holdout_Min-50%": 0.5,
        "holdout_holdout_Min-60%": 0.5
    }
}
