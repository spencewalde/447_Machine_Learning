import pylab as pl
import numpy as np
import pcn2
import pickle, gzip

# Read the dataset in (code from sheet)
f = gzip.open('/Users/swald/OneDrive - MNSCU/447 MACHINELEARNING/Python_Module3/mnist.pkl.gz','rb')
u=pickle._Unpickler(f)
u.encoding='latin1'
tset, vset, teset = u.load()
f.close()

nread = 200
# Just use the first few images
train_in = tset[0][:nread,:]

# This is a little bit of work -- 1 of N encoding
# Make sure you understand how it does it
train_tgt = np.zeros((nread,10))
for i in range(nread):
    train_tgt[i,tset[1][i]] = 1

test_in = teset[0][:nread,:]
test_tgt = np.zeros((nread,10))
for i in range(nread):
    test_tgt[i,teset[1][i]] = 1

# Train a Perceptron on training set
p = pcn2.pcn2(train_in, train_tgt)
p.pcntrain(train_in, train_tgt,.25,100)

# This isn't really good practice since it's on the training data, 
# but it does show that it is learning.
p.confmat(train_in,train_tgt)

# Now test it
p.confmat(test_in,test_tgt)


# /Users/swald/OneDrive - MNSCU/447 MACHINELEARNING/Python_Module3/mnist.pkl.gz