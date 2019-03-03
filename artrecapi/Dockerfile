FROM python:3.6
MAINTAINER Evan Goodwin "evansgoodwin@gmail.com"
RUN mkdir -p /home/project/artrecapi
WORKDIR /home/project/artrecapi
COPY requirements.txt /home/project/artrecapi
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/artrecapi

ENV AUTHOSECRETKEY='Mulwxn4IbM9-wyzkAZrwlKAV4a_JfE3ksOZZAHIO8alyWIUvpAg0xVlSL6JEy1yP'
ENV AWSSECRETKEY='S14VBczNUFRpj58hSM6y18bBUh21ME7r2lb7DvG5'
ENV CLIENTID='cpi9d80OLzSVvvu2xfokE77UOZlqFt6P'
ENV SECRETKEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
ENV SPEECHAPI='AIzaSyAz3Fdl3RpA5T8B-etlMoc60ya75xHAqus'
ENV DBSERVER='13.57.196.128:8484'
ENV AWSACCESSKEY=AKIAJM32EA7YZSN5OCSQ
ENV AWSSECRETKEY_key=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

ENV aws_access_key_id=AKIAJM32EA7YZSN5OCSQ
ENV aws_secret_access_key=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
ENV dbname=langalearn
ENV dbuser=ymroddi
ENV dbhost=lango84.cukbl7fyxfht.us-west-1.rds.amazonaws.com
ENV dbpassword=royallord8413
