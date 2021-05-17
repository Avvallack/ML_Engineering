docker run -v $(pwd)/data:/home/starspace_worker/data task_1 \
starspace train -trainFile ./data/starspace_train.txt -model ./data/modelSaveFile -trainMode 0 -minCount 100 -ngrams 3 -label __hub__
