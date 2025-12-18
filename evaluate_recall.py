from load_company_data import load_company_data
from retrieve_test import recommend


def extract_slug(url):
    if not isinstance(url, str):
        return ""
    return url.rstrip("/").split("/")[-1]


def evaluate_recall_at_10():
    train_df, _ = load_company_data()
    recalls = []

    for i, row in train_df.iterrows():
        query = row["Query"]
        true_url = row["Assessment_url"]
        true_slug = extract_slug(true_url)

        results = recommend(query, top_k=10)

        recommended_slugs = []
        for r in results:
            # 🔑 CORRECT column from metadata.csv
            url = r.get("canonical_url")

            if url:
                recommended_slugs.append(extract_slug(url))

        recall = 1 if true_slug in recommended_slugs[:10] else 0
        recalls.append(recall)

        # 🔍 Debug only for first query
        if i == 0:
            print("GT URL:", true_url)
            print("GT SLUG:", true_slug)
            print("Top slugs:", recommended_slugs[:5])
            print("-" * 40)

    mean_recall = sum(recalls) / len(recalls)
    print(f"\n✅ Mean Recall@10: {mean_recall:.4f}")


if __name__ == "__main__":
    evaluate_recall_at_10()
