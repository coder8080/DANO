import matplotlib.pyplot as plt
import seaborn as sns
from constants import max_value


def main():
    plt.ylim(0, max_value)
    dataset_before = sns.load_dataset("before", data_home="./data_home")
    sns.barplot(data=dataset_before, x="weekday",
                y="count")
    plt.savefig('images/before.png')


if __name__ == '__main__':
    main()
