import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# --------------------- Load Dataset ---------------------
# Load the data from the Excel sheet
df = pd.read_excel(r'C:\Users\hutaz\Desktop\final try 4\Indain_Food_Cuisine_Dataset.xlsx')

# Normalize column names for consistency
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# Display the first few rows of the DataFrame to ensure it loaded correctly
print(df.head())

# --------------------- Question 1: Checking for Null Values ---------------------
print("\nChecking for null values in the data:")
print(df.isnull().sum())

# Visualize missing data
import missingno as msno
msno.heatmap(df, figsize=(10, 6), cmap="viridis")
plt.title("Missing Data Heatmap")
plt.show()

# --------------------- Question 2: Filtering Vegetarian Dishes ---------------------
def filter_vegetarian_dishes(df):
    return df[df['diet_type'].str.contains("vegetarian", na=False, case=False)]

vegetarian_dishes = filter_vegetarian_dishes(df)
print("\nVegetarian Dishes:")
print(vegetarian_dishes[['name_of_dish', 'diet_type', 'course_name', 'cuisine_name']])

# --------------------- Question 3: Filtering Dishes by Cuisine ---------------------
def filter_by_cuisine(df, cuisine):
    return df[df['cuisine_name'].str.contains(cuisine, na=False, case=False)]

north_indian_dishes = filter_by_cuisine(df, 'north indian')
print("\nNorth Indian Dishes:")
print(north_indian_dishes[['name_of_dish', 'diet_type', 'course_name', 'cuisine_name']])

# --------------------- Question 4: Filtering Top-Rated Dishes ---------------------
df['ratings_of_dish'] = pd.to_numeric(df['ratings_of_dish'], errors='coerce')

def top_rated_dishes(df, min_rating=4.5):
    return df[df['ratings_of_dish'] >= min_rating]

top_rated = top_rated_dishes(df)
print("\nTop Rated Dishes:")
print(top_rated[['name_of_dish', 'ratings_of_dish', 'cuisine_name', 'course_name']])

# --------------------- Question 5: Filtering Dishes by Course Type ---------------------
def filter_by_course(df, course_name):
    return df[df['course_name'].str.contains(course_name, na=False, case=False)]

side_dishes = filter_by_course(df, 'side dish')
print("\nSide Dishes:")
print(side_dishes[['name_of_dish', 'course_name', 'cuisine_name']])

# --------------------- Question 6: Calculating Average Times ---------------------
def extract_minutes(time_str):
    match = re.search(r"(\d+)", str(time_str))
    return int(match.group(1)) if match else 0

time_cols = ['prepration_time', 'cooking_time', 'total_time']
for col in time_cols:
    df[f"{col}_minutes"] = df[col].apply(extract_minutes)

avg_prep = df['prepration_time_minutes'].mean()
avg_cook = df['cooking_time_minutes'].mean()
avg_total = df['total_time_minutes'].mean()

print(f"\nAverage Preparation Time: {avg_prep:.2f} minutes")
print(f"Average Cooking Time: {avg_cook:.2f} minutes")
print(f"Average Total Time: {avg_total:.2f} minutes")

# --------------------- Question 7: Searching for Dishes by Ingredient ---------------------
def search_by_ingredient(df, ingredient):
    return df[df['ingredients_of_dish'].str.contains(ingredient, na=False, case=False)]

garlic_dishes = search_by_ingredient(df, 'garlic')
print("\nDishes containing Garlic:")
print(garlic_dishes[['name_of_dish', 'ingredients_of_dish', 'cuisine_name']])

# --------------------- Question 8: Saving Filtered Data ---------------------
vegetarian_dishes.to_excel('vegetarian_dishes.xlsx', index=False)
top_rated.to_excel('top_rated_dishes.xlsx', index=False)
print("\nFiltered data has been saved to 'vegetarian_dishes.xlsx' and 'top_rated_dishes.xlsx'.")

# --------------------- Data Visualization ---------------------
sns.set_style("whitegrid")

# Bar Chart: Count of Dishes by Cuisine
plt.figure(figsize=(10, 6))
cuisine_counts = df['cuisine_name'].value_counts().head(10)
sns.barplot(x=cuisine_counts.index, y=cuisine_counts.values, palette='viridis')
plt.title('Top 10 Cuisines with Most Dishes')
plt.xlabel('Cuisine')
plt.ylabel('Number of Dishes')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#----------------------------------------2nd pie chart ----------------------------------------------------------------------

# Assuming the DataFrame `df` is already loaded and has a column named 'diet_type'


# Calculate value counts for diet types
diet_counts = df['diet_type'].value_counts()

# Create the pie chart
plt.figure(figsize=(12, 8))  # Larger figure size
colors = sns.color_palette('Set3', len(diet_counts))

# Adjust labeldistance and autopct for better spacing
def custom_autopct(pct):
    """Only display percentages greater than 1% or show 'small' for tiny slices."""
    return ('%1.1f%%' % pct) if pct > 1 else ''

wedges, texts, autotexts = plt.pie(
    diet_counts,
    labels=None,  # Remove direct labels from the chart to avoid overlap
    autopct=custom_autopct,  # Custom function to handle small percentages
    colors=colors,
    startangle=90,
    wedgeprops={'edgecolor': 'black'},
    pctdistance=0.85  # Move percentage text closer to the center
)

# Title
plt.title('Distribution of Dishes by Diet Type', fontsize=16)

# Add a custom legend instead of directly labeling
legend_labels = [f'{label} ({pct:.1f}%)' for label, pct in zip(diet_counts.index, diet_counts / diet_counts.sum() * 100)]
plt.legend(
    wedges,  # Use wedges to display colors in the legend
    legend_labels,
    title="Diet Type",
    loc="center left", 
    bbox_to_anchor=(1.1, 0.5),  # Place the legend to the right
    fontsize=10,
    frameon=True
)

# Draw a circle at the center to make it a donut chart (optional)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)

# Tight layout to prevent overlap
plt.tight_layout()

# Show the chart
plt.show()


# Scatter Plot: Relationship Between Preparation Time, Cooking Time, and Ratings

plt.figure(figsize=(10, 6))
sns.scatterplot(x='prepration_time_minutes', y='cooking_time_minutes', size='ratings_of_dish',
                hue='cuisine_name', data=df, alpha=0.7, sizes=(20, 200))
plt.title("Relationship Between Preparation Time, Cooking Time, and Ratings")
plt.xlabel("Preparation Time (minutes)")
plt.ylabel("Cooking Time (minutes)")
plt.legend(bbox_to_anchor=(1.05, 1), title="Cuisine")
plt.tight_layout()
plt.show()

print(df.columns)


#-----------------------------------------

# Detecting outliers using the IQR method
def detect_outliers(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return series[(series < lower_bound) | (series > upper_bound)]

# Detect outliers in time columns
outliers_prep = detect_outliers(df['prepration_time_minutes'])
outliers_cook = detect_outliers(df['cooking_time_minutes'])

print("\nOutliers in Preparation Time:")
print(outliers_prep)

print("\nOutliers in Cooking Time:")
print(outliers_cook)

# Visualize outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['prepration_time_minutes', 'cooking_time_minutes']])
plt.title("Box Plot of Preparation and Cooking Times")
plt.show()

#=============================

# Correlation analysis
correlation_matrix = df[['prepration_time_minutes', 'cooking_time_minutes', 'total_time_minutes', 'ratings_of_dish']].corr()

# Heatmap visualization
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

## Effort Score

# Effort Score = preparation time + cooking time
df['effort_score'] = df['prepration_time_minutes'] + df['cooking_time_minutes']

# Scatter plot to analyze Effort Score vs Ratings
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='effort_score', y='ratings_of_dish', hue='cuisine_name', alpha=0.7)
plt.title("Effort Score vs Ratings")
plt.xlabel("Effort Score")
plt.ylabel("Ratings")
plt.legend(bbox_to_anchor=(1.05, 1), title="Cuisine")
plt.tight_layout()
plt.show()

df.to_excel('enhanced_indian_cuisine_dataset.xlsx', index=False)
print("Enhanced dataset has been saved as 'enhanced_indian_cuisine_dataset.xlsx'.")

# Average Ratings and Effort by Cuisine
# Group by cuisine and calculate averages
cuisine_summary = df.groupby('cuisine_name').agg({
    'ratings_of_dish': 'mean',
    'effort_score': 'mean',
    'total_time_minutes': 'mean',
    'name_of_dish': 'count'
}).rename(columns={
    'ratings_of_dish': 'avg_rating',
    'effort_score': 'avg_effort',
    'total_time_minutes': 'avg_total_time',
    'name_of_dish': 'dish_count'
}).sort_values(by='avg_rating', ascending=False)

print("\nCuisine-wise Summary:")
print(cuisine_summary.head(10))

#-> Bar Plot: Top Cuisines by Average Rating

top_cuisines_by_rating = cuisine_summary.sort_values('avg_rating', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_cuisines_by_rating, x=top_cuisines_by_rating.index, y='avg_rating', palette='mako')
plt.xticks(rotation=45, ha='right')
plt.title("Top 10 Cuisines by Average Dish Rating")
plt.ylabel("Average Rating")
plt.xlabel("Cuisine")
plt.tight_layout()
plt.show()

#----Heatmap: Cuisine vs Average Metrics
plt.figure(figsize=(10, 6))
sns.heatmap(cuisine_summary[['avg_rating', 'avg_effort', 'avg_total_time']], annot=True, cmap="YlGnBu", fmt=".1f")
plt.title("Cuisine-wise Averages: Rating, Effort, Total Time")
plt.tight_layout()
plt.show()

course_summary = df.groupby('course_name').agg({
    'ratings_of_dish': 'mean',
    'effort_score': 'mean',
    'total_time_minutes': 'mean',
    'name_of_dish': 'count'
}).rename(columns={
    'ratings_of_dish': 'avg_rating',
    'effort_score': 'avg_effort',
    'total_time_minutes': 'avg_total_time',
    'name_of_dish': 'dish_count'
}).sort_values(by='avg_rating', ascending=False)

print("\nCourse-wise Summary:")
print(course_summary.head())

#1. Which cuisines offer high ratings with low effort?
# Define high rating and low effort thresholds
high_rating_threshold = 4.2
low_effort_threshold = 5  

# Filter cuisines that meet both criteria
efficient_cuisines = cuisine_summary[
    (cuisine_summary['avg_rating'] >= high_rating_threshold) &
    (cuisine_summary['avg_effort'] <= low_effort_threshold)
].sort_values(by='avg_rating', ascending=False)

print("\nCuisines with High Ratings and Low Effort:")
print(efficient_cuisines)

#2. Top courses by rating or effort

# Top 5 easy courses (lowest effort)
top_easy_courses = course_summary.sort_values('avg_effort').head(5)
print("\nTop 5 Course Types by Ease (Lowest Avg Effort):")
print(top_easy_courses)

# Top 5 courses by rating
top_rated_courses = course_summary.sort_values('avg_rating', ascending=False).head(5)
print("\nTop 5 Course Types by Rating:")
print(top_rated_courses)

#3. Visual: Effort vs Rating Scatter Plot by Cuisine

plt.figure(figsize=(10, 6))
sns.scatterplot(data=cuisine_summary, x='avg_effort', y='avg_rating', size='dish_count', hue=cuisine_summary.index, legend=False, palette='tab10')
plt.axhline(high_rating_threshold, color='green', linestyle='--', label='High Rating Threshold')
plt.axvline(low_effort_threshold, color='red', linestyle='--', label='Low Effort Threshold')
plt.title("Cuisine: Avg Effort vs Avg Rating")
plt.xlabel("Average Effort Score")
plt.ylabel("Average Rating")
plt.legend()
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle("Dashboard Summary of Indian Food Dataset", fontsize=18)

# 1. Top 10 Cuisines by Average Rating
top_rated_cuisines = cuisine_summary.sort_values('avg_rating', ascending=False).head(10)
sns.barplot(x=top_rated_cuisines['avg_rating'], y=top_rated_cuisines.index, ax=axes[0, 0], palette='coolwarm')
axes[0, 0].set_title('Top 10 Cuisines by Avg Rating')
axes[0, 0].set_xlabel('Average Rating')

# 2. Top 10 Easiest Cuisines (Lowest Avg Effort)
easiest_cuisines = cuisine_summary.sort_values('avg_effort').head(10)
sns.barplot(x=easiest_cuisines['avg_effort'], y=easiest_cuisines.index, ax=axes[0, 1], palette='Greens')
axes[0, 1].set_title('Top 10 Easiest Cuisines')
axes[0, 1].set_xlabel('Average Effort Score')

# 3. Scatter: Effort vs Rating by Cuisine
sns.scatterplot(data=cuisine_summary, x='avg_effort', y='avg_rating', size='dish_count',
                ax=axes[1, 0], hue=cuisine_summary.index, palette='tab20', legend=False)
axes[1, 0].axhline(4.2, color='green', linestyle='--')
axes[1, 0].axvline(5, color='red', linestyle='--')
axes[1, 0].set_title('Effort vs Rating (by Cuisine)')
axes[1, 0].set_xlabel('Average Effort')
axes[1, 0].set_ylabel('Average Rating')

# 4. Top Courses by Average Rating
top_courses = course_summary.sort_values('avg_rating', ascending=False).head(5)
sns.barplot(x=top_courses['avg_rating'], y=top_courses.index, ax=axes[1, 1], palette='Blues_r')
axes[1, 1].set_title('Top Course Types by Rating')
axes[1, 1].set_xlabel('Average Rating')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Top 5 cuisines that are both highly rated and require low effort
recommendations = cuisine_summary[
    (cuisine_summary['avg_rating'] >= 4.2) & 
    (cuisine_summary['avg_effort'] <= 5)
].sort_values('avg_rating', ascending=False)
