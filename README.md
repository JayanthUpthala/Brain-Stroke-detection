# Brain Stroke Detection

This project is a Brain Stroke Detection system built with Django and machine learning models. It includes a web application for uploading a hemorrhage dataset, selecting classification models, evaluating performance, and predicting stroke risk using patient scan data.

## Project Structure

- `/Front end/brain/`
  - Django project and app files
  - `brain/` - Django project configuration
  - `brainapp/` - Django application containing views, forms, templates, static assets, and URL routes
- `/back end/dia.ipynb`
  - Jupyter notebook for dataset exploration, preprocessing, model training, and evaluation
- `CODE AND DOC/back end/hemorrhage_diagnosis.csv`
  - Example dataset used to train and test the model

## Features

- User registration and login
- CSV dataset upload via the web interface
- Dataset preview and basic view page
- Multiple classification models supported:
  - K-Nearest Neighbors
  - Logistic Regression
  - Gaussian Naive Bayes
  - Decision Tree
  - Random Forest
  - MLP Neural Network
  - Support Vector Classifier
  - CatBoost Classifier
- Data balancing using SMOTE before training
- Stroke risk prediction from direct input values
- Output message shows whether there is a risk of a brain stroke

## Dependencies

Recommended Python packages:

- Django
- pandas
- scikit-learn
- catboost
- imbalanced-learn

Optional packages used in the notebook:

- seaborn
- matplotlib

## Setup Instructions

### Prerequisites
Ensure you have Python 3.x installed. You can install the necessary dependencies using:

Bash
pip install pandas numpy scikit-learn matplotlib seaborn
### Installation & Usage
Clone the repository:

Bash
git clone https://github.com/JayanthUpthala/Brain-Stroke-detection.git
Navigate to the directory:

Bash
cd Brain-Stroke-detection
Run the Analysis:
Open the Jupyter Notebook or run the main script:

Bash
jupyter notebook

## Usage

1. Register a new user or log in with an existing account.
2. Upload the hemorrhage dataset at the `Load` page.
3. View the uploaded data on the `View` page.
4. Evaluate model performance on the `Modules` page by selecting an algorithm.
5. Use the `Prediction` page to enter scan values and get a stroke risk result.

## Notes

- The model is trained at runtime for each prediction and module evaluation request.
- The prediction form expects values for the following features:
  - `PatientNumber`
  - `SliceNumber`
  - `Intraventricular`
  - `Intraparenchymal`
  - `Subarachnoid`
  - `Epidural`
  - `Subdural`
  - `No_Hemorrhage`
- The target label used for training is `Fracture_Yes_No`.

## Important Files

- `/Front end/brain/brainapp/views.py` - Main application logic and model training/prediction flow
- `/Front end/brain/brainapp/templates/prediction.html` - Prediction input form
- `/back end/dia.ipynb` - Notebook for dataset analysis and model evaluation

## Limitations

- Not configured for production deployment.
- Model training happens on demand, which may be slow for large datasets.
- Sensitive data handling and security settings should be reviewed before deployment.

## Contact

Jayanth Upthala - jayanth.upthala@gmail.com

