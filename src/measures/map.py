from measures.precision import get_precision_at_k

def get_ap_at_k(retrieved_ids, relevant_ids, k):
    
    # AP@k = SUM( Precision@k for each relevant id at k rank ) / Tp 

    # tp counter
    relevant_and_retrieved = 0

    # sum for precisions
    precision_sum = 0
    
    # Iterate through each rank up to k
    for i in range(1, k + 1):
        if retrieved_ids[i - 1] in relevant_ids:
            relevant_and_retrieved += 1
            precision_sum += get_precision_at_k(retrieved_ids, relevant_ids, i)
    
    if relevant_and_retrieved == 0:
        return 0.0
    
    ap = precision_sum / relevant_and_retrieved

    return ap

def get_map(aps: list):
    if not aps:
        return 0.0
    return sum(aps) / len(aps)