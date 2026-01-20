# Excel to Pandas Cheat Sheet

A quick reference guide for business students transitioning from Excel to Python with Pandas.

---

## 📊 Basic Operations

| Excel | Pandas | Example |
|-------|--------|---------|
| Open file | `pd.read_csv()` | `df = pd.read_csv('data.csv')` |
| Save file | `.to_csv()` | `df.to_csv('output.csv', index=False)` |
| View data | Scroll | `df.head()` or `df.tail()` |
| File info | Properties | `df.info()` or `df.shape` |

---

## 🔢 Aggregate Functions

| Excel Formula | Pandas Method | Example |
|---------------|---------------|---------|
| `=SUM(A1:A10)` | `.sum()` | `df['Sales'].sum()` |
| `=AVERAGE(A1:A10)` | `.mean()` | `df['Sales'].mean()` |
| `=COUNT(A1:A10)` | `.count()` | `df['Sales'].count()` |
| `=MIN(A1:A10)` | `.min()` | `df['Sales'].min()` |
| `=MAX(A1:A10)` | `.max()` | `df['Sales'].max()` |
| `=MEDIAN(A1:A10)` | `.median()` | `df['Sales'].median()` |
| `=STDEV(A1:A10)` | `.std()` | `df['Sales'].std()` |

---

## 🎯 Conditional Functions

| Excel Formula | Pandas Equivalent | Example |
|---------------|-------------------|---------|
| `=SUMIF(A:A,"Laptop",B:B)` | Filter + sum | `df[df['Product']=='Laptop']['Sales'].sum()` |
| `=COUNTIF(A:A,">100")` | Filter + count | `df[df['Sales']>100].shape[0]` |
| `=AVERAGEIF(A:A,"North",B:B)` | Filter + mean | `df[df['Region']=='North']['Sales'].mean()` |
| `=IF(A1>100,"High","Low")` | `.apply()` or `np.where()` | `df['Category'] = df['Sales'].apply(lambda x: 'High' if x>100 else 'Low')` |

---

## 🔍 VLOOKUP & Data Joining

| Excel | Pandas | Example |
|-------|--------|---------|
| `=VLOOKUP(value, table, col, 0)` | `.merge()` | `df.merge(lookup_table, on='key', how='left')` |
| Multiple VLOOKUPs | Single merge | Automatically brings all columns |
| INDEX-MATCH | `.merge()` | Same as VLOOKUP but more powerful |

### Merge Types (Join Types)
- `how='left'` - Keep all rows from left table (like VLOOKUP)
- `how='right'` - Keep all rows from right table
- `how='inner'` - Keep only matching rows
- `how='outer'` - Keep all rows from both tables

---

## 📊 Pivot Tables & GroupBy

| Excel | Pandas | Example |
|-------|--------|---------|
| PivotTable | `.groupby()` | `df.groupby('Region')['Sales'].sum()` |
| Multiple aggregations | `.agg()` | `df.groupby('Product').agg({'Sales': ['sum','mean']})` |
| Pivot with rows & cols | `.pivot_table()` | `pd.pivot_table(df, values='Sales', index='Region', columns='Product')` |

### Common GroupBy Operations
```python
# Single aggregation
df.groupby('Category')['Sales'].sum()

# Multiple aggregations
df.groupby('Category').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Profit': 'sum'
})

# Group by multiple columns
df.groupby(['Region', 'Product'])['Sales'].sum()
```

---

## 🔧 Data Manipulation

| Excel | Pandas | Example |
|-------|--------|---------|
| Filter (Data → Filter) | Boolean indexing | `df[df['Sales'] > 1000]` |
| Sort | `.sort_values()` | `df.sort_values('Sales', ascending=False)` |
| Remove duplicates | `.drop_duplicates()` | `df.drop_duplicates(subset='Product')` |
| New calculated column | Formula → drag down | `df['Profit'] = df['Sales'] - df['Cost']` |
| Text functions | `.str` methods | `df['Upper'] = df['Name'].str.upper()` |

---

## 📅 Date Functions

| Excel | Pandas | Example |
|-------|--------|---------|
| `=YEAR(A1)` | `.dt.year` | `df['Year'] = df['Date'].dt.year` |
| `=MONTH(A1)` | `.dt.month` | `df['Month'] = df['Date'].dt.month` |
| `=DAY(A1)` | `.dt.day` | `df['Day'] = df['Date'].dt.day` |
| `=WEEKDAY(A1)` | `.dt.dayofweek` | `df['Weekday'] = df['Date'].dt.dayofweek` |
| `=TEXT(A1,"MMMM")` | `.dt.month_name()` | `df['MonthName'] = df['Date'].dt.month_name()` |
| `=QUARTER(A1)` | `.dt.quarter` | `df['Quarter'] = df['Date'].dt.quarter` |

**Important**: First convert to datetime: `df['Date'] = pd.to_datetime(df['Date'])`

---

## 📈 Charts & Visualization

| Excel | Pandas/Matplotlib | Example |
|-------|-------------------|---------|
| Insert → Chart | `.plot()` | `df['Sales'].plot(kind='bar')` |
| Bar chart | `kind='bar'` | `df.groupby('Product')['Sales'].sum().plot(kind='bar')` |
| Line chart | `kind='line'` | `df.groupby('Month')['Sales'].sum().plot(kind='line')` |
| Pie chart | `kind='pie'` | `df.groupby('Region')['Sales'].sum().plot(kind='pie')` |
| Scatter plot | `kind='scatter'` | `df.plot(kind='scatter', x='Cost', y='Sales')` |

### Basic Plot Customization
```python
import matplotlib.pyplot as plt

df.groupby('Product')['Sales'].sum().plot(kind='bar', color='steelblue')
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

## 🎨 Conditional Formatting

| Excel | Pandas | Example |
|-------|--------|---------|
| Conditional formatting | `.style` | `df.style.background_gradient(subset=['Sales'])` |
| Highlight cells | Filter & assign | `df.loc[df['Sales'] > 1000, 'Category'] = 'High'` |
| Color scales | `.style.background_gradient()` | Applies color gradients to cells |

---

## 🔄 Common Workflows

### 1. Loading and Exploring Data
```python
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Quick look
df.head()          # First 5 rows
df.info()          # Data types and null counts
df.describe()      # Statistical summary
df.shape           # (rows, columns)
```

### 2. Data Cleaning
```python
# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.dropna()                    # Remove rows with any null
df = df.fillna(0)                   # Fill nulls with 0
df['Column'] = df['Column'].fillna(df['Column'].mean())  # Fill with mean

# Convert data types
df['Date'] = pd.to_datetime(df['Date'])
df['Sales'] = df['Sales'].astype(float)
```

### 3. Filtering (Multiple Conditions)
```python
# Single condition
high_sales = df[df['Sales'] > 1000]

# Multiple conditions (AND)
result = df[(df['Sales'] > 1000) & (df['Region'] == 'North')]

# Multiple conditions (OR)
result = df[(df['Product'] == 'Laptop') | (df['Product'] == 'Monitor')]

# Using .isin() for multiple values
result = df[df['Region'].isin(['North', 'South'])]
```

### 4. Creating Pivot Tables
```python
# Simple pivot
pivot = pd.pivot_table(
    df,
    values='Sales',
    index='Region',
    columns='Product',
    aggfunc='sum'
)

# Complex pivot with multiple aggregations
pivot = pd.pivot_table(
    df,
    values=['Sales', 'Profit'],
    index=['Region', 'Category'],
    aggfunc={'Sales': 'sum', 'Profit': ['sum', 'mean']}
)
```

### 5. Merging Data (VLOOKUP Alternative)
```python
# Left join (like VLOOKUP)
result = sales_df.merge(
    product_info_df,
    on='ProductID',
    how='left'
)

# Merge on multiple columns
result = df1.merge(
    df2,
    on=['ProductID', 'Date'],
    how='inner'
)

# Merge with different column names
result = df1.merge(
    df2,
    left_on='ProductID',
    right_on='ID',
    how='left'
)
```

---

## 💡 Pro Tips

### 1. Chain Operations
```python
# Instead of multiple steps, chain operations
result = (df[df['Sales'] > 100]
          .groupby('Region')['Sales']
          .sum()
          .sort_values(ascending=False))
```

### 2. Use .loc and .iloc
```python
# .loc for label-based indexing
df.loc[df['Sales'] > 1000, 'Category'] = 'High'

# .iloc for position-based indexing
first_5_rows = df.iloc[:5]
```

### 3. Apply Custom Functions
```python
# Define a function
def categorize(value):
    if value > 1000:
        return 'High'
    elif value > 100:
        return 'Medium'
    else:
        return 'Low'

# Apply to a column
df['Category'] = df['Sales'].apply(categorize)
```

### 4. Quick Column Operations
```python
# Perform operations on entire columns
df['Profit'] = df['Sales'] - df['Cost']
df['Margin%'] = (df['Profit'] / df['Sales']) * 100
df['Total'] = df['Price'] * df['Quantity']
```

### 5. String Operations
```python
# String methods
df['Upper'] = df['Name'].str.upper()
df['Lower'] = df['Name'].str.lower()
df['Length'] = df['Name'].str.len()
df['Contains'] = df['Name'].str.contains('Laptop')
df['Split'] = df['Name'].str.split(' ')
```

---

## 🚀 Performance Tips

| Scenario | Recommendation |
|----------|----------------|
| Large datasets (>1M rows) | Use `.query()` instead of boolean indexing |
| Many similar operations | Use `.apply()` with vectorized operations |
| Multiple conditions | Use `np.where()` or `np.select()` |
| Categorical data | Convert to `category` dtype |
| Memory issues | Load in chunks: `pd.read_csv('file.csv', chunksize=10000)` |

---

## 📚 Key Differences

| Aspect | Excel | Pandas |
|--------|-------|--------|
| **Data Size** | Limited (~1M rows) | Virtually unlimited |
| **Speed** | Slower with large data | Much faster |
| **Reproducibility** | Manual steps | Code is fully reproducible |
| **Automation** | Limited (macros) | Full automation with Python |
| **Version Control** | Difficult | Easy with Git |
| **Collaboration** | File sharing issues | Code is easy to share |
| **Learning Curve** | Easier initially | Steeper but more powerful |

---

## 🎓 Learning Path

1. **Start Here**: Basic operations (read, view, summarize)
2. **Then Learn**: Filtering, sorting, calculations
3. **Next**: GroupBy and aggregations
4. **Advanced**: Merging, pivot tables, time series
5. **Expert**: Custom functions, optimization, visualization

---

## 📖 Additional Resources

- **Official Documentation**: https://pandas.pydata.org/docs/
- **10 Minutes to Pandas**: https://pandas.pydata.org/docs/user_guide/10min.html
- **Pandas Cheat Sheet PDF**: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

---

## 💻 Quick Start Template

```python
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('your_data.csv')

# Explore
print(df.head())
print(df.info())
print(df.describe())

# Analyze
summary = df.groupby('Category')['Sales'].sum()
print(summary)

# Visualize
summary.plot(kind='bar')
plt.title('Sales by Category')
plt.show()

# Export
df.to_csv('output.csv', index=False)
```

---

**Remember**: The best way to learn is by doing! Start with simple tasks and gradually build up to more complex analyses. 🚀
