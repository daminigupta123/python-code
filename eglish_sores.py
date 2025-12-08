

import pandas as pd

def find_top_performers(
    csv_path,
    subject_value='English',
    test_type_value='Original',
    score_column='score',
    subject_column='subject',
    test_type_column='test_type',
    top_n=10,
    output_csv=None
):
    # read CSV
    df = pd.read_csv(csv_path)

    # normalize strings for robust matching
    df[subject_column] = df[subject_column].astype(str).str.strip().str.lower()
    df[test_type_column] = df[test_type_column].astype(str).str.strip().str.lower()

    subject_val = str(subject_value).strip().lower()
    test_type_val = str(test_type_value).strip().lower()

    # filter
    filtered = df[
        (df[subject_column] == subject_val) &
        (df[test_type_column] == test_type_val)
    ].copy()

    if filtered.empty:
        print("No rows matched the subject/test_type filter.")
        return filtered  # empty DataFrame

    # ensure score is numeric
    filtered[score_column] = pd.to_numeric(filtered[score_column], errors='coerce')
    filtered = filtered.dropna(subset=[score_column])

    # sort descending by score
    filtered = filtered.sort_values(by=score_column, ascending=False)

    # top N (or all if fewer)
    top = filtered.head(top_n).reset_index(drop=True)

    print(f"Top {min(len(top), top_n)} performers in '{subject_value}' / '{test_type_value}':")
    # print a simple table
    print(top.to_string(index=False))

    if output_csv:
        top.to_csv(output_csv, index=False)
        print(f"Saved top performers to: {output_csv}")

    return top

# Example usage:
if __name__ == "__main__":
    # change paths and parameters as needed
    top_df = find_top_performers(
        csv_path="results.csv",
        subject_value="English",
        test_type_value="Original",
        score_column="score",
        subject_column="subject",
        test_type_column="test_type",
        top_n=20,
        output_csv="top_english_original.csv"
    )
