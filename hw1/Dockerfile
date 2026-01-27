FROM python:3.13

RUN pip install jupyter pandas fastparquet sqlalchemy psycopg2-binary

# Set working directory
WORKDIR /app
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]