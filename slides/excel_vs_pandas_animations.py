from manim import *

class ExcelVsPandasSUM(Scene):
    """Animation comparing Excel SUM function to Pandas sum()"""
    
    def construct(self):
        # Title
        title = Text("Excel vs Pandas: SUM Function", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Excel side
        excel_title = Text("Excel", font_size=36, color=GREEN).shift(LEFT * 3 + UP * 1.5)
        excel_formula = Text("=SUM(D2:D10)", font_size=28).shift(LEFT * 3 + UP * 0.5)
        
        # Excel spreadsheet representation
        excel_cells = VGroup()
        values = [120, 250, 180, 95, 310, 220, 160, 280, 145]
        for i, val in enumerate(values):
            cell = Text(f"${val}", font_size=20).shift(LEFT * 3 + DOWN * (i * 0.3))
            excel_cells.add(cell)
        
        excel_group = VGroup(excel_title, excel_formula, excel_cells)
        
        # Pandas side
        pandas_title = Text("Pandas", font_size=36, color=ORANGE).shift(RIGHT * 3 + UP * 1.5)
        pandas_code = Code(
            code="df['Sales'].sum()",
            language="python",
            font_size=20,
            background="window",
            style="monokai"
        ).shift(RIGHT * 3 + UP * 0.3)
        pandas_code.scale(0.7)
        
        pandas_group = VGroup(pandas_title, pandas_code)
        
        # Animate Excel side
        self.play(Write(excel_title))
        self.play(Write(excel_formula))
        self.play(Create(excel_cells), run_time=2)
        self.wait(0.5)
        
        # Animate Pandas side
        self.play(Write(pandas_title))
        self.play(Create(pandas_code))
        self.wait(0.5)
        
        # Calculate sum
        total = sum(values)
        excel_result = Text(f"= ${total}", font_size=32, color=YELLOW).shift(LEFT * 3 + DOWN * 3)
        pandas_result = Text(f"${total}", font_size=32, color=YELLOW).shift(RIGHT * 3 + DOWN * 1)
        
        # Show results simultaneously
        self.play(
            Write(excel_result),
            Write(pandas_result)
        )
        self.wait(1)
        
        # Highlight advantage
        advantage = Text(
            "Pandas: Same result, but works on millions of rows instantly!",
            font_size=24,
            color=BLUE
        ).to_edge(DOWN)
        self.play(Write(advantage))
        self.wait(2)


class ExcelVsPandasVLOOKUP(Scene):
    """Animation comparing Excel VLOOKUP to Pandas merge"""
    
    def construct(self):
        # Title
        title = Text("Excel VLOOKUP vs Pandas Merge", font_size=44, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Excel VLOOKUP
        excel_title = Text("Excel VLOOKUP", font_size=32, color=GREEN).shift(LEFT * 3.5 + UP * 2)
        excel_formula = Text(
            "=VLOOKUP(B2,\nProductTable,2,FALSE)",
            font_size=18,
            line_spacing=0.8
        ).shift(LEFT * 3.5 + UP * 0.8)
        
        excel_note = Text(
            "• Must count columns\n• Only looks right\n• One column at a time\n• Slow on large data",
            font_size=16,
            line_spacing=1.2,
            color=GRAY
        ).shift(LEFT * 3.5 + DOWN * 0.5)
        
        excel_group = VGroup(excel_title, excel_formula, excel_note)
        
        # Pandas merge
        pandas_title = Text("Pandas Merge", font_size=32, color=ORANGE).shift(RIGHT * 3.5 + UP * 2)
        pandas_code = Code(
            code="df.merge(product_info,\n         on='Product',\n         how='left')",
            language="python",
            font_size=16,
            background="window",
            style="monokai"
        ).shift(RIGHT * 3.5 + UP * 0.7)
        pandas_code.scale(0.8)
        
        pandas_note = Text(
            "• No column counting\n• Bidirectional lookup\n• All columns at once\n• Fast on any size",
            font_size=16,
            line_spacing=1.2,
            color=GRAY
        ).shift(RIGHT * 3.5 + DOWN * 0.5)
        
        pandas_group = VGroup(pandas_title, pandas_code, pandas_note)
        
        # Animate
        self.play(Write(excel_title))
        self.play(Write(excel_formula))
        self.play(FadeIn(excel_note))
        self.wait(0.5)
        
        self.play(Write(pandas_title))
        self.play(Create(pandas_code))
        self.play(FadeIn(pandas_note))
        self.wait(1)
        
        # Winner announcement
        winner = Text("Winner: Pandas! 🏆", font_size=36, color=YELLOW)
        winner.to_edge(DOWN)
        self.play(Write(winner))
        self.wait(2)


class ExcelVsPandasPivot(Scene):
    """Animation comparing Excel Pivot Tables to Pandas groupby"""
    
    def construct(self):
        # Title
        title = Text("Pivot Tables: Excel vs Pandas", font_size=44, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Excel Process
        excel_title = Text("Excel Process", font_size=32, color=GREEN).shift(LEFT * 3.5 + UP * 2)
        excel_steps = VGroup(
            Text("1. Select data", font_size=20),
            Text("2. Insert → PivotTable", font_size=20),
            Text("3. Drag fields to areas", font_size=20),
            Text("4. Configure calculations", font_size=20),
            Text("5. Format results", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(LEFT * 3.5 + UP * 0.2)
        
        excel_time = Text("⏱️ ~2-3 minutes", font_size=24, color=RED).shift(LEFT * 3.5 + DOWN * 1.8)
        
        # Pandas Process
        pandas_title = Text("Pandas Process", font_size=32, color=ORANGE).shift(RIGHT * 3.5 + UP * 2)
        pandas_code = Code(
            code="""df.groupby('Region')['Sales']
  .sum()
  .sort_values()""",
            language="python",
            font_size=18,
            background="window",
            style="monokai"
        ).shift(RIGHT * 3.5 + UP * 0.5)
        pandas_code.scale(0.9)
        
        pandas_time = Text("⚡ <1 second", font_size=24, color=GREEN).shift(RIGHT * 3.5 + DOWN * 1.8)
        
        # Animate Excel process
        self.play(Write(excel_title))
        for i, step in enumerate(excel_steps):
            self.play(Write(step), run_time=0.5)
            self.wait(0.3)
        self.play(Write(excel_time))
        self.wait(0.5)
        
        # Animate Pandas process
        self.play(Write(pandas_title))
        self.play(Create(pandas_code), run_time=1)
        self.play(Write(pandas_time))
        self.wait(1)
        
        # Conclusion
        conclusion = Text(
            "Pandas: Faster, repeatable, and scales to millions of rows!",
            font_size=26,
            color=YELLOW
        ).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)


class ExcelVsPandasCharts(Scene):
    """Animation showing chart creation comparison"""
    
    def construct(self):
        # Title
        title = Text("Creating Charts: Excel vs Pandas", font_size=44, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create sample data representation
        data_title = Text("Sample Data: Sales by Product", font_size=28).shift(UP * 2)
        
        # Simple bar chart representation
        products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
        values = [15000, 800, 1200, 4500]
        
        # Excel section
        excel_label = Text("Excel", font_size=32, color=GREEN).shift(LEFT * 3.5 + UP * 1)
        excel_steps = Text(
            "1. Select data\n2. Insert → Chart\n3. Choose type\n4. Format manually",
            font_size=18,
            line_spacing=1.2
        ).shift(LEFT * 3.5 + DOWN * 0.2)
        
        # Pandas section
        pandas_label = Text("Pandas", font_size=32, color=ORANGE).shift(RIGHT * 3.5 + UP * 1)
        pandas_code = Code(
            code="""df.groupby('Product')['Sales']
  .sum()
  .plot(kind='bar')""",
            language="python",
            font_size=18,
            background="window",
            style="monokai"
        ).shift(RIGHT * 3.5 + DOWN * 0.2)
        pandas_code.scale(0.85)
        
        # Animate
        self.play(Write(data_title))
        self.wait(0.5)
        
        self.play(Write(excel_label), Write(pandas_label))
        self.wait(0.3)
        
        self.play(Write(excel_steps), Create(pandas_code))
        self.wait(1)
        
        # Create simple bar chart animation
        chart_title = Text("Result: Professional Chart", font_size=24).to_edge(DOWN).shift(UP * 2)
        self.play(Write(chart_title))
        
        # Simple bars
        bars = VGroup()
        max_height = 2
        for i, (product, value) in enumerate(zip(products, values)):
            height = (value / max(values)) * max_height
            bar = Rectangle(
                width=0.6,
                height=height,
                color=BLUE,
                fill_opacity=0.7
            ).shift(DOWN * 2 + LEFT * 2.5 + RIGHT * i * 1.5)
            bars.add(bar)
        
        self.play(Create(bars), run_time=2)
        self.wait(1)
        
        # Advantage text
        advantage = Text(
            "Pandas: Automated, consistent, and programmable!",
            font_size=24,
            color=YELLOW
        ).to_edge(DOWN)
        self.play(Write(advantage))
        self.wait(2)


class WorkshopIntro(Scene):
    """Introduction animation for the workshop"""
    
    def construct(self):
        # Main title
        title = Text("Python for Business Students", font_size=52, color=BLUE)
        subtitle = Text("From Excel to Pandas", font_size=36, color=ORANGE)
        subtitle.next_to(title, DOWN)
        
        title_group = VGroup(title, subtitle)
        
        self.play(Write(title), run_time=1.5)
        self.play(Write(subtitle), run_time=1.5)
        self.wait(1)
        
        # Transform to smaller size
        self.play(title_group.animate.scale(0.5).to_edge(UP))
        self.wait(0.5)
        
        # What you'll learn
        learn_title = Text("What You'll Learn:", font_size=36, color=GREEN).shift(UP * 1.5)
        
        topics = VGroup(
            Text("✓ Excel formulas → Pandas functions", font_size=24),
            Text("✓ VLOOKUP → Merge operations", font_size=24),
            Text("✓ Pivot Tables → GroupBy analysis", font_size=24),
            Text("✓ Charts → Data visualization", font_size=24),
            Text("✓ Real business projects", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(DOWN * 0.3)
        
        self.play(Write(learn_title))
        self.wait(0.5)
        
        for topic in topics:
            self.play(Write(topic), run_time=0.7)
            self.wait(0.3)
        
        self.wait(1)
        
        # Closing message
        closing = Text("Let's Get Started! 🚀", font_size=40, color=YELLOW)
        closing.to_edge(DOWN)
        self.play(Write(closing))
        self.wait(2)
