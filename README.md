# Yelp Reviews Data Analysis and Processing

This project aims to cover some components of end-to-end text data management and processing applications. The components covered in this repository are Data Analysis, CLI Application for Sentiment Analysis and Negation Detection. 

Yelp is an online platform that connects businesses with its customers. Yelp Open Dataset is a large collection of data that is readily available for public use. This contains real-world business data, user profiles and reviews shared by users over various metropolitan areas. With it being available to the public and vast size and attributes of the data, it is widely used for review data analysis and processing.

## Methodology
1. **Data Sampling**  
   Yelp’s Open Dataset includes reviews from multiple metropolitan areas. So, sampling is done on businesses and reviews datasets on one metropolitan area. To choose a metropolitan area, the business dataset is processed. After analyzing this dataset, some discrepancies like “Reno” and “reno” being the same city but accounting for different number of reviews are identified. Therefore, case folding is performed on this column and all of the city names are converted into lowercase to standardize them.
   <img width="465" height="211" alt="image" src="https://github.com/user-attachments/assets/dcf81e58-6979-4421-98f2-5c8db2128567" />  
   Only the top 7 cities with the most reviews are analyzed because a bigger set of reviews would provide more meaningful insights. It can also be seen that New Orleans has a high mean and standard deviation of review counts. Furthermore, New Orleans also has the second highest total number of reviews. This shows that New Orleans provides a large and diverse dataset enabling us to find meaningful insights and identify real-world applicable patterns.
   
2. **Data Analysis**  
   The filtered dataset after choosing New Orleans as the city of focus is analyzed and a summary of statistics is generated. Alongside this heatmaps of the businesses in New Orleans are also generated to get insights based on geographic context. Furthermore tokenization and stemming is performed. Two stemming algorithms namely Porter stemming and Lancaster stemming are evaluated along side results when no stemming is applied.

3. **Negation Detection**  
   A command-line interface (CLI) application is developed for detecting negations. The applications aims detect negations in reviews of a particular business. Post detecting negations, the application provides statistics including average star ratings, count of reviews containing negations, total negation words found, most frequent negation terms, and sample sentences with negations that can help the business and customers viewing the business to better understand critical feedback and areas of concern expressed by the reviewers.

5. **Sentiment Analysis**  
   A command-line interface (CLI) application is developed for performing sentiment analysis on business reviews. The application aims to analyze customer sentiments for a particular business in New Orleans by processing their reviews using VADER sentiment analysis. Post analyzing the sentiments, the application provides statistics including an overall sentiment classification (Positive/Neutral/Negative), average sentiment score, and sentiment distribution that can help the business and potential customers better understand the general customer satisfaction and opinions expressed by the reviewers.

## Future Scope

The CLI applications can further be improved by converting it into a web-based application with the help of Streamlit. Along side this the Sentiment Analysis and Negation Detection applications can be integrated together in order to draw more meaningful and impactful insights.

## Usage
**Note for current/future NTU students:** While this repository is public, please ensure you adhere to NTU's Academic Integrity Policy. This is intended as a reference for my personal portfolio; using this code for your own graded assignments is strictly prohibited by the University.
