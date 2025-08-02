import pandas as pd

def ingest_xlsx_brokerage_data(file_path: str) -> pd.DataFrame:
    """
    Ingests brokerage data from an Excel file and returns a DataFrame.
    
    Args:
        file_path (str): The path to the Excel file containing brokerage data.
        
    Returns:
        pd.DataFrame: A DataFrame containing the ingested brokerage data.
    """
    try:
        df = pd.read_excel(file_path, sheet_name='Sheet1', engine='openpyxl')
        return df
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return pd.DataFrame()
    

# Ingest raw xlsx data and write to csv
xlsx_df = ingest_xlsx_brokerage_data(r'C:\InvestmentPerformanceTrackerV2\data\raw\xlsx\us_stock_trades.xlsx')
xlsx_df.to_csv(r'C:\InvestmentPerformanceTrackerV2\data\raw\csv\us_stock_trades.csv',index=False)
