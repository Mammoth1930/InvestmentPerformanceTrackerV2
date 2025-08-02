SELECT *
FROM read_csv_auto('{{ var("raw_trades_path") }}')