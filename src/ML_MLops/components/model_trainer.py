import pandas as pd
import os
from ML_MLOps import logger
from sklearn.linear_model import ElasticNet
import joblib
from ML_MLOps.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        X_train = pd.read_csv(self.config.train_X_path)
        y_train = pd.read_csv(self.config.train_y_path)
        X_test = pd.read_csv(self.config.test_X_path)
        y_test = pd.read_csv(self.config.test_y_path)

        lr = ElasticNet(alpha = self.config.alpha, l1_ratio = self.config.l1_ratio, random_state=42)
        lr.fit(X_train, y_train)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))