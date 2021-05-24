
FROM python:slim
CMD pip install cython
COPY *.py ./
COPY ./extensions/* ./extensions/
CMD cd ./extensions && python setup.py build_ext --inplace
CMD python batch_analysis.py

