FROM centos:latest

RUN yum install python36 -y

RUN pip3 install pandas sklearn

RUN mkdir -p /sal_pred

COPY salary_pred.py /sal_pred

COPY Salary_data.csv /sal_pred

CMD python3 salary_pred.py


