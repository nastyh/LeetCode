from tensorflow.keras.layers import Input, Embedding, Flatten, Concatenate, Dense
from tensorflow.keras.models import Model

# User input
user_input = Input(shape=(1,), name='user_input')
user_embedding = Embedding(input_dim=num_users, output_dim=embedding_dim)(user_input)
user_flat = Flatten()(user_embedding)

# Item input
item_input = Input(shape=(1,), name='item_input')
item_embedding = Embedding(input_dim=num_items, output_dim=embedding_dim)(item_input)
item_flat = Flatten()(item_embedding)

# Demographic inputs
age_input = Input(shape=(1,), name='age_input')
gender_input = Input(shape=(1,), name='gender_input')
location_input = Input(shape=(1,), name='location_input')

# Product-specific inputs
category_input = Input(shape=(1,), name='category_input')
price_input = Input(shape=(1,), name='price_input')
brand_input = Input(shape=(1,), name='brand_input')

# Combine embeddings and inputs
concatenated = Concatenate()([user_flat, item_flat, age_input, gender_input, location_input, category_input, price_input, brand_input])

# Fully connected layers
fc1 = Dense(64, activation='relu')(concatenated)
fc2 = Dense(32, activation='relu')(fc1)

# Output layer
output = Dense(1, activation='sigmoid')(fc2)

# Compile the model
model = Model(inputs=[user_input, item_input, age_input, gender_input, location_input, category_input, price_input, brand_input], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])