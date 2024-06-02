def get_precision_at_k(retrieved_ids, relevant_ids, k):

    # get top k retrieved
    retrieved_at_k = retrieved_ids[:k]
    print(f'Retrieved at {k}')
    print(retrieved_at_k)
    
    # get (Tp in k)
    relevant_and_retrieved = [id for id in retrieved_at_k if id in relevant_ids]
    print('Relevant and Retrieved')
    print(relevant_and_retrieved)
    
    # P = (Tp in k) / k
    precision = len(relevant_and_retrieved) / k
    
    return precision
