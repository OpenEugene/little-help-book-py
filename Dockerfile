FROM mvpstudio/python:3 as base
COPY . /home/mvp/app
RUN pip3 install requests
RUN pip3 install requests
RUN pip3 install openpyxl
RUN pip3 install Flask
USER mvp
WORKDIR /home/mvp/app
EXPOSE 80
EXPOSE 443
EXPOSE 5000
# CMD python3 endpoint.py
# ENTRYPOINT python3 endpoint.py
