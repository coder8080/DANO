import matplotlib.pyplot as plt
import seaborn as sns


def main():
    plt.ylim(0, 50)

    dataset_after = sns.load_dataset("during", data_home="./data_home")
    sns.barplot(data=dataset_after, x="genre",
                y="count", palette=['#3274a1', '#c03d3e', '#845b53', '#3a923a', '#d684bd'])
    plt.savefig('images/during.png')


if __name__ == '__main__':
    main()
