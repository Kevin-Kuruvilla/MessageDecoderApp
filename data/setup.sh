pip install --upgrade kaggle
mkdir -p ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
kaggle datasets download -d kazanova/sentiment140
unzip sentiment140
rm sentiment140.zip
mv training.1600000.processed.noemoticon.csv data.csv