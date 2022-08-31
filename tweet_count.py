import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter


st.title("Counts of Tweets by Stock Symbol")
st.subheader("Enter stock symbol to return amount of mentions in the last week")

stock = st.text_input("Ex: $TESLA")

tweets_list = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper('$AMD since:2022-08-30 until:2022-08-31').get_items()):
    tweets_list.append([tweet.date, tweet.content])

st.write(len(tweets_list))