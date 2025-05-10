# Analysis-of-Indian-Food-Cuisine-Dataset

# 🍛 Indian Cuisine Analysis

This repository presents a comprehensive analysis of an Indian Cuisine Dataset. The goal is to extract meaningful
insights into dish characteristics, cuisine patterns, ratings, and cooking efforts using Python data science tools.

---

## 📊 Features

- Load and clean a real-world Excel dataset of Indian dishes
- Analyze:
  - Missing values
  - Vegetarian vs Non-Vegetarian dishes
  - Cuisine-specific filtering (e.g., North Indian)
  - Top-rated dishes
  - Dishes filtered by course (main dish, side dish, etc.)
  - Time-based metrics: preparation, cooking, total time
- Ingredient-based search (e.g., dishes with garlic)
- Save filtered datasets as Excel files
- Visualizations:
  - Bar charts, pie charts, scatter plots, box plots, heatmaps
  - Effort vs Rating Analysis
  - Dashboard with multi-plot summary
- Outlier detection (IQR method)
- Summary metrics by cuisine and course type
- Recommendations: Best cuisines based on high rating + low effort

---

## 📁 Dataset

- Format: Excel `.xlsx`
- Filename: `Indain_Food_Cuisine_Dataset.xlsx`
- Columns include:
  - Name of dish
  - Ingredients
  - Course name
  - Cuisine type
  - Ratings
  - Diet type
  - Preparation/Cooking/Total time

---

## 🛠️ Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/Mohammed-Saleh-Ishaq/Analysis-of-Indian-Food-Cuisine-Dataset.git

   Once cloned, navigate into the directory using:

   cd Analysis-of-Indian-Food-Cuisine-Dataset

2. Install required packages :

```bash
   pip install pandas matplotlib seaborn missingno openpyxl

3. Add the dataset:

   - Place Indain_Food_Cuisine_Dataset.xlsx in the root folder of the project.


