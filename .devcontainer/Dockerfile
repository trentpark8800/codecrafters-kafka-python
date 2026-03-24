FROM mcr.microsoft.com/devcontainers/python

RUN useradd -m coder && mkdir -p /home/coder/.cache && chown -R coder:coder /home/coder

RUN apt-get update \
    && apt-get install -y curl bsdmainutils git netcat-traditional xxd \
    && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://codecrafters.io/install.sh | bash

USER coder

WORKDIR /home/coder/codecrafters-kafka-python

COPY --chown=coder:coder pyproject.toml uv.lock .python-version ./

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/home/coder/.local/bin:$PATH"
RUN uv sync

CMD ["bash"]