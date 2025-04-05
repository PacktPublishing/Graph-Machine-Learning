#!/bin/bash

curl -fsSL https://ollama.com/install.sh | sh

ollama -v

ollama pull minicpm-v
ollama pull nomic-embed-text

