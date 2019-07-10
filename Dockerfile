FROM python:3.7.4

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./api.py ./linear_regression_model.joblib /app/

ENTRYPOINT [ "python" ]
CMD [ "api.py", "linear_regression_model.joblib" ]