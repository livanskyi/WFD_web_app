from models.isolation_forest.IsolationForest import IsolationForestDetector
from models.random_forest.RandomForest import RandomForestDetector
import os
import pandas as pd
import time


def run_model_detection(user_path, configs):
    threshold = configs['threshold']
    models_list = configs['models']
    data = __read_files_into_dataframe(user_path)

    # TODO: more models
    # data = __data_preprocessing(data)
    # detector = IsolationForestDetector(data)
    # prediction = detector.detect_anomaly()
    # result_data = __preparing_result_data(prediction, threshold)
    result_data = data

    result_filename = __saving_result_file(result_data, user_path)
    return result_filename


def __read_files_into_dataframe(user_path):
    data = None
    for f in os.listdir(user_path):
        data_f = pd.read_csv(f'{user_path}{f}', sep=';')
        if data is None:
            data = data_f.copy()
            continue
        data = data.append(data_f, ignore_index=True)
    return data


def __data_preprocessing(data):
    pass


def __preparing_result_data(data, threshold):
    pass


def __saving_result_file(result_data, user_path):
    name = f'fraud_prediction-{int(time.time())}'
    result_data.to_csv(os.path.join(user_path, name))
    return name

