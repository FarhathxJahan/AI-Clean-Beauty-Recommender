import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# FILE LOADING
# =========================

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "clean_beauty_final.csv")

df = pd.read_csv(DATA_PATH)

# =========================
# DATA CLEANING
# =========================

df["rating"] = df["rating"].fillna(0)
df["clean_score"] = df["clean_score"].fillna(0)
df["recommendation_score"] = df["recommendation_score"].fillna(0)
df["irritant_count"] = df["irritant_count"].fillna(0)

# =========================
# ML SCORING LOGIC
# =========================

df["final_score"] = (
    df["clean_score"] * 0.4
    + df["recommendation_score"] * 0.3
    + df["rating"] * 10 * 0.2
    - df["irritant_count"] * 2
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Clean Beauty Recommender",
    layout="wide"
)

# =========================
# TITLE
# =========================

st.title("💄 AI Clean Beauty Recommender")
st.write(
    "Find clean, safe, and personalized skincare recommendations using AI-inspired scoring."
)

# =========================
# SIDEBAR FILTERS
# =========================

st.sidebar.header("Filters")

category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(
        df["secondary_category"].dropna().unique().tolist()
    )
)

skin_type = st.sidebar.selectbox(
    "Skin Type",
    [
        "All",
        "Dry Skin",
        "Oily / Acne-Prone",
        "Sensitive Skin",
        "All Skin Types"
    ]
)

acne_safe = st.sidebar.selectbox(
    "Acne Safe?",
    ["All", "Yes", "No"]
)

fragrance_free = st.sidebar.selectbox(
    "Fragrance Free?",
    ["All", "Yes", "No"]
)

search = st.sidebar.text_input(
    "Search Product"
)

top_n = st.sidebar.slider(
    "Number of Results",
    3,
    15,
    5
)

# =========================
# FILTERING LOGIC
# =========================

filtered = df.copy()

if category != "All":
    filtered = filtered[
        filtered["secondary_category"] == category
    ]

if skin_type != "All":
    filtered = filtered[
        filtered["skin_type_match"].str.contains(
            skin_type,
            na=False
        )
    ]

if acne_safe != "All":
    filtered = filtered[
        filtered["acne_prone_safe"] == acne_safe
    ]

if fragrance_free != "All":
    filtered = filtered[
        filtered["fragrance_free"] == fragrance_free
    ]

if search:
    filtered = filtered[
        filtered["product_name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# =========================
# SORT PRODUCTS
# =========================

filtered = filtered.sort_values(
    by="final_score",
    ascending=False
)

results = filtered.head(top_n)

# =========================
# RECOMMENDATIONS
# =========================

st.subheader("🏆 Top Recommended Products")

if results.empty:

    st.warning(
        "No products found. Try different filters."
    )

else:

    for _, row in results.iterrows():

        st.markdown("---")

        st.subheader(row["product_name"])

        st.write(
            f"**Brand:** {row['brand_name']}"
        )

        st.write(
            f"**Category:** {row['secondary_category']}"
        )

        st.write(
            f"⭐ Rating: {row['rating']}"
        )

        st.write(
            f"🧪 Clean Score: {row['clean_score']}"
        )

        st.write(
            f"⚠ Irritant Count: {row['irritant_count']}"
        )

        st.write(
            f"🤖 Final Recommendation Score: {round(row['final_score'],2)}"
        )

        st.info(
            f"""
Why this product is recommended:

✔ High clean score: {row['clean_score']}

✔ Matches your selected filters

✔ Low irritant level

✔ Good balance of safety, quality and rating

✔ Ranked using AI-inspired scoring logic
"""
        )

# =========================
# DASHBOARD SECTION
# =========================

st.markdown("---")
st.header("📊 Dataset Analytics Dashboard")

# =========================
# CHART 1
# =========================

st.subheader("Product Category Distribution")

category_counts = (
    df["secondary_category"]
    .value_counts()
)

st.bar_chart(category_counts)

# =========================
# CHART 2
# =========================

st.subheader("Clean Score Distribution")

fig1, ax1 = plt.subplots()

ax1.hist(
    df["clean_score"],
    bins=20
)

ax1.set_xlabel("Clean Score")
ax1.set_ylabel("Frequency")
ax1.set_title("Distribution of Clean Scores")

st.pyplot(fig1)

# =========================
# CHART 3
# =========================

st.subheader("Rating vs Clean Score")

fig2, ax2 = plt.subplots()

ax2.scatter(
    df["rating"],
    df["clean_score"]
)

ax2.set_xlabel("Rating")
ax2.set_ylabel("Clean Score")
ax2.set_title("Rating vs Clean Score")

st.pyplot(fig2)

# =========================
# CHART 4
# =========================

st.subheader("Irritant Level Distribution")

irritant_counts = (
    df["irritant_count"]
    .value_counts()
    .sort_index()
)

st.bar_chart(irritant_counts)

# =========================
# PROJECT STATS
# =========================

st.markdown("---")
st.header("📈 Dataset Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Products",
    len(df)
)

col2.metric(
    "Categories",
    df["secondary_category"].nunique()
)

col3.metric(
    "Average Rating",
    round(df["rating"].mean(), 2)
)

col4.metric(
    "Average Clean Score",
    round(df["clean_score"].mean(), 2)
)

st.success("AI Clean Beauty Recommender Successfully Running")
