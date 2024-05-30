import os

class PreProcessor:
    
    def __init__(self, dataset_id: int, output_dir: str):
        self.dataset_id = dataset_id
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def start(self):
        structured_corpus = []
        
        if self.dataset_id == 1:
            print('structuring dataset 1..')
            import ds1_prep
            structured_corpus = ds1_prep.start()
            
        else:
            print('structuring dataset 2..')
            import ds2_prep
            structured_corpus = ds2_prep.start()

        return structured_corpus

