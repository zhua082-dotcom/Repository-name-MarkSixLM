# Repository-name-MarkSixLM
MarkSixLM/
│
├── engine/
├── backtest/
├── training/
├── data/
├── weights/
├── output/
├── config/
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
Mark Six Lottery Prediction Engine
history.csv
MarkSixLM/data/history.csv
https://www.python.org/downloads/
Python 3.11+
source .venv/bin/activate
requirements.txt
pandas
numpy
scipy
scikit-learn
openpyxl
matplotlib
pip install -r requirements.txt
engine/

history_loader.py

feature_store_engine.py

gap_engine.py

trend_engine.py

lifecycle_engine.py

long_strength_engine.py

recovery_engine.py

recovery_score_engine.py

recovery_transition_engine.py

recovery_matrix_engine.py

prediction_engine.py

adaptive_score_engine.py

calibration_engine.py

bayesian_engine.py
MarkSixLM/engine/
git status
git add .
git commit -m "Sprint23 complete"
git push origin main
python training/train.py
HistoryLoader

↓

FeatureStore

↓

State

↓

Transition

↓

Recovery

↓

Prediction

↓

RollingBacktest

↓

Adaptive
python main.py --predict 218
更新history.csv
        │
        ▼
git pull
        │
        ▼
python training/retrain.py
        │
        ▼
python main.py --predict XXX
        │
        ▼
git add .
git commit
git push
