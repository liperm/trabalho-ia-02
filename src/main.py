from dto.game import Game
from proximity import Proximities
import pandas as pd
from consts import *


def parse_input()-> Game:
  game = Game()
  with open('input.txt', 'r') as file:
    for line in file:
      key, value = line.strip().split(': ')
      setattr(game, key, value.lower())

  return game


def parse_case(case: pd.DataFrame)-> Game:
  game = Game()

  categories = case['categories'].split(';')
  game.category = []
  for category in categories:
    game.category.append(category.lower())

  genres = case['genres'].split(';')
  game.genre = []
  for genre in genres:
    game.genre.append(genre.lower())

  game.developer = case['developer'].lower()
  game.platform = case['platforms'].lower()
  game.publisher = str(case['publisher']).lower()
  game.release_date = case['release_date'].lower()
  game.required_age = int(case['required_age'])
  return game


def get_max_proximity(
  parameter_to_compare: str, 
  parameters: list, 
  proximity_dataframe: pd.DataFrame):
  candidates = []
  for p in parameters:
    try:
      proximity = proximity_dataframe[parameter_to_compare][p]
      candidates.append(proximity)
    except KeyError:
      print(f'combination {parameter_to_compare}/{p} is not mapped')

  return max(candidates)


def main():
  input: Game = parse_input()
  category_proximity_dataframe = Proximities.category()
  genre_proximity_dataframe = Proximities.genre()
  required_age_proximity_dataframe = Proximities.required_age()

  cases: pd.DataFrame = pd.read_csv('steam.csv')
  cases.insert(len(cases.axes[1]), 'total_proximity', 0.0 , True)
  for index, row in cases.iterrows():
    current_case = parse_case(row)

    category_proximity = get_max_proximity(
      input.category, 
      current_case.category, 
      category_proximity_dataframe) * CATEGORY_WEIGHT
    genre_proximity = get_max_proximity(
      input.genre, current_case.genre, genre_proximity_dataframe) * GENRE_WEIGHT
    required_age_proximity = required_age_proximity_dataframe[int(input.required_age)][current_case.required_age] * REQUIRED_AGE_WEIGHT

    plataform_proximity = 0.0
    if input.platform in current_case.platform:
      plataform_proximity = 1.0 * PLATFORM_WEIGHT

    developer_proximity = 0.0
    if input.developer == current_case.developer:
      developer_proximity = 1.0 * DEVELOPER_WEIGHT

    publisher_proximity = 0.0
    if input.publisher == current_case.publisher:
      publisher_proximity = 1.0 * PUBLISHER_WEIGHT

    total_proximity = (
      category_proximity + 
      genre_proximity + 
      required_age_proximity + 
      plataform_proximity + 
      developer_proximity + 
      publisher_proximity)/WEIGHT_SUM

    cases.at[index, 'total_proximity'] = total_proximity

  cases.sort_values(by=['total_proximity'], inplace=True, ascending=False)
  print(f'CASO DE ENTRADA: {vars(input)}\n')
  print(f'PESOS:\ndeveloper: {DEVELOPER_WEIGHT}\npublisher: {PUBLISHER_WEIGHT}\nplatform: {PLATFORM_WEIGHT}\nrequired_age: {REQUIRED_AGE_WEIGHT}\ncategory: {CATEGORY_WEIGHT}\ngenre: {GENRE_WEIGHT}\n')
  print(f'CASOS POR ORDEM DE SIMILARIDADE: {cases}')

if __name__ == '__main__':
  main()

