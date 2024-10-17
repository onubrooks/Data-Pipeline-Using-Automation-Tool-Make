import pandas as pd
from transform import convert_numeric, handle_missing_values, handle_outliers, transform_data, aggregate_data

def etl(data, numeric_cols):
    df = pd.DataFrame(data)

    # transforms

    df = convert_numeric(df, numeric_cols)
    handle_missing_values(df)
    df = handle_outliers(df)
    df = transform_data(df)

    # df_aggregated = aggregate_data(df)

    return df.to_dict(orient='records')
    