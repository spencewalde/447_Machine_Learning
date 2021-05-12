import numpy as np
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
targets = np.array([[0], [1], [1], [1]])
import pcn_logic_eg
p=pcn_logic_eg.pcn(inputs, targets)
p.pcntrain(inputs, targets, .25,25)
# Add the inputs that match the bias node
# def linearregression(inputs,targets):
#     inputs_bias = np.concatenate((inputs,-np.ones((np.shape(inputs)[0],1))),axis=1)
#     p.pcnfwd(inputs_bias)

#     beta = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(inputs),inputs)),np.transpose(inputs)),targets)
#     outputs = np.dot(inputs,beta)
#     return outputs


la = linearregression(inputs,targets)
print(la)
# write short script to compute the result of [1,0]
# new_inputs = np.array([0,0, -1])
# outputs=p.pcnfwd(new_inputs)
# print(outputs)