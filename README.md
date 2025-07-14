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
   ```
   Once cloned, navigate into the directory using:
   ```bash

   cd Analysis-of-Indian-Food-Cuisine-Dataset
   ```

3. Install required packages :

```bash
   pip install pandas matplotlib seaborn missingno openpyxl
   ```
3. Add the dataset:

   - Place Indain_Food_Cuisine_Dataset.xlsx in the root folder of the project.

---


## 🚀 Run the Analysis

Execute the Python script:

```bash

python indian_cuisine_analysis.py

```

The script will:
   1. Print insights to the console
   2. Save filtered data as Excel files
   3. Show multiple interactive plots
   
---
## 📈 Sample Visuals

  1. Pie chart of diet types
     ![Pie_chart _Figure_3](https://github.com/user-attachments/assets/84ecceea-42c4-41e8-bbaf-931223491fe1)
---
  2. Bar plots of top cuisines
     ![Bar Chart _Figure_2](https://github.com/user-attachments/assets/f9aa2a87-88b4-4176-ab82-d236859e3cd5)

---

  3. Dashboard summary (4-in-1 chart)
     ![Bar plot_Figure_11](https://github.com/user-attachments/assets/4297ac82-0279-4595-88bc-e8aaf6ce1a36)


---

## 🧠 Insights & Recommendations

   --> 1. Cuisines with high average ratings and low average effort.
   --> 2. Best course types for ease or quality.
   --> 3. Outliers in time-based metrics.
    4. Heatmap of correlation between time and ratings.

---

## 📤 Output Files
    --> 1. vegetarian_dishes.xlsx.
    --> 2. top_rated_dishes.xlsx.
    --> 3. Indain_Food_Cuisine_Dataset.xlsx.

---

## ✅ Requirements
    
     -->  1. python
     -->  2. Libraries: panda , seaborn , Matplotlib , missingno , openpyxl , Vscode.

---
