FROM fedora:25

RUN dnf update -y && dnf install libstdc++ -y && dnf clean all
RUN dnf install gcc gcc-c++ zlib zlib-devel libffi-devel wget make -y

RUN cd /usr/src \
    && wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz \
    && tar xzf Python-3.7.1.tgz \
    && cd Python-3.7.1 \
    && ./configure --enable-optimizations \
    && make altinstall \
    && python3.7 -V

RUN ldd --version

RUN cd /var \
    && touch flag \
    && chmod 777 flag

COPY . Aleksej_Samarin/
CMD ["python3.7", "Aleksej_Samarin/hw.py"]