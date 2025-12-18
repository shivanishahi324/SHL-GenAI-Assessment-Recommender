import pandas as pd

FILE_PATH = "Gen_AI Dataset.xlsx"

def load_company_data():
    xls = pd.ExcelFile(FILE_PATH)
    print("Sheets found in Excel:", xls.sheet_names)

    train_df = pd.read_excel(xls, xls.sheet_names[0])
    test_df = pd.read_excel(xls, xls.sheet_names[1])

    print("\nTrain Data Preview:")
    print(train_df.head())

    print("\nTest Data Preview:")
    print(test_df.head())

    print("\nTrain shape:", train_df.shape)
    print("Test shape:", test_df.shape)

    return train_df, test_df


if __name__ == "__main__":
    load_company_data()
