### Code Refactoring model.ipynb

**Shell scripts**
Shell scripts can be started with `bash {script}`
- `start_jupyterlab.sh`: starts the Jupyter server for model training and creates a Docker volume for models
- `start_model_container.sh`: starts the API for model deployment

Access Jupyter container after running start_jupyterlab.sh at `http://0.0.0.0:10000/`


**data_science_problem**
- `data_science_problem/solutions.ipynb`: contains refactored code for model training & development
- `data_science_problem/data`: contains the CSV files for training and validation
- `data_science_problem/models`: contains the trained models, and is also the Docker volume for the deployment container
- `data_science_problem/test_api.ipynb`: contains a sample notebook for querying the Model Deployment API
- `data_science_problem/docker`: contains Dockerfile and requirements.txt for the container build process

The first step was to refactor the code in model.ipynb. The code was not designed to operate in a professional environment. This involves adding logging for easier error analysis and adopting an OOP approach, making the code easier to unit/integration test and providing better clarity for further development and bug fixing. The refactored code can be found in `solutions.ipynb`.

Each section is now encapsulated in a class:
Initially, all paths and other dependencies are maintained in a Config Class, and all environment variables are stored in a .env file in the root directory. All further steps are packaged in separate classes: DataLoader for data handling, Visualize for all data visualizations, etc.

The next step is setting up the project architecture in Docker, meaning that all MLOps steps are outsourced to individual containers. This provides more control over the entire process since all microservices now run independently. Here, a distinction is mainly made between Model Training and Model Development.

The files `start_jupyterlab.sh` and `start_model_container.sh` each start a container for training and a container for model deployment. The models are stored in a Docker volume created in the `start_jupyterlab.sh` file, which is shared by both containers. This means that once a model is trained and saved, it is immediately available to the deployment container and can be accessed via API.

**MLOPS**

- `mlops_problem/app.py`: Deployment of the model using FastAPI
- `mlops_problem/docker`: contains Dockerfile and requirements.txt for the container build process

It is fundamentally important that training and deployment are separated but can communicate with each other as microservices and share relevant volumes, such as the model volume. Furthermore, in a next step, a model training tracking technology such as MLFlow would be integrated or linked to the Model Training Container.
