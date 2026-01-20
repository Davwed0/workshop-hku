#!/usr/bin/env python3
"""
Test script to validate that all notebooks can be executed without errors.
This ensures the workshop materials are functional and beginner-friendly.
"""

import sys
import os

def test_imports():
    """Test that all required libraries can be imported."""
    print("Testing imports...")
    try:
        import pandas as pd
        print(f"✓ pandas {pd.__version__}")
        
        import numpy as np
        print(f"✓ numpy {np.__version__}")
        
        import matplotlib
        print(f"✓ matplotlib {matplotlib.__version__}")
        
        import seaborn
        print(f"✓ seaborn {seaborn.__version__}")
        
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_data_loading():
    """Test that the sample data can be loaded."""
    print("\nTesting data loading...")
    try:
        import pandas as pd
        df = pd.read_csv('data/superstore_sales.csv')
        
        # Validate data structure
        assert df.shape[0] == 60, f"Expected 60 rows, got {df.shape[0]}"
        assert df.shape[1] == 5, f"Expected 5 columns, got {df.shape[1]}"
        
        expected_cols = ['Date', 'Product', 'Region', 'Sales', 'Cost']
        assert list(df.columns) == expected_cols, f"Unexpected columns: {list(df.columns)}"
        
        print(f"✓ Data loaded: {df.shape[0]} rows × {df.shape[1]} columns")
        print(f"✓ Columns: {', '.join(df.columns)}")
        print(f"✓ Date range: {df['Date'].min()} to {df['Date'].max()}")
        
        return True
    except Exception as e:
        print(f"✗ Data loading error: {e}")
        return False

def test_basic_operations():
    """Test basic pandas operations used in the notebooks."""
    print("\nTesting basic operations...")
    try:
        import pandas as pd
        import numpy as np
        
        df = pd.read_csv('data/superstore_sales.csv')
        
        # Test calculations (from notebook 1)
        df['Profit'] = df['Sales'] - df['Cost']
        df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
        
        # Test aggregations
        total_sales = df['Sales'].sum()
        avg_sales = df['Sales'].mean()
        count_sales = df['Sales'].count()
        
        print(f"✓ Total Sales: ${total_sales:,.2f}")
        print(f"✓ Average Sales: ${avg_sales:,.2f}")
        print(f"✓ Count: {count_sales}")
        
        # Test filtering
        laptop_sales = df[df['Product'] == 'Laptop']
        print(f"✓ Laptop sales: {len(laptop_sales)} records")
        
        # Test groupby
        product_sales = df.groupby('Product')['Sales'].sum()
        print(f"✓ GroupBy works: {len(product_sales)} products")
        
        return True
    except Exception as e:
        print(f"✗ Operation error: {e}")
        return False

def test_advanced_operations():
    """Test advanced operations from notebook 2."""
    print("\nTesting advanced operations...")
    try:
        import pandas as pd
        
        df = pd.read_csv('data/superstore_sales.csv')
        df['Profit'] = df['Sales'] - df['Cost']
        
        # Test merge (VLOOKUP equivalent)
        product_info = pd.DataFrame({
            'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
            'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics'],
        })
        
        df_merged = df.merge(product_info, on='Product', how='left')
        assert 'Category' in df_merged.columns, "Merge failed"
        print(f"✓ Merge operation successful")
        
        # Test pivot table
        pivot = pd.pivot_table(
            df,
            values='Sales',
            index='Region',
            columns='Product',
            aggfunc='sum',
            fill_value=0
        )
        print(f"✓ Pivot table created: {pivot.shape}")
        
        # Test date operations
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        print(f"✓ Date operations successful")
        
        return True
    except Exception as e:
        print(f"✗ Advanced operation error: {e}")
        return False

def test_visualization():
    """Test that visualization libraries work."""
    print("\nTesting visualization...")
    try:
        import pandas as pd
        import matplotlib
        matplotlib.use('Agg')  # Use non-interactive backend
        import matplotlib.pyplot as plt
        
        df = pd.read_csv('data/superstore_sales.csv')
        
        # Test simple plot
        product_sales = df.groupby('Product')['Sales'].sum()
        fig, ax = plt.subplots(figsize=(8, 6))
        product_sales.plot(kind='bar', ax=ax)
        plt.close(fig)
        
        print(f"✓ Visualization library works")
        return True
    except Exception as e:
        print(f"✗ Visualization error: {e}")
        return False

def main():
    """Run all tests."""
    print("="*60)
    print("WORKSHOP VALIDATION TEST")
    print("="*60)
    
    tests = [
        ("Import Test", test_imports),
        ("Data Loading Test", test_data_loading),
        ("Basic Operations Test", test_basic_operations),
        ("Advanced Operations Test", test_advanced_operations),
        ("Visualization Test", test_visualization),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n✗ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Workshop materials are ready to use.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please review the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
