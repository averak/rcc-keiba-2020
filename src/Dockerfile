FROM joyzoursky/python-chromedriver:3.8-selenium

ENV TZ='Asia/Tokyo'

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system

RUN ["pipenv", "run", "start"]