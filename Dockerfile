FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /server
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY cookbook ./cookbook
COPY ingredients ./ingredients
COPY manage.py ./
COPY schema.py ./
RUN ["python", "--version"]
RUN ["python", "manage.py","makemigrations"]
RUN ["python", "manage.py","migrate"]
RUN ["python", "manage.py","loaddata", "./ingredients/fixtures/ingredients.json"]
RUN ["ls", "-lah"]
CMD python manage.py runserver 0.0.0.0:$PORT

