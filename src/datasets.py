import ir_datasets

# query<query_id, text>
# doc<doc_id, text, title>
dataset_test_1 = ir_datasets.load('beir/scifact/train')


# query<query_id, text>
# doc<doc_id, text>
dataset_test_2 = ir_datasets.load('beir/quora/dev')


# query<query_id, url, domain, title, text, sentence_annotations>
# doc<doc_id, page_title, wikidata_id, wikidata_classes, text, sections, infoboxes>
dataset_1 = ir_datasets.load('trec-tot/2023/train')


# query<query_id, text>
# doc<doc_id, text>
dataset_2 = ir_datasets.load('wikir/en1k/training')