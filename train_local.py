import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping


early_stopper = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

print("Initializing Local AI Training Sequence...")

# Define Local Paths, 7 emotion folders
dataset_path = r'C:\Users\yunzhanlee\desktop\python_ai_trainer\dataset'

# Check the path exists to prevent instant crashes
if not os.path.exists(dataset_path):
    print(f"--> ERROR: Cannot find dataset at {dataset_path}")
    exit()


# Set Up Data Generators
print("\nScanning Local Images...")
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2 # Reserves 20% for testing
)

train_generator = datagen.flow_from_directory(
    dataset_path,
    target_size=(48, 48),    
    color_mode='grayscale',  
    batch_size=64,
    class_mode='categorical',
    subset='training'
)

validation_generator = datagen.flow_from_directory(
    dataset_path,
    target_size=(48, 48),
    color_mode='grayscale',
    batch_size=64,
    class_mode='categorical',
    subset='validation'
)


# Build the Neural Network Architecture
print("\nBuilding AI Architecture...")
model = Sequential()

# Block 1
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# Block 2
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# Block 3
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

#Flatten and Output
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax')) # 7 Output nodes


# Compile and Train the Model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print("\nStarting Training (This may take a while on a CPU)...")
history = model.fit(
    train_generator,
    epochs=100, 
    validation_data=validation_generator,
    callbacks=[early_stopper]
)


# Save the Final Model
save_path = r'C:\Users\yunzhanlee\desktop\python_ai_trainer\local_emotion_model_2.keras'
model.save(save_path)

print("\n=========================================")
print(f"✅ Success! Local model saved to: {save_path}")
print("IMPORTANT: Class Label Mapping:")
print(train_generator.class_indices)
print("=========================================")