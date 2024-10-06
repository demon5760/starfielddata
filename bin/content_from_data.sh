#!/usr/bin/env bash

DATA_DIR="$(pwd)/data"
CONTENT_DIR="$(pwd)/content"

SLATES_DATA_DIR="${DATA_DIR}/slates"
SLATES_CONTENT_DIR="${CONTENT_DIR}/items/slates"
for SLATE_FILE in ${SLATES_DATA_DIR}/*; do
    SLATE_CONTENT_FILE_NAME=$(echo $(basename "${SLATE_FILE}") | sed -e s/yaml/md/g)
    SLATE_CONTENT_FILE_PATH="${SLATES_CONTENT_DIR}/${SLATE_CONTENT_FILE_NAME}"
    if [[ ! -f "${SLATE_CONTENT_FILE_PATH}" ]]; then
        echo "'${SLATE_CONTENT_FILE_PATH}' is missing."
        hugo new content --kind slate "${SLATE_CONTENT_FILE_PATH}"
    fi
done