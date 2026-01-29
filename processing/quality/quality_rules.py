def validate_not_null(df, columns):
    for col in columns:
        if df[col].isnull().any():
            raise ValueError(f"Null values detected in column: {col}")

def validate_positive_values(df, column):
    if (df[column] <= 0).any():
        raise ValueError(f"Non-positive values detected in column: {column}")

def validate_date_parsing(df, column):
    if df[column].isnull().any():
        raise ValueError(f"Invalid dates found in column: {column}")
