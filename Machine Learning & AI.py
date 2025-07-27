# 41. Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 42. Fit model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression().fit(X_train, y_train)

# 43. Predict
preds = model.predict(X_test)

# 44. Accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, preds))

# 45. Normalize data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 46. Load model
import joblib
model = joblib.load('model.pkl')

# 47. Save model
joblib.dump(model, 'model.pkl')

# 48. NLP tokenization
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
tokens = word_tokenize("Hello from MNCs")

# 49. Image processing
from PIL import Image
img = Image.open('pic.jpg').resize((100, 100))

# 50. Use OpenAI or LLM API
import openai
openai.api_key = 'sk-xxx'
openai.ChatCompletion.create(model='gpt-4', messages=[{"role":"user", "content":"Hello"}])
