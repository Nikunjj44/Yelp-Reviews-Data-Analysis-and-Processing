import pandas as pd

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

# Function to load datasets of a metropolitan city

def load_datasets(business_path, review_path):
    df_business = pd.read_csv(business_path)
    df_business = df_business.drop(columns = ["index"])
    
    df_reviews = pd.read_csv(review_path)
    df_reviews = df_reviews.drop(columns = ["index"])

    return df_business, df_reviews


# Function to get business name and give filtered list of reviews

def get_review_for_business(df_business, df_review, business_name):
    error = False
    if business_name in df_business["name"].tolist():
        business_id = df_business.loc[df_business["name"] == business_name, "business_id"].iloc[0]
        df_review_filtered = df_review[df_review["business_id"] == business_id].reset_index(drop = True)
        
        print(f"Found {len(df_review_filtered)} reviews for {business_name}")

        df = df_review_filtered
    else:
        print(f"{business_name} not present in dataset")
        df    = "Error" 
        error = True
    return df, error
# Function to detect and generate negation results

def generate_negation_results(df, negation_words):
    
    result = []
    for i, row in df.iterrows():
        text = row["text"]
    
        # Dividing each review into sentences
        sentence = sent_tokenize(text)
        for s in sentence:
            words = word_tokenize(s)
    
            # Finding negation words
            neg_word = []
            for w in words:
                if w in negation_words:
                    neg_word.append(w)
    
            if len(neg_word) > 0:
                result.append({
                    "review_id" : row["review_id"],
                    "user_id"   : row["user_id"],
                    "stars"     : row["stars"],
                    "sentence"  : s,
                    "neg_count" : len(neg_word),
                    "neg_words" : neg_word
                })

    return result

# Function to analyse negation results

def analyse_negation(business_name, df, result):
    
    print(f"Business Name: {business_name}")

    avg_stars = round(df["stars"].mean(),2)
    print(f"Average star rating: {avg_stars}\n")
    
    total_reviews = len(df["review_id"].unique().tolist())
    print(f"Total reviews analysed: {total_reviews}")
    
    neg_reviews = len(set(row["review_id"] for row in result))
    print(f"Reviews with negation: {neg_reviews}")
    
    sen_neg = len(result)
    print(f"Sentences with negation: {sen_neg}")
    
    words_neg = sum(row["neg_count"] for row in result)
    print(f"Total negation words: {words_neg}")
    
    print("\n")
    print("Most frequent negation words: ")
    
    neg_words = []
    for row in result:
        for w in row["neg_words"]:
            neg_words.append(w)
    
    for word, freq in Counter(neg_words).most_common():
        print(f"{word} : {freq}")
    
    print("\n")
    print("Some sentences with negation words: ")
    i = 1
    for row in result[:3]:
        print(f'{i}. \"{row["sentence"]}\" (negation words: {", ".join(row["neg_words"])})')
        i = i + 1


def main():
    business_name_ip = input("Enter the business name: ")
    try:
        df_business, df_reviews = load_datasets(business_path = "business_new_orleans.csv", review_path = "review_new_orleans.csv")
    
        df_business_reviews, b_error = get_review_for_business(df_business = df_business, df_review = df_reviews, business_name = business_name_ip)

        if not b_error:
            negation_words = [
            "no", "not", "never", "none", "nobody", "nothing", "neither", "nowhere", "hardly", "scarcely", "barely", "rarely", "seldom", "dont", 
            "doesn't", "didn't", "won't", "wouldn't", "shouldn't", "cannot", "can't", "couldn't", "isn't", "aren't", "wasn't", "weren't", "hasn't", 
            "haven't", "hadn't"]
            
            negation_result = generate_negation_results(df = df_business_reviews, negation_words = negation_words)

            analyse_negation(business_name = business_name_ip, df = df_business_reviews, result = negation_result)
    except Exception as e:
        print(f"An error occurred: {e}")
        
    
if __name__ == "__main__":
    main()


