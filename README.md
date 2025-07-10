# 🧠 Toxic Comment Detection using Logistic Regression & TF-IDF

This project classifies whether a comment contains **toxic, threatening, or hateful language** using classic NLP + machine learning:

- 🔹 Traditional ML: **TF-IDF + Logistic Regression**
- 🧠 Outputs **natural-language explanation**
- 🖥️ Clean & responsive UI built with **Streamlit**

---


## 📸 Screenshots

### ✅ Non-Toxic Comment Predictions

| Comment 1 | Comment 2 |
|-----------|-----------|
| ![Non-Toxic 1](https://raw.githubusercontent.com/dhruvin6122/Text-Toxicity-Predictor/main/Text-Toxicity-Predictor/screenshorts/nontoxic1.png) | ![Non-Toxic 2](https://raw.githubusercontent.com/dhruvin6122/Text-Toxicity-Predictor/main/Text-Toxicity-Predictor/screenshorts/nontoxic2.png) |

---

### ❌ Toxic Comment Predictions

| Comment 1 | Comment 2 |
|-----------|-----------|
| ![Toxic 1](https://raw.githubusercontent.com/dhruvin6122/Text-Toxicity-Predictor/main/Text-Toxicity-Predictor/screenshorts/toxic1.png) | ![Toxic 2](https://raw.githubusercontent.com/dhruvin6122/Text-Toxicity-Predictor/main/Text-Toxicity-Predictor/screenshorts/toxic2.png) |

---

## 🔍 Features

- 🧠 Logistic Regression with TF-IDF (multi-label classification)
- 💬 Predict 6 toxicity types in 1 go
- 🪄 Smart interpretation like:
  > “This comment appears to be: **Toxic and Hateful**”
- 📊 Confusion matrix & metrics
- ⚖️ Handles imbalanced data
- 🖼️ Streamlit web UI included

---

## 🏷️ Labels Detected

| Label          | Meaning                            |
|----------------|-------------------------------------|
| `toxic`        | Mildly offensive                    |
| `severe_toxic` | Extremely abusive                   |
| `obscene`      | Obscene or vulgar language          |
| `threat`       | Threats of violence or harm         |
| `insult`       | Personal attacks or mockery         |
| `identity_hate`| Hate speech against identity groups |

---

## 🧠 Model Details

### ✅ TF-IDF + Logistic Regression
- Uses `TfidfVectorizer` with unigrams & bigrams
- One model per label (multi-label)
- Optimized with `class_weight='balanced'`
- Thresholding applied for label confidence
- Fully interpretable

---

## 🧪 Test Examples

| Comment                                                              | Predicted Labels                     |
|----------------------------------------------------------------------|--------------------------------------|
| "You’re such a dumb loser."                                          | `toxic`, `insult`                    |
| "F*** you and your stupid face."                                     | `toxic`, `obscene`                   |
| "I’ll find you and break your legs."                                 | `toxic`, `threat`                    |
| "Thanks for your help, I really appreciate it."                      | _(None - clean)_                     |
| "People from your race are filth."                                   | `identity_hate`, `toxic`             |

---

## 📥 Dataset

Used the official **Jigsaw Toxic Comment Classification Challenge** dataset.

📎 [Download from Kaggle](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/data)

---

## 🛠️ Tech Stack

| Layer         | Tools / Libraries                           |
|---------------|----------------------------------------------|
| Language      | Python 3.x                                   |
| UI            | Streamlit                                    |
| NLP           | NLTK, Scikit-learn                           |
| Vectorization | TF-IDF                                       |
| Model         | Logistic Regression                          |
| Deployment    | Streamlit Cloud / Local                      |



---

## 🔮 Future Enhancements

- 🤖 Add Random Forest & XGBoost comparisons
- 🧬 Transformer-based classifier (BERT)
- 🔍 Model interpretability with SHAP
- 🛡️ Toxicity severity score
- 🧪 Batch CSV prediction upload
- ☁️ Cloud deployment (Streamlit Cloud or Hugging Face)

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
Feel free to use, modify, and distribute with credit.

---

## 🙋‍♂️ Author

**Dhruvin Patel**  
🎓 B.Tech – Computer Science  
📍 Gujarat, India  
📧 Email: pateldhruvin6122@gmail.com  
🔗 GitHub: [@dhruvin6122](https://github.com/dhruvin6122)  
💼 LinkedIn: [View Profile](https://www.linkedin.com/in/patel-dhruvin-70b602280)
