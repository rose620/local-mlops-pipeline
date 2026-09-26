#!/bin/bash
set -e

echo "🚀 Sending sample payload via cURL..."

response=$(curl -s -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d @sample_payload.json)

echo "🎯 Prediction Response:"
echo "$response"
