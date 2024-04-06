FROM python
WORKDIR /myapp

#COPY ./myapp.py .

#COPY ./servers.txt .
#CMD ["python", "myapp.py"]
##COPY ./api_demo.py .
#RUN pip install requests
#CMD ["python" ,"api_demo.py"]



COPY dataBase.py .
RUN pip install pymysql
CMD ["python" , "dataBase.py"]
