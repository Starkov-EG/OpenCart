FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT pytest ./tests/test_page_object_dk.py --alluredir allure-results
