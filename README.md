# Python for Business Students: Excel to Pandas Workshop

A comprehensive, beginner-friendly Python workshop designed specifically for business students to transition from Excel to Python using Pandas. Learn data analysis with side-by-side Excel comparisons and real-world business examples.

## 🎯 Workshop Overview

This workshop teaches you how to perform common business analysis tasks in Python that you already know how to do in Excel. You'll learn:

- **Excel formulas → Pandas functions** (SUM, AVERAGE, COUNT, etc.)
- **VLOOKUP → Merge operations** (joining datasets)
- **Pivot Tables → GroupBy analysis** (data aggregation)
- **Charts → Data visualization** (professional graphs)
- **Real business project** (complete analysis workflow)

## 📚 Repository Structure

```
workshop-hku/
├── notebooks/              # Jupyter notebooks with lessons
│   ├── 01_basics.ipynb    # Excel basics to Pandas
│   ├── 02_advanced.ipynb  # VLOOKUP, Pivot Tables, advanced functions
│   └── 03_project.ipynb   # Complete business analysis project
├── data/                   # Sample datasets
│   └── superstore_sales.csv
├── slides/                 # Manim animated presentations
│   ├── excel_vs_pandas_animations.py
│   └── README.md
├── requirements.txt        # Python dependencies
├── CHEATSHEET.md          # Quick reference guide
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites

- Basic familiarity with Excel
- No Python experience required!
- Computer with Python 3.8+ installed

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Davwed0/workshop-hku.git
   cd workshop-hku
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

5. **Open `notebooks/01_basics.ipynb` to start learning!**

## 📖 Workshop Modules

### Module 1: Basics (`01_basics.ipynb`)
**Duration: ~60 minutes**

Learn the fundamental operations:
- Loading and viewing data
- Basic statistics (SUM, AVERAGE, COUNT, MIN, MAX)
- Filtering data
- Creating new columns
- Sorting
- Simple charts

**Excel Equivalents:**
- `=SUM()` → `df.sum()`
- `=AVERAGE()` → `df.mean()`
- `=COUNT()` → `df.count()`
- Filter & Sort → Boolean indexing & `.sort_values()`

### Module 2: Advanced (`02_advanced.ipynb`)
**Duration: ~90 minutes**

Master advanced techniques:
- VLOOKUP → Merge/Join operations
- Pivot Tables → GroupBy aggregations
- SUMIF, COUNTIF, AVERAGEIF
- Date operations
- Multiple aggregations
- Heatmaps and advanced visualizations

**Excel Equivalents:**
- `=VLOOKUP()` → `.merge()`
- Pivot Tables → `.groupby()` & `.pivot_table()`
- `=SUMIF()` → Filtered aggregations
- Date functions → `.dt` accessor

### Module 3: Complete Project (`03_project.ipynb`)
**Duration: ~120 minutes**

Apply everything in a real business scenario:
- Complete sales analysis workflow
- KPI dashboard creation
- Product and regional performance analysis
- Time series analysis
- Cross-dimensional analysis
- Business insights and recommendations
- Professional report generation

**Skills Practiced:**
- Data preparation and feature engineering
- Comprehensive business analysis
- Executive summary creation
- Data storytelling
- Actionable recommendations

## 📊 Sample Data

The workshop uses `superstore_sales.csv` with realistic retail data:
- **60 transactions** across 6 months
- **4 products**: Laptop, Mouse, Keyboard, Monitor
- **4 regions**: North, South, East, West
- **Columns**: Date, Product, Region, Sales, Cost

Perfect for learning without being overwhelming!

## 🎬 Animated Slides (Manim)

The `slides/` directory contains Manim animations comparing Excel and Pandas operations:

1. **WorkshopIntro** - Introduction to the workshop
2. **ExcelVsPandasSUM** - Comparing SUM function
3. **ExcelVsPandasVLOOKUP** - VLOOKUP vs Merge
4. **ExcelVsPandasPivot** - Pivot Tables vs GroupBy
5. **ExcelVsPandasCharts** - Chart creation comparison

### Rendering Animations

```bash
cd slides
manim -pql excel_vs_pandas_animations.py WorkshopIntro
```

See `slides/README.md` for detailed instructions.

## 📝 Cheat Sheet

Check out `CHEATSHEET.md` for a comprehensive quick reference guide with:
- Side-by-side Excel and Pandas comparisons
- Common operations and their equivalents
- Code examples for every function
- Pro tips and best practices
- Quick start templates

Perfect for printing or keeping open while you work!

## 💡 Key Advantages of Pandas over Excel

| Feature | Excel | Pandas |
|---------|-------|--------|
| **Data Size** | ~1M rows max | Unlimited (memory-dependent) |
| **Speed** | Slow with large data | 10-100x faster |
| **Automation** | Limited (VBA macros) | Full Python automation |
| **Reproducibility** | Manual steps | Code is reproducible |
| **Version Control** | Difficult | Easy with Git |
| **Advanced Analytics** | Limited | Full Python ecosystem |

## 🎓 Learning Outcomes

By the end of this workshop, you will be able to:

✅ Load and explore data from CSV files  
✅ Perform calculations and aggregations  
✅ Filter and sort data efficiently  
✅ Join datasets (VLOOKUP replacement)  
✅ Create pivot tables and groupby analyses  
✅ Generate professional visualizations  
✅ Conduct complete business analysis  
✅ Automate repetitive data tasks  
✅ Write reproducible analysis code  

## 🛠️ Troubleshooting

### Jupyter Notebook won't start
```bash
# Try reinstalling jupyter
pip install --upgrade jupyter notebook
```

### Import errors
```bash
# Reinstall requirements
pip install -r requirements.txt --upgrade
```

### Manim installation issues
```bash
# Manim has system dependencies. See:
# https://docs.manim.community/en/stable/installation.html
```

### Python version issues
This workshop requires Python 3.8 or higher:
```bash
python --version  # Check your version
```

## 📚 Additional Resources

- **Pandas Documentation**: https://pandas.pydata.org/docs/
- **10 Minutes to Pandas**: https://pandas.pydata.org/docs/user_guide/10min.html
- **Matplotlib Gallery**: https://matplotlib.org/stable/gallery/
- **Seaborn Tutorial**: https://seaborn.pydata.org/tutorial.html
- **Python for Data Analysis (Book)**: By Wes McKinney (Pandas creator)

## 🤝 Contributing

Found a bug or have a suggestion? Feel free to:
- Open an issue
- Submit a pull request
- Share your feedback

## 📧 Contact & Support

For questions or support:
- **Create an issue** in this repository
- **Email**: [Your contact information]
- **Office Hours**: [If applicable]

## 🎉 Acknowledgments

This workshop was created for business students at HKU (Hong Kong University) to make data analysis accessible and practical.

Special thanks to:
- The Pandas development team
- The Jupyter project
- The Manim community
- All workshop participants for their feedback

## 📄 License

This workshop material is available for educational use. Feel free to use and adapt for your own learning or teaching!

---

## 🚀 Quick Start Checklist

- [ ] Clone the repository
- [ ] Install Python 3.8+
- [ ] Create virtual environment
- [ ] Install requirements
- [ ] Launch Jupyter Notebook
- [ ] Open `01_basics.ipynb`
- [ ] Start learning!

**Ready to transform your data analysis skills? Let's get started! 📊✨**

---

*Last updated: January 2026*