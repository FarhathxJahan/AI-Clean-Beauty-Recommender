# Methodology

## 1. Data Collection

The dataset used in this project consists of skincare and beauty products along with their attributes such as product name, brand name, ingredients, ratings, clean score, recommendation score, irritant count, category, and skin type compatibility. The data serves as the foundation for generating personalized skincare recommendations.

## 2. Data Cleaning

Before building the recommendation system, the dataset was cleaned to improve data quality and consistency. Missing values in important numerical columns such as rating, clean score, recommendation score, and irritant count were replaced with default values. Missing ingredient information was also handled to prevent errors during text processing.

## 3. Feature Engineering

Relevant product attributes were selected to improve recommendation quality. Numerical features such as clean score, recommendation score, rating, and irritant count were prepared for similarity calculations. Ingredient lists were also extracted as text features because ingredients play a major role in determining skincare product similarity.

## 4. TF-IDF Vectorization

The ingredient lists were converted into numerical vectors using Term Frequency–Inverse Document Frequency (TF-IDF). This technique transforms ingredient text into machine-readable representations while giving more importance to unique and meaningful ingredients and reducing the impact of commonly occurring words.

## 5. Cosine Similarity

Cosine Similarity was used to measure how similar two products are based on their ingredient compositions. Products with similar ingredient profiles receive higher similarity scores, enabling the system to identify alternative products with comparable formulations.

## 6. Hybrid Recommendation Model

A hybrid recommendation approach was implemented by combining:

* Ingredient Similarity (TF-IDF + Cosine Similarity)
* Numerical Feature Similarity (Clean Score, Recommendation Score, Rating, and Irritant Count)

The final similarity score was calculated using weighted contributions:

* 60% Ingredient Similarity
* 40% Numerical Feature Similarity

This hybrid approach improves recommendation quality by considering both product formulation and product performance indicators.

## 7. Product Recommendation Generation

When a user searches for a product, the system identifies the most similar products using the hybrid similarity matrix. Recommendations are ranked according to similarity scores and filtered based on user-selected criteria such as category, skin type, acne safety, and fragrance-free preferences.

For users who do not search for a specific product, products are ranked using clean score, recommendation score, rating, and irritant count to provide high-quality recommendations.

## 8. Streamlit Deployment

The recommendation system was deployed using Streamlit. The application provides an interactive user interface where users can:

* Filter products by category
* Select skin type preferences
* Search for products
* View personalized recommendations
* Explore skincare analytics and visualizations

The deployed application allows users to discover clean and safe skincare products in a simple and user-friendly environment.

