
from chain import MarkovChain
from nltk.corpus import gutenberg


# creating the chain 
# 1st order -> 0
mc = MarkovChain(0)

# train
# download nltk and change path accordingly
# any text file can be used to train the chain
corpora_path = '/usr/local/share/nltk_data/corpora/gutenberg/'

for filename in gutenberg.fileids():
    print(corpora_path+str(filename))
    try:
        mc.train(corpora_path+str(filename))
    except (UnicodeDecodeError):
        pass
    

# testing
# print(mc.chain)
# print(mc.find_next_state('it')) #first order
# print(mc.find_next_state('gain'))

    
# convert to json and save to file
mc.to_json('markov_chain_1st_order.json')



