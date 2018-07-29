import numpy as np
import os

def load_embedding(embedding_dir):

    word2id_file = os.path.join(embedding_dir,'word2id.npy')
    word2id = np.load(word2id_file)

    phase_embedding_file = os.path.join(embedding_dir,'phase_embedding.npy')
    amplitude_embedding_file = os.path.join(embedding_dir,'amplitude_embedding.npy')
    phase_embedding = np.load(phase_embedding_file)
    amplitude_embedding = np.load(amplitude_embedding_file)
    return(word2id, phase_embedding, amplitude_embedding)


embedding_dir = 'eval/eval_CR_mixture/embedding'
word2id, phase_embedding, amplitude_embedding = load_embedding(embedding_dir)
print(word2id)
print(phase_embedding)
print(amplitude_embedding)
print('ABC'.lower())
