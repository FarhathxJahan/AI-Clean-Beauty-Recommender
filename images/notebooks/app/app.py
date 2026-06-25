import streamlit as st
import pandas as pd
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
# RECOMMENDATION SCORING
# =========================
df["final_score"] = (
    df["clean_score"] * 0.4 +
    df["recommendation_score"] * 0.3 +
    df["rating"] * 10 * 0.2 -
    df["irritant_count"] * 2
)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Clean Beauty Recommender",
    layout="wide"
)

st.title("💄 AI Clean Beauty Recommender")
st.write("Find clean, safe and personalized skincare recommendations.")

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
# FILTERING
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
# SORT RESULTS
# =========================
filtered = filtered.sort_values(
    by="final_score",
    ascending=False
)

results = filtered.head(top_n)

# =========================
# RESULTS
# =========================
st.subheader("Top Recommended Products")

if results.empty:
    st.warning(
        "No products found. Try different filters."
    )
else:
    for _, row in results.iterrows():

        st.markdown("---")

        st.subheader(row["product_name"])

        st.write(
            "**Brand:**",
            row["brand_name"]
        )

        st.write(
            "**Category:**",
            row["secondary_category"]
        )

        st.write(
            "⭐ Rating:",
            row["rating"]
        )

        st.write(
            "🧪 Clean Score:",
            row["clean_score"]
        )

        st.write(
            "⚠ Irritant Count:",
            row["irritant_count"]
        )

        st.info(
            f"""
            Why this product is recommended:

            ✔ High clean score: {row['clean_score']}

            ✔ Matches your selected filters

            ✔ Lower irritant count

            ✔ Balanced recommendation score
            """
        )
