import numpy as np

# lendo os dados do dataset
data = open('data/dataset.txt', 'r').read()
chars = list(set(data))
data_size, vocab_size = len(data), len(chars)

print('data has %d characters, %d unique.' % (data_size, vocab_size))

char_to_ix = { ch:i for i,ch in enumerate(chars) }
ix_to_char = { i:ch for i,ch in enumerate(chars) }

# Hiperparametros
hidden_size = 100
seq_length = 25
learning_rate = 1e-1