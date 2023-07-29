from Task2 import get_dirs_json, write_json, write_csv, write_pickle
if __name__ == '__main__':

    dict_json = get_dirs_json('C:\Makarov\Python2\Seminar\Homework\Homework8')
    write_json('info_json.json', dict_json)
    write_csv('info_csv.csv', dict_json)
    write_pickle('info_picle.pickle', dict_json)