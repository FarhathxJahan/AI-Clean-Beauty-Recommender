# Methodology

## Data Collection

The dataset was collected from Kaggle using Sephora skincare product data.

The dataset includes:

- Product Name
- Brand Name
- Ingredients
- Ratings
- Reviews
- Categories
- Product Highlights

---

## Data Cleaning

The following preprocessing steps were performed:

- Removed duplicate products
- Handled missing values
- Standardized ingredient lists
- Converted ingredient text into structured format
- Cleaned category information
- Normalized product attributes

---

## Feature Engineering

Several custom features were created:

### Clean Score

Measures how free a product is from potentially harmful ingredients.

### Recommendation Score

Combines:

- Product cleanliness
- User ratings
- Product reviews

### Irritant Count

Counts detected potentially irritating ingredients.

### Fragrance Free

Flags products that do not contain fragrance.

### Acne Prone Safe

Identifies products suitable for acne-prone skin.

### Skin Type Match

Assigns products to:

- Dry Skin
- Sensitive Skin
- Oily / Acne-Prone
- All Skin Types

### Best For

Maps products to major concerns:

- Acne
- Dryness
- Anti-Aging
- Oil Control
- General Care

---

## Recommendation Logic

Products are filtered using:

- Category
- Skin Type
- Acne Safety
- Fragrance Preference

Products are then ranked using a weighted scoring system.
