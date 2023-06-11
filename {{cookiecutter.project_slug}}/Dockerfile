FROM python:3.9

WORKDIR /{{cookiecutter.project_slug}}

COPY ./requirements.txt /{{cookiecutter.project_slug}}/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /{{cookiecutter.project_slug}}/requirements.txt

COPY ./app /{{cookiecutter.project_slug}}/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]