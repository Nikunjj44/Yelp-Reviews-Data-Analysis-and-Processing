import pandas as pd

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import ssl
import certifi
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

import nltk
#nltk.download('vader_lexicon')

# Function to load datasets of a metropolitan city

def load_datasets(business_path, review_path):
    df_business = pd.read_csv(business_path)
    df_business = df_business.drop(columns = ["index"])
    
    df_reviews = pd.read_csv(review_path)
    df_reviews = df_reviews.drop(columns = ["index"])

    return df_business, df_reviews


# Function to get business name and give filtered list of reviews

def get_review_for_business(df_business, df_review, business_name):
    if business_name in df_business["name"].tolist():
        business_id = df_business.loc[df_business["name"] == business_name, "business_id"].iloc[0]
        df_review_filtered = df_review[df_review["business_id"] == business_id].reset_index(drop = True)
        
        print(f"Found {len(df_review_filtered)} reviews for {business_name}")

        return df_review_filtered
    else:
        print(f"{business_name} not present in dataset")


def review_sentiment_analysis(df, business_name):
    # Sentiment Processing
    sentiment_analyzer = SentimentIntensityAnalyzer()

    df["sentiment"] = df["text"].apply(lambda x: sentiment_analyzer.polarity_scores(x)["compound"])
    df["sentiment_label"] = df["sentiment"].apply(
        lambda x: "Positive" if x > 0.5 else ("Negative" if x < 0 else "Neutral")
    )
    
    # Analysis
    avg_sentiment_score = round(df["sentiment"].mean(), 2)

    if avg_sentiment_score > 0.5:
        sentiment_label = "Positive"
    elif ((avg_sentiment_score > 0) & (avg_sentiment_score < 0.5)):
        sentiment_label = "Neutral"
    else:
        sentiment_label = "Negative"

    print(f"Overall Sentiment of {business_name} is {sentiment_label}")
    print(f"Average Sentimet Score (ranging from -1 to 1): {avg_sentiment_score}")
    print(f"Sentiment Distribution is as follows: ")
    print(df["sentiment_label"].value_counts().to_string(index=True, header=False))
    
    return df


def main():
    business_name_ip = input("Enter the business name: ")
    try:
        df_business, df_reviews = load_datasets(business_path = "business_new_orleans.csv", review_path = "review_new_orleans.csv")
    
        df_business_reviews = get_review_for_business(df_business = df_business, df_review = df_reviews, business_name = business_name_ip)

        review_sentiment_analysis(df = df_business_reviews, business_name = business_name_ip)
    except Exception as e:
        print(f"An error occurred: {e}")
        
    
if __name__ == "__main__":
    main()


