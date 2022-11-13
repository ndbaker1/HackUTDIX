import os

from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

from itertools import chain
import requests

nebula_url = 'api.utdnebula.com'
apikey = os.environ['NEBULA_KEY']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)



def fetch_class_data(class_id: str):
    return requests.get(
        f'https://{nebula_url}/course/{class_id}',
        headers={ 'x-api-key': apikey },
    ).json()['data']

def fetch_class_ids(page: int):
    class_id_iter = list()

    class_id_iter = chain(
        class_id_iter,
        map(
            lambda e: e['_id'],
            requests.get(
                f'https://{nebula_url}/course?subject_prefix=CS&offset={page}',
                headers={ 'x-api-key': apikey },
            ).json()['data']
        )
    ) 
    
    return class_id_iter

def encode_text(text_description: str):
    # Tokenize sentences
    encoded_input = tokenizer([text_description], padding=True, truncation=True, return_tensors='pt')

    # Compute token embeddings
    with torch.no_grad():
        model_output = model(**encoded_input)

    # Perform pooling
    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

    # Normalize embeddings
    sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)

    return sentence_embeddings[0]

def compute_similarity(search, class_id_to_descriptor: dict):
    similarities = [(class_id, F.cosine_similarity(search, c, dim=0)) for (class_id, c) in class_id_to_descriptor.items()]
    return sorted(similarities, key=lambda s: s[1])