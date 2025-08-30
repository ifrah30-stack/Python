# Data analysis and visualization with pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataAnalyzer:
    def __init__(self, data):
        self.df = pd.DataFrame(data)
    
    def basic_stats(self):
        return {
            'shape': self.df.shape,
            'columns': list(self.df.columns),
            'dtypes': self.df.dtypes.to_dict(),
            'null_counts': self.df.isnull().sum().to_dict(),
            'describe': self.df.describe()
        }
    
    def analyze_numeric(self):
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        analysis = {}
        
        for col in numeric_cols:
            analysis[col] = {
                'mean': self.df[col].mean(),
                'median': self.df[col].median(),
                'std': self.df[col].std(),
                'min': self.df[col].min(),
                'max': self.df[col].max(),
                'skew': self.df[col].skew(),
                'kurtosis': self.df[col].kurtosis()
            }
        
        return analysis
    
    def create_visualizations(self):
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) >= 2:
            fig, axes = plt.subplots(2, 2, figsize=(12, 10))
            
            # Scatter plot
            self.df.plot.scatter(x=numeric_cols[0], y=numeric_cols[1], ax=axes[0,0])
            axes[0,0].set_title('Scatter Plot')
            
            # Histogram
            self.df[numeric_cols[0]].hist(ax=axes[0,1], bins=20)
            axes[0,1].set_title('Histogram')
            
            # Box plot
            self.df[numeric_cols].boxplot(ax=axes[1,0])
            axes[1,0].set_title('Box Plot')
            
            # Correlation heatmap
            corr = self.df[numeric_cols].corr()
            im = axes[1,1].imshow(corr, cmap='coolwarm', interpolation='nearest')
            axes[1,1].set_xticks(range(len(corr.columns)))
            axes[1,1].set_yticks(range(len(corr.columns)))
            axes[1,1].set_xticklabels(corr.columns, rotation=45)
            axes[1,1].set_yticklabels(corr.columns)
            plt.colorbar(im, ax=axes[1,1])
            axes[1,1].set_title('Correlation Heatmap')
            
            plt.tight_layout()
            plt.show()

# Sample data
sample_data = {
    'age': np.random.randint(18, 65, 100),
    'salary': np.random.normal(50000, 15000, 100),
    'experience': np.random.randint(0, 40, 100),
    'department': np.random.choice(['IT', 'HR', 'Finance', 'Marketing'], 100)
}

# Usage
analyzer = DataAnalyzer(sample_data)
print("Basic Stats:", analyzer.basic_stats())
print("Numeric Analysis:", analyzer.analyze_numeric())
analyzer.create_visualizations()
