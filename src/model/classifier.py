import os
import sys
import numpy as np
from PIL import Image, ImageOps

# Suppress TensorFlow verbose logging
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

class RPSClassifier:
    """
    Clasificador de gestos de Piedra, Papel o Tijera utilizando
    un modelo pre-entrenado exportado desde Keras / Teachable Machine.
    """
    def __init__(self, model_path: str = None, labels_path: str = None):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        default_folder = os.path.join(base_dir, "converted_keras (Piedra-Papel-Tijera)")
        
        self.model_path = model_path or os.path.join(default_folder, "keras_model.h5")
        self.labels_path = labels_path or os.path.join(default_folder, "labels.txt")
        self.model = None
        self.labels = self._load_labels()
        self._load_model()

    def _load_labels(self):
        labels = []
        if os.path.exists(self.labels_path):
            with open(self.labels_path, "r", encoding="utf-8") as f:
                for line in f:
                    cleaned = line.strip()
                    if not cleaned:
                        continue
                    # Format typically: "0 Piedra" or just "Piedra"
                    parts = cleaned.split(" ", 1)
                    if len(parts) > 1 and parts[0].isdigit():
                        labels.append(parts[1].strip())
                    else:
                        labels.append(cleaned)
        if not labels:
            labels = ["Piedra", "Papel", "Tijera"]
        return labels

    def _load_model(self):
        # Try tf_keras first, then fallback to tensorflow.keras
        try:
            import tf_keras as keras
            self.model = keras.models.load_model(self.model_path, compile=False)
            return
        except Exception:
            pass

        try:
            import tensorflow as tf
            self.model = tf.keras.models.load_model(self.model_path, compile=False)
            return
        except Exception as e:
            raise RuntimeError(f"Error cargando modelo Keras desde {self.model_path}: {e}")

    def preprocess_image(self, image: Image.Image, target_size=(224, 224)) -> np.ndarray:
        """
        Preprocesa la imagen de entrada:
        - Conversión a RGB
        - Redimensionamiento y recorte centrado a 224x224
        - Normalización a rango [-1, 1]
        """
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # Fit image maintaining aspect ratio
        fitted_image = ImageOps.fit(image, target_size, Image.Resampling.LANCZOS)
        
        image_array = np.asarray(fitted_image, dtype=np.float32)
        # Teachable Machine normalization: (x / 127.5) - 1.0
        normalized_image = (image_array / 127.5) - 1.0
        
        # Expand dimensions to batch format: (1, 224, 224, 3)
        data = np.expand_dims(normalized_image, axis=0)
        return data

    def predict(self, image: Image.Image):
        """
        Realiza la predicción sobre una imagen PIL.
        Retorna diccionario con predicción principal, confianza y probabilidades por clase.
        """
        data = self.preprocess_image(image)
        prediction = self.model.predict(data, verbose=0)[0]
        
        class_idx = int(np.argmax(prediction))
        confidence = float(prediction[class_idx])
        predicted_label = self.labels[class_idx] if class_idx < len(self.labels) else f"Clase {class_idx}"
        
        probabilities = {
            self.labels[i] if i < len(self.labels) else f"Clase {i}": float(prediction[i])
            for i in range(len(prediction))
        }
        
        return {
            "label": predicted_label,
            "confidence": confidence,
            "class_index": class_idx,
            "probabilities": probabilities
        }
