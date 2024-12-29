import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Embedding, Concatenate
from tensorflow.keras.models import Model

"""
Input Features:

User features: Demographics, behavior embeddings, historical interactions.
Item features: Metadata, embeddings, latent factors.
Context features: Time, device, location.
Model Design:

Build a shared representation using deep neural networks (e.g., fully connected layers, embeddings).
Add task-specific output layers:
Engagement: Sigmoid activation for binary classification.
Relevance: Linear activation for regression.
Training:

Optimize the combined loss function using a gradient-based optimizer.
Experiment with α and β to balance tasks.

PROBLEMS
Task Imbalance:

Engagement data is often more abundant than relevance data. Weighting the losses appropriately is crucial.
Negative Transfer:

If tasks are too dissimilar, the shared representation might hurt performance. Use techniques like auxiliary losses or task-specific layers to mitigate this.
Evaluation:

Evaluate each task separately (e.g., precision/recall for engagement, RMSE for relevance).
Ensure that optimizing one task does not degrade the other.
"""


# Define input layers
user_input = Input(shape=(1,), name="user_id")
item_input = Input(shape=(1,), name="item_id")
context_input = Input(shape=(10,), name="context_features")

# Embedding layers
user_embedding = Embedding(input_dim=10000, output_dim=32)(user_input)
item_embedding = Embedding(input_dim=10000, output_dim=32)(item_input)

# Shared feature representation
shared_features = Concatenate()([user_embedding, item_embedding, context_input])
shared_features = Dense(64, activation='relu')(shared_features)
shared_features = Dense(32, activation='relu')(shared_features)

# Engagement task head
engagement_output = Dense(1, activation='sigmoid', name="engagement")(shared_features)

# Relevance task head
relevance_output = Dense(1, activation='linear', name="relevance")(shared_features)

# Build model
model = Model(inputs=[user_input, item_input, context_input], outputs=[engagement_output, relevance_output])

# Compile with multi-task loss
model.compile(
    optimizer='adam',
    loss={
        "engagement": "binary_crossentropy",
        "relevance": "mse"
    },
    loss_weights={"engagement": 0.7, "relevance": 0.3}
)

# Summary
model.summary()

# Training example
model.fit(
    [user_ids, item_ids, context_features],
    {"engagement": engagement_labels, "relevance": relevance_scores},
    epochs=10,
    batch_size=32
)

