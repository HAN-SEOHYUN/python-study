FROM python:3

CMD ["/bin/bash"]

WORKDIR /app

RUN pip3 install streamlit

COPY ./src ./