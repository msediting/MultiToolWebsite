#!/bin/bash

# Create a zip file of the whole project
echo "Creating production zip file of MultiTools..."

# Create a timestamp for the zip file
timestamp=$(date +"%Y%m%d_%H%M%S")
zip_file="multitools_production_$timestamp.zip"

# Files and directories to include
zip -r "$zip_file" \
    app.py \
    main.py \
    wsgi.py \
    .htaccess \
    requirements-production.txt \
    README.md \
    static/ \
    templates/

echo "Production zip file created: $zip_file"
echo "You can download this file and deploy it on your Hostinger server."