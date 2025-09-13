import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame


def setup_plotting_style() -> None:
    plt.style.use('default')


def create_seaborn_pairplot(df: DataFrame) -> sns.axisgrid.PairGrid:
    setup_plotting_style()

    plot_vars = ['Age', 'Fare', 'SibSp', 'Parch', 'Pclass']
    
    df_plot = df[plot_vars + ['Survived']].copy()
    df_plot['Survival_Status'] = df_plot['Survived'].map({0: 'Non-survivor', 1: 'Survivor'})
    
    # Set custom colors: red for non-survivors, blue for survivors
    custom_colors = {'Non-survivor': 'red', 'Survivor': 'blue'}
    
    g = sns.pairplot(df_plot, 
                     vars=plot_vars,
                     hue='Survival_Status',
                     palette=custom_colors,
                     diag_kind='hist',
                     plot_kws={'alpha': 0.6, 's': 15},
                     diag_kws={'alpha': 0.7})

    g.figure.suptitle('Seaborn Pairplot: Variables by Survival Status', y=1.02, fontsize=16)
    
    return g


def run_pairwise_analysis(df: DataFrame) -> tuple:
    pairplot = create_seaborn_pairplot(df)
    plt.show()
    
    return pairplot
