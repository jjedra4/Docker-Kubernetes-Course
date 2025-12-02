FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["jupyter", "notebook", "--port", "8888", "--no-browser", "--ip", "0.0.0.0", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
