from clean import load_data, clean_data

df = load_data()
df_clean = clean_data(df)

X = df_clean.drop("price", axis = 1)
y = df_clean["price"]