import click
import pandas as pd
from categorization.models.sklearn.sk_models import Categorizer

from dotenv import load_dotenv
import os
load_dotenv()

model_file = '../saved_models/model.pkl'

@click.command(name='train_model')
@click.option('--model_name', '-m',
              type=click.Choice(os.getenv('VALID_MODELS').split(",")),
              help='Name of the model to be trained.')

def train_model(model_name):
    print('Getting data...')

    df = pd.read_csv(f'{os.getenv("DATA_FOLDER")}/{os.getenv("LOCAL_FILE_NAME")}')

    selected_categories=[
        'Account management',
        'Design',
        'Strategy',
        'Creative',
        'Software & UX/UI',
        'Social Media'
        ]

    df['category_name']=df['category_name'].apply(lambda x: x if x in selected_categories else 'Others')

    X = df['document_dirty']

    y = df['category_name']

    model = Categorizer(model_name=model_name)

    print('Training model...')
    
    model.fit(X, y)

    print('Model succesfully trained!')

    print('Model metadata: ', model.get_metadata())
    
    task = ['campana de marketing digital en redes']

    prediction = model.predict(task)

    print(f'Prediction Test completed:\ntask = {task}, predicted category = {prediction}')

    model.save_model(model_file)

if __name__ == '__main__':
    train_model()
