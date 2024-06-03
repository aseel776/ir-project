def get_recall(retrieved_ids, relevant_ids):

    if not relevant_ids:
        return 0.0
    
    # get Tp
    relevant_and_retrieved = [id for id in retrieved_ids if id in relevant_ids]

    # recall = Tp / (Tp + Fn)
    recall = len(relevant_and_retrieved) / len(relevant_ids)
    
    return recall

def get_avg_recall(recalls: list):
    if not recalls:
        return 0.0
    return sum(recalls) / len(recalls)