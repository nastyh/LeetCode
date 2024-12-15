class KNNRecommender:
    def __init__(self, k, metric='cosine', weighted=True):
        self.k = k
        self.metric = metric
        self.weighted = weighted

    def fit(self, X, y):
        self.X = X  # User-item matrix
        self.y = y  # Ratings
        return self

    def predict_rating(self, user, item):
        neighbors = self.get_neighbors(user)
        if not neighbors:
            return None
        if self.weighted:
            pred = np.sum([self.weighted_rating(neighbor, item) for neighbor in neighbors])
        else:
            pred = np.mean([self.X[neighbor, item] for neighbor in neighbors])
        return round(pred, 2)

    def weighted_rating(self, neighbor, item):
        w = self.similarity(user, neighbor)
        return w * self.X[neighbor, item]

    def similarity(self, user1, user2):
        vec1, vec2 = self.X[user1], self.X[user2]
        if self.metric == 'cosine':
            return np.dot(vec1, vec2) / (np.sqrt(np.dot(vec1, vec1)) * np.sqrt(np.dot(vec2, vec2)))
        elif self.metric == 'pearson':
            return np.corrcoef(vec1, vec2)[0, 1]

    def get_neighbors(self, user):
        distances = [self.similarity(user, other) for other in range(len(X)) if other != user]
        indices = np.argsort(distances)[-self.k:]
        return indices