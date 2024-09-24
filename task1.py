import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    return pd.read_csv(file) 

def exercise_1(df):
    return df.columns

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(k)

def exercise_4(df):
    return df['type'].unique()

def exercise_5(df):
    freq = df["nameDest"].value_counts()
    return freq[:10]

def exercise_6(df):
    return df.loc[df["isFraud"] == 1]

def exercise_7(df):
    return df.groupby(["nameDest"])["newbalanceDest"].agg("mean").sort_values(ascending=False)

def visual_1(df):
    def transaction_counts(df):
        # TODO
        return df["type"].value_counts()
    def transaction_counts_split_by_fraud(df):
        # TODO
        return df.groupby(by=["type" , "isFraud"]).size()

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction types vs Occurence')
    axs[0].set_xlabel('Transaction Types')
    axs[0].set_ylabel('Occurrence')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction types split by fraud bar chart')
    axs[1].set_xlabel('(Type , Fraud)')
    axs[1].set_ylabel('Occurrence')
    fig.suptitle('Transactions Chart')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return 'The fraudulent activities in given dataset can only be seen while transactions like CASH_OUT or TRANSFER.'

def visual_2(df):
    def query(df):
        # TODO
        df["OriginDelta"] = df["oldbalanceOrg"] - df["newbalanceOrig"]
        df["DestDelta"] = df["oldbalanceDest"] - df["newbalanceDest"]
        return df.loc[df["type"] == "CASH_OUT"]
    plot = query(df).plot.scatter(x='OriginDelta',y='DestDelta')
    plot.set_title('Origin account balance delta v. Destination account balance delta')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return 'The line y=-x is particularly interesting as it is result of instantacnous settlement'

def exercise_custom(df):
    return df[["isFlaggedFraud" , "isFraud"]].value_counts()

def visual_custom(df):
    fig, ax = plt.subplots(1, figsize=(4,6))
    exercise_custom(df).plot(ax=ax, kind='bar')
    ax.set_title('Fraud Detection')
    ax.set_xlabel('isFlaggedFraud, isFraud')
    ax.set_ylabel('Occurrence')
    for p in ax.patches:
        ax.annotate(p.get_height(), (p.get_x(), p.get_height()))

    return "The Following graph shows how effective the fraud detection is."

