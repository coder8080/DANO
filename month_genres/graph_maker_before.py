import matplotlib.pyplot as plt
import seaborn as sns


def main():
    plt.ylim(0, 50)

    dataset_after = sns.load_dataset("before", data_home="./data_home")
    sns.barplot(data=dataset_after, x="genre", y="count",
                palette=['#3274a1', '#e1812c', '#3a923a', '#c03d3e', '#9372b2'])
    plt.savefig('images/before.png')


if __name__ == '__main__':
    main()
