#!/bin/bash

# https://stackoverflow.com/questions/59895/how-can-i-get-the-source-directory-of-a-bash-script-from-within-the-script-itsel
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "${SCRIPT_DIR}/weather"

# check if file exists (e.g. in CI cache)
sha256sum -c checksums.sha256
if [[ $? == 0 ]]; then
  echo "Data already downloaded."
  exit 0
else
  echo "Downloading data..."
fi

# download an extract data files
wget https://hep.tsinghua.edu.cn/~meowmeow/physics-data/terrain/dataset.tar.gz -O - | tar -xzf -

# check if download succeeds
sha256sum -c checksums.sha256
if [[ $? != 0 ]]; then
  echo "Checksum failed. Please run this script again."
  exit 1
fi
