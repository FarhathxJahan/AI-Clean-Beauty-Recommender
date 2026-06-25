# Project Story

## Problem Statement

The skincare industry contains thousands of products, making it difficult for consumers to identify products that are safe, effective, and suitable for their skin type. Many users struggle to understand ingredient lists, compare products, and evaluate safety-related factors such as irritants and clean beauty standards.

## Why This Problem Matters

Consumers increasingly seek clean beauty products that align with their skincare goals and personal values. However, finding suitable products often requires extensive research and technical knowledge about ingredients.

Many users experience confusion due to:

* Large numbers of available products
* Complex ingredient lists
* Marketing claims that are difficult to verify
* Limited knowledge of ingredient safety
* Difficulty finding alternatives to existing products

As a result, consumers may spend significant time and money experimenting with products that may not meet their needs.

## Proposed Solution

The AI Clean Beauty Recommender was developed to simplify the product discovery process. The system analyzes product ingredients and quality-related features to recommend products that closely match user preferences.

Users can:

* Search for products
* Filter products by category
* Select skin type preferences
* Identify acne-safe and fragrance-free options
* Receive intelligent recommendations based on product similarity

## Machine Learning Approach

The project uses a Hybrid Content-Based Recommendation System.

The recommendation engine combines:

1. TF-IDF Vectorization of product ingredients
2. Cosine Similarity for ingredient comparison
3. Numerical similarity based on clean score, recommendation score, rating, and irritant count

The hybrid model generates recommendations by combining ingredient-based similarity and numerical feature similarity, resulting in more accurate and meaningful product suggestions.

## Results Achieved

The final system successfully:

* Processes skincare product information
* Identifies similar products using machine learning techniques
* Generates personalized recommendations
* Provides filtering based on user preferences
* Visualizes important skincare dataset insights
* Delivers recommendations through a deployed Streamlit application

The project demonstrates how machine learning can be applied to solve real-world consumer decision-making challenges while promoting informed and safer skincare choices.

## Conclusion

The AI Clean Beauty Recommender bridges the gap between skincare data and consumer decision-making. By combining ingredient analysis, product quality metrics, and machine learning techniques, the project helps users discover products that better align with their skincare needs and preferences.
