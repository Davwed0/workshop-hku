# Manim Slides - Excel vs Pandas Animations

This directory contains Manim animations comparing Excel and Pandas operations.

## Available Animations

1. **WorkshopIntro**: Introduction to the workshop
2. **ExcelVsPandasSUM**: Comparing SUM function
3. **ExcelVsPandasVLOOKUP**: Comparing VLOOKUP vs Merge
4. **ExcelVsPandasPivot**: Comparing Pivot Tables vs GroupBy
5. **ExcelVsPandasCharts**: Comparing chart creation

## How to Render Animations

### Render a single animation:
```bash
manim -pql excel_vs_pandas_animations.py WorkshopIntro
```

### Render all animations:
```bash
manim -pql excel_vs_pandas_animations.py WorkshopIntro
manim -pql excel_vs_pandas_animations.py ExcelVsPandasSUM
manim -pql excel_vs_pandas_animations.py ExcelVsPandasVLOOKUP
manim -pql excel_vs_pandas_animations.py ExcelVsPandasPivot
manim -pql excel_vs_pandas_animations.py ExcelVsPandasCharts
```

### Render in high quality:
```bash
manim -pqh excel_vs_pandas_animations.py WorkshopIntro
```

## Quality Options
- `-ql`: Low quality (faster rendering, for testing)
- `-qm`: Medium quality
- `-qh`: High quality (production)
- `-p`: Preview after rendering

## Output
Videos will be saved in `media/videos/excel_vs_pandas_animations/`

## Tips for Presentation
- Use low quality for quick previews during development
- Render in high quality for final presentation
- Consider creating a slide deck with embedded videos
- Or use the videos directly in your presentation software

## Customization
Edit `excel_vs_pandas_animations.py` to customize:
- Colors and styling
- Animation timing
- Text content
- Data examples
