#!/bin/bash

curl -fsSL https://ollama.com/install.sh | sudo sh

ollama -v

ollama pull minicpm-v
ollama pull nomic-embed-text

