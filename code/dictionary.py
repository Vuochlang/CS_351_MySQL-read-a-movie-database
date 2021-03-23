import csv
import json


# parse multi-values attributes into dictionaries
class Dictionary:
    def __init__(self):
        self.movie_dictionary = {}  # ('id':{}{})
        self.genre_dictionary = {}  # ('id': 'name')
        self.keywords_dictionary = {}  # ('id': 'name')
        self.production_companies_dictionary = {}  # ('name', 'id')
        self.production_countries_dictionary = {}  # ('iso_3166_1', 'name')
        self.spoken_languages_dictionary = {}  # ('iso_639_1', 'name')

    def create_dictionary(self, file):
        try:
            csv_file = open(file)
        except (FileNotFoundError, FileExistsError):
            print("Error opening the CSV file")
        else:
            # read rows into a dictionary format
            reader = csv.DictReader(csv_file)

            # read each row and parse multi-values attributes
            for row in reader:
                movie_id = row["id"]
                self.movie_dictionary[movie_id] = {}

                genre = row["genres"]
                keyword = row["keywords"]
                pro_company = row["production_companies"]
                pro_country = row["production_countries"]
                language = row["spoken_languages"]

                temp = self.parse_store_to_dict(genre,
                                                key_name='id',
                                                value_name='name')
                self.movie_dictionary[movie_id]["genres"] = list(temp.keys())
                self.genre_dictionary.update(temp)

                temp = self.parse_store_to_dict(keyword,
                                                key_name='id',
                                                value_name='name')
                self.movie_dictionary[movie_id]["keywords"] = list(temp.keys())
                self.keywords_dictionary.update(temp)

                temp = self.parse_store_to_dict(pro_company,
                                                key_name='id',
                                                value_name='name')
                self.movie_dictionary[movie_id]["production_companies"] = list(temp.keys())
                self.production_companies_dictionary.update(temp)

                temp = self.parse_store_to_dict(pro_country,
                                                key_name='iso_3166_1',
                                                value_name='name')
                self.movie_dictionary[movie_id]["production_countries"] = list(temp.keys())
                self.production_countries_dictionary.update(temp)

                temp = self.parse_store_to_dict(language,
                                                key_name='iso_639_1',
                                                value_name='name')
                self.movie_dictionary[movie_id]["spoken_languages"] = list(temp.keys())
                self.spoken_languages_dictionary.update(temp)
            csv_file.close()

    @staticmethod
    def parse_list(string):
        for each in string.split('}, '):
            if each[0] == '[':
                each = each[1:]
            if each[-1] != ']':
                each += "}"
            else:
                each = each[:-1]
            yield each

    # parse data and store as dictionary with given key and value
    # then return dictionary
    def parse_store_to_dict(self, data, key_name, value_name):
        temp_dictionary = {}
        if data == '[]':
            return temp_dictionary
        for i in self.parse_list(data):
            e = json.loads(i)
            temp_dictionary = self.add_to_dict(temp_dictionary, e, key_name,
                                               value_name)
        return temp_dictionary

    @staticmethod
    def add_to_dict(my_dictionary, data, key, value):
        if data[key] not in my_dictionary:
            my_dictionary[data[key]] = data[value]
        return my_dictionary
