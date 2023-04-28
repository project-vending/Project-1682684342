python
import os

class Config:
    """
    Configuration settings for the data engineering project.
    """
    # Define paths
    DATA_DIR = '../data'
    RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw_data')
    PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed_data')
    LOGS_DIR = '../logs'
    LOG_FILE = os.path.join(LOGS_DIR, 'app.log')

    # Define data settings
    SAMPLE_RATE = 0.1 # fraction of data to sample for testing
    TRAIN_TEST_SPLIT = 0.8 # fraction of data to use for training

    # Define model settings
    NUM_FEATURES = 10
    NUM_CLASSES = 2
