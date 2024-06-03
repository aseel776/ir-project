def get_reciprocal_rank(retrieved_ids, relevant_ids):
    
    # rr = (1 / rank in retrieved ids) for the first relevant id in retrieved docs
    
    for rank, doc_id in enumerate(retrieved_ids, start=1):
        if doc_id in relevant_ids:
            return 1 / rank
    return 0

def get_mrr(rrs: list):
    if not rrs:
        return 0
    return sum(rrs) / len(rrs)