FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/jeehyunkim0510/doshisanjo.git

RUN echo


WORKDIR /home/doshisanjo/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-ta=w7bx=k*u0w_$lef4#z0d&^ptbp0=gj%wuk5$2x_tzc4&a9e" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]