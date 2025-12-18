import pandas as pd
from load_company_data import load_company_data
from retrieve_test import recommend

def generate_final_csv():
    _, test_df = load_company_data()

    rows = []

    for idx, row in test_df.iterrows():
        query = row["Query"]

        results = recommend(query, top_k=10)

        # canonical_url nikaalo (metadata ke according)
        urls = []
        for r in results:
            url = r.get("canonical_url")
            if url:
                urls.append(url)

        # agar kam aaye toh blank fill
        while len(urls) < 10:
            urls.append("")

        rows.append({
            "query_id": idx,
            "query": query,
            "recommended_assessments": urls
        })

    df_out = pd.DataFrame(rows)

    # list ko string bana dete hain (CSV friendly)
    df_out["recommended_assessments"] = df_out["recommended_assessments"].apply(
        lambda x: "; ".join(x)
    )

    df_out.to_csv("final_submission.csv", index=False)
    print("✅ Final CSV generated: final_submission.csv")


if __name__ == "__main__":
    generate_final_csv()
