import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame


def setup_plotting_style() -> None:
    plt.style.use('default')
    sns.set_palette("husl")


def create_distribution_plots(df: DataFrame) -> plt.Figure:
    setup_plotting_style()
    
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    fig.suptitle('Distribution Analysis: Survivors vs Non-Survivors', fontsize=16, y=1.02)
    
    survivors = df[df['Survived'] == 1]
    non_survivors = df[df['Survived'] == 0]

    # age
    
    axes[0, 0].hist(non_survivors['Age'], bins=30, alpha=0.7, label='Non-survivors', color='red')
    axes[0, 0].hist(survivors['Age'], bins=30, alpha=0.7, label='Survivors', color='blue')

    axes[0, 0].set_title('Age Distribution')
    axes[0, 0].set_xlabel('Age')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].legend()

    # fare
 
    axes[0, 1].hist(non_survivors['Fare'], bins=50, alpha=0.7, label='Non-survivors', color='red')
    axes[0, 1].hist(survivors['Fare'], bins=50, alpha=0.7, label='Survivors', color='blue')

    axes[0, 1].set_title('Fare Distribution')
    axes[0, 1].set_xlabel('Fare')
    axes[0, 1].set_ylabel('Frequency')

    axes[0, 1].legend()
    axes[0, 1].set_xlim(0, 200) # add limits for better visualization

    # pclass
    
    pclass_counts = df.groupby(['Pclass', 'Survived']).size().unstack()
    pclass_counts.plot(kind='bar', ax=axes[0, 2], color=['red', 'blue'])

    axes[0, 2].set_title('Passenger Class Distribution')
    axes[0, 2].set_xlabel('Passenger Class')
    axes[0, 2].set_ylabel('Count')

    axes[0, 2].legend(['Non-survivors', 'Survivors'])
    axes[0, 2].tick_params(axis='x', rotation=0)
    
    # sex

    sex_counts = df.groupby(['Sex', 'Survived']).size().unstack()
    sex_counts.plot(kind='bar', ax=axes[1, 0], color=['red', 'blue'])
    
    axes[1, 0].set_title('Sex Distribution')
    axes[1, 0].set_xlabel('Sex (0=Female, 1=Male)')
    axes[1, 0].set_ylabel('Count')

    axes[1, 0].legend(['Non-survivors', 'Survivors'])
    axes[1, 0].tick_params(axis='x', rotation=0)
    
    # deck

    deck_counts = df.groupby(['Deck', 'Survived']).size().unstack()
    deck_counts.plot(kind='bar', ax=axes[1, 1], color=['red', 'blue'])

    axes[1, 1].set_title('Deck Distribution')
    axes[1, 1].set_xlabel('Deck')
    axes[1, 1].set_ylabel('Count')

    axes[1, 1].legend(['Non-survivors', 'Survivors'])
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    # sibsp

    sibsp_counts = df.groupby(['SibSp', 'Survived']).size().unstack()
    sibsp_counts.plot(kind='bar', ax=axes[1, 2], color=['red', 'blue'])

    axes[1, 2].set_title('Siblings/Spouses Distribution')
    axes[1, 2].set_xlabel('Number of Siblings/Spouses')
    axes[1, 2].set_ylabel('Count')

    axes[1, 2].legend(['Non-survivors', 'Survivors'])
    axes[1, 2].tick_params(axis='x', rotation=0)
    
    # parch

    parch_counts = df.groupby(['Parch', 'Survived']).size().unstack()
    parch_counts.plot(kind='bar', ax=axes[2, 0], color=['red', 'blue'])

    axes[2, 0].set_title('Parents/Children Distribution')
    axes[2, 0].set_xlabel('Number of Parents/Children')
    axes[2, 0].set_ylabel('Count')

    axes[2, 0].legend(['Non-survivors', 'Survivors'])
    axes[2, 0].tick_params(axis='x', rotation=0)
    
    # add box plots for age and fare

    box_data_age = [survivors['Age'], non_survivors['Age']]
    axes[2, 1].boxplot(box_data_age, labels=['Survivors', 'Non-survivors'])
    axes[2, 1].set_title('Age Distribution')
    axes[2, 1].set_ylabel('Age')
    
    box_data_fare = [survivors['Fare'], non_survivors['Fare']]
    axes[2, 2].boxplot(box_data_fare, labels=['Survivors', 'Non-survivors'])
    axes[2, 2].set_title('Fare Distribution')
    axes[2, 2].set_ylabel('Fare')
    
    plt.tight_layout()
    return fig


def print_survival_analysis(df):
    print("Overall survival rate:", f"{df['Survived'].mean():.1%}")
    print()
    
    print("Survival rates by Sex:")
    print(f"Female (0): {df[df['Sex']==0]['Survived'].mean():.1%}")
    print(f"Male (1): {df[df['Sex']==1]['Survived'].mean():.1%}")
    print()
    
    print("Survival rates by Passenger Class:")

    for pclass in sorted(df['Pclass'].unique()):
        rate = df[df['Pclass']==pclass]['Survived'].mean()
        print(f"Class {pclass}: {rate:.1%}")

    print()
    
    print("Survival rates by Deck:")

    for deck in sorted(df['Deck'].unique()):
        # do not print missing values
        if deck != -1:
            rate = df[df['Deck']==deck]['Survived'].mean()
            count = len(df[df['Deck']==deck])

            print(f"Deck {deck}: {rate:.1%} (n={count})")

    print()


def print_distribution_comparison(df):
    survivors = df[df['Survived'] == 1]
    non_survivors = df[df['Survived'] == 0]

    print("STATS - AGE:")
    print("Survivors:")
    print(f"  Mean: {survivors['Age'].mean():.2f}, Median: {survivors['Age'].median():.2f}, Std: {survivors['Age'].std():.2f}")
    print("Non-survivors:")
    print(f"  Mean: {non_survivors['Age'].mean():.2f}, Median: {non_survivors['Age'].median():.2f}, Std: {non_survivors['Age'].std():.2f}")
    print()

    print("STATS - FARE:")
    print("Survivors:")
    print(f"  Mean: {survivors['Fare'].mean():.2f}, Median: {survivors['Fare'].median():.2f}, Std: {survivors['Fare'].std():.2f}")
    print("Non-survivors:")
    print(f"  Mean: {non_survivors['Fare'].mean():.2f}, Median: {non_survivors['Fare'].median():.2f}, Std: {non_survivors['Fare'].std():.2f}")
    print()


def run_complete_analysis(df):
    fig = create_distribution_plots(df)
    plt.show()

    print_survival_analysis(df)
    print_distribution_comparison(df)
    
    return fig
