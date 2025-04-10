Description: Markov Chain implementation for next word prediction.
             Trained for 1st, 2nd and 3rd order chains.
"""
from string import punctuation
from numpy.random import choice
import json

class MarkovChain(object):
    
    def __init__(self, order, chain={}):
        self.chain = chain 
        self.order = order
        
    def train(self, filename):
      
        words = self.get_input_fron_file(filename)
        self.update_Markov_chain(words)
        
    def get_input_fron_file(self,filename):
        words = [] 
        with open(filename) as f:        
            for word in f.read().split():
                pure_word = self.strip_punctuation(word)
                words.append(pure_word.lower())
        return words
    
    def strip_punctuation(self,s):
        
        return ''.join(c for c in s if c not in punctuation)
        
    def update_Markov_chain(self, words): 
        index = 0
        for word in words[:len(words)-self.order-1]:
            state = ' '.join(words[index:index + self.order+1])
            next_state = words[index + self.order + 1] 
            index += 1 
        
            if state not in self.chain:
                self.chain[state] = {}
        
            if next_state not in self.chain[state]:
                self.chain[state][next_state] = 0
            
            self.chain[state][next_state] += 1
    
        
            
    def find_next_state(self,state):
        
        state = self.strip_punctuation(state)
        if state not in self.chain.keys():
            # word has never been encountered in training
            return None
        else:            
            choices = list(self.chain[state].keys())
            weights = list(self.chain[state].values())
            # find propabilities from weights
            sum = self.calc_sum(weights)
            # -Debug- print(sum)
            prob = []
            for w in weights:
                prob.append(float(w)/sum)
            # -Debug- print(prob)
            return choice(choices,p=prob)
        
    def calc_sum(self,listarray):
        
        sum = 0.0
        for x in listarray:
            sum += x
        return sum
 
    # JSON methods
    
    def to_json(self, filename):
      
           with open(filename,'w') as f:
            json.dump(self.to_json_serializible(),f)
        
    def to_json_serializible(self):
        
        return {
                "order":self.order,
                "markov_chain":json.dumps(self.chain, sort_keys=True)
                }
     
    @classmethod
    def from_json(cls, filename):
      
        
        with open(filename) as f:
            data = json.load(f)
        order = data['order']
        chain = json.loads(data['markov_chain'])
        obtained_chain = cls(order,chain)        
        return obtained_chain
    
