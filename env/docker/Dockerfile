ARG PYVER=3.9
FROM python:3.9-alpine
SHELL ["ash", "-c"]
ARG GECKO_VER=0.29.0
COPY py/requirements.txt .
RUN \
  apk add \
  firefox \
  ttf-dejavu \
  ttf-liberation \
  font-noto-cjk \
  font-noto-emoji \
  && pip install -qr requirements.txt \
  && rm requirements.txt \
  && wget https://github.com/mozilla/geckodriver/releases/download/v${GECKO_VER}/geckodriver-v${GECKO_VER}-linux64.tar.gz \
  && tar -C /usr/bin/ \
  -xvzf geckodriver*.tar.gz \
  && rm geckodriver* \
  && chmod +x /usr/bin/geckodriver