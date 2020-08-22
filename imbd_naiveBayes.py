import pandas as pd
import numpy as np
import config

from sklearn import naive_bayes
from sklearn import metrics
#from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection

from sklearn import decomposition

from nltk import word_tokenize

if __name__ == "__main__":
    df = pd.read_csv(config.input_data, nrows=1000)

    df = df.sample(frac=1).reset_index(drop=True)    

    df.sentiment = df.sentiment.apply(
        lambda x: 1 if x == "positive" else 0
    )

    kf = model_selection.StratifiedKFold(n_splits=5)    
    
    for f, idx in enumerate(kf.split(X=df.loc[:, 'review'], y=df.sentiment)):
        print(f)
        train_idx, test_idx = idx[0], idx[1]
        
        train_df = df.iloc[train_idx]
        test_df = df.iloc[test_idx]

        cvs = TfidfVectorizer(tokenizer=word_tokenize, token_pattern=None, ngram_range=(1, 3))
        cvs.fit(train_df.review)

        xtrain = cvs.transform(train_df.review)
        xtest = cvs.transform(test_df.review)

        svd = decomposition.NMF(n_components=30)

        svd.fit(X=xtrain)

        xtrain_svd = svd.transform(xtrain)
        xtest_svd = svd.transform(xtest)

        model = naive_bayes.MultinomialNB()

        model.fit(X=xtrain_svd, y=train_df.sentiment)

        ypred = model.predict(xtest_svd)

        acc = metrics.accuracy_score(test_df.sentiment, ypred)

        print(acc)