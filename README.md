# sentiment_analysis_bot

- This is a twitter bot which performs sentiment analysis on tweets and replies with the type of review that is either positive or negative also with variability.
- To use, reply to a tweet by @AnalyseBot and within a minute the bot will reply.

### Note:
It performs faster by using pickling.
Since featuresets.pickle came out about 300MB, have not included in repo.
Dont forget to create using:
```
featuresets = [(find_features(rev), category) for (rev, category) in documents]
```
