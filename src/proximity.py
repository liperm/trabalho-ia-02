import pandas as pd

category_proximities = {
  'index': ['single-player', 'online multi-player', 'local multi-player', 'online co-op', 'local co-op', 'single e multi'],
  'single-player': [1.0, 0.0, 0.2, 0.2, 0.2, 0.9],
  'online multi-player': [0.0, 1.0, 0.5, 0.7, 0.2, 1.0],
  'local multi-player': [0.2, 0.5, 1.0, 0.2, 0.7, 1.0],
  'online co-op': [0.2, 0.7, 0.2, 1.0, 0.8, 0.5],
  'local co-op ': [0.2, 0.2, 0.7, 0.8, 1.0, 0.5],
  'single e multi': [0.9, 1.0, 1.0, 0.5, 0.5, 1.0]
}

genre_proximities = {
  'index': ['action', 'strategy', 'rpg', 'adventure', 'simulation', 'racing', 'sports'],
  'action': [1, 0.4, 0.3, 0.7, 0.1, 0, 0],
  'strategy': [0.4, 1, 0.9, 0.6, 0.3, 0, 0.1],
  'rpg': [0.3, 0.9, 1, 0.7, 0, 0.1, 0.1],
  'adventure': [0.7, 0.6, 0.7, 1, 0.1, 0.3, 0],
  'simulation': [0.1, 0.3, 0, 0.1, 1, 0.8, 0.9],
  'racing': [0, 0, 0.1, 0.3, 0.8, 1, 0.7],
  'sports': [0, 0.1, 0.1, 0, 0.9, 0.7, 1]
}

required_age_proximities = {
  'index': [3, 7, 12, 16, 18, 0],
  3: [1, 0.8, 0.6, 0.4, 0.2, 0.8],
  7: [0.8, 1, 0.8, 0.6, 0.4, 0.6],
  12: [0.6, 0.6, 1, 0.8, 0.6, 0.4],
  16: [0.4, 0.4, 0.8, 1, 0.8, 0.2],
  18: [0.2, 0.2, 0.6, 0.8, 1, 0],
  0: [0.8, 0.6, 0.4, 0.2, 0, 1]
}


class Proximities:
  def __get_df(dic)-> pd.DataFrame:
    df = pd.DataFrame(dic)
    df = df.set_index('index')
    return df

  def category()-> pd.DataFrame:
    return Proximities.__get_df(category_proximities)

  def genre()-> pd.DataFrame:
    return Proximities.__get_df(genre_proximities)

  def required_age()-> pd.DataFrame:
    return Proximities.__get_df(required_age_proximities)

print(Proximities.category().keys())