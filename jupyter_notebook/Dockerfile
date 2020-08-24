FROM python:3.7.3-slim

LABLE maintainer='Bikram'
LABLE version="0.1"
LABLE description=" Jupyter Notebook & Data (.csv file) to provide a summary "

WORKDIR /data

COPY .  /data

RUN pip install numpy pandas seaborn jupyter

EXPOSE  9999

CMD ["jupyter","notebook","--ip=0.0.0.0","--port=9999","--no-browser","--allow=root"]
