FROM mcr.microsoft.com/devcontainers/python

RUN useradd -m coder && mkdir -p /home/coder/.cache && chown -R coder:coder /home/coder

# Do all root-level work first
RUN apt-get update \
    && apt-get install -y curl bsdmainutils git \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://codecrafters.io/install.sh | bash

# Install uv as coder so it lands in /home/coder/.local/bin
USER coder
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/home/coder/.local/bin:${PATH}"

WORKDIR /home/coder/codecrafters-kafka-python
COPY --chown=coder:coder pyproject.toml uv.lock .python-version ./

RUN uv sync --frozen

CMD ["bash"]