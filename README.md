# SENTIMENT ANALYSIS BOT
- This is a twitter bot which performs sentiment analysis on tweets and replies with either a positive/negative or a variable review.
- To use, reply to any tweet by @AnalyseBot and within a minute, the bot will reply.

### Note:
It performs faster by using pickling.
Since featuresets.pickle came out to be about 300MB, So, it is not included in repo.
Dont forget to create using:
```
featuresets = [(find_features(rev), category) for (rev, category) in documents]
```
