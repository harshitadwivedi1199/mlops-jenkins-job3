FROM centos:latest

RUN yum install python36 -y

RUN pip3 install pandas sklearn

COPY salary_pred.py .

COPY Salary_data.csv .

CMD python3 salary_pred.py


