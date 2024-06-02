import ir_datasets

# query<query_id, text>
# doc<doc_id, text, title>
dataset_test_1 = ir_datasets.load('beir/scifact/train')
dataset_test_1_test = ir_datasets.load('beir/scifact/test')


# query<query_id, text>
# doc<doc_id, text>
dataset_test_2 = ir_datasets.load('beir/quora/dev')
dataset_test_2_test = ir_datasets.load('beir/quora/test')


# query<query_id, url, domain, title, text, sentence_annotations>
# doc<doc_id, page_title, wikidata_id, wikidata_classes, text, sections, infoboxes>
dataset_1 = ir_datasets.load('trec-tot/2023/train')
dataset_1_test = ir_datasets.load('trec-tot/2023/dev')


# query<query_id, text>
# doc<doc_id, text>
dataset_2 = ir_datasets.load('wikir/en1k/training')
dataset_2_test = ir_datasets.load('wikir/en1k/test')
dataset_2_validation = ir_datasets.load('wikir/en1k/validation')