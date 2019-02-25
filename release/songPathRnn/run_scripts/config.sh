#********************************************************************
#Source: https://github.com/rajarshd/ChainsofReasoning
#See Chains of Reasoning over Entities, Relations, and Text using Recurrent Neural Networks
#https://arxiv.org/abs/1607.01426
#**********************************************************************
#!/bin/bash
host=`hostname`
experiment_dir="../"		
output_dir="results"
experiment_file=$experiment_dir/0.txt
output_dir=$output_dir/lse
data_dir="../data/output/"
gpu_id=0
numEntityTypes=1
includeEntityTypes=1
includeEntity=1
numEpoch=20
numFeatureTemplates=3
rnnHidSize=100
relationEmbeddingDim=10
entityTypeEmbeddingDim=10
entityEmbeddingDim=50
relationVocabSize=10
entityVocabSize=30
entityTypeVocabSize=10
topK=2 #0 is max; 1 is top K , 2 is LogSumExp
K=5
regularize=0
learningRate=1e-3
learningRateDecay=0.0167 #(1/60)
l2=1e-3
rnnType='rnn' #rnn or lstm as of now
epsilon=1e-8 #epsilon for adam
gradClipNorm=5
gradientStepCounter=100000 #to print loss after gradient updates
saveFrequency=1
batchSize=128
useGradClip=1 # 0 == L2 regularization
# package_path='/home/rajarshi/ChainsofReasoning/model/?.lua'
useAdam=1
paramInit=0.1
evaluationFrequency=5
createExptDir=1 #make it 0 if you dont want to create a directory and only print stuff
useReLU=1
rnnInitialization=1
numLayers=1
useDropout=0
dropout=0.3
