def get_precision_at_k(retrieved_ids, relevant_ids, k):

    # get top k retrieved
    retrieved_at_k = retrieved_ids[:k]
    
    # get (Tp in k)
    relevant_and_retrieved = [id for id in retrieved_at_k if id in relevant_ids]
    
    # P = (Tp in k) / k
    precision = len(relevant_and_retrieved) / k
    
    return precision

def get_avg_precision(precisions: list):
    if not precisions:
        return 0.0
    return sum(precisions) / len(precisions)
