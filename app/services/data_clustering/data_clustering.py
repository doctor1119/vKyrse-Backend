from sklearn.cluster import KMeans

import json
import warnings
warnings.simplefilter(action='ignore')

# from app.services.data_collection.collect_articles import articles_to_dataframe
from app.services.data_processing.preprocess_articles_v2 import preprocess_articles_v2


def clusterize_articles(pandas_dataframe):
    NUM_CLUSTERS, corpus_embeddings, data = preprocess_articles_v2(pandas_dataframe)
    clustering_model = KMeans(n_clusters=NUM_CLUSTERS)
    clustering_model.fit(corpus_embeddings)
    cluster_assignment = clustering_model.labels_

    data['cluster_id'] = cluster_assignment
    # Добавим имена кластеров и факторы влияния, на данный момент оставим имена пустыми
    cluster_names = {i: "" for i in range(NUM_CLUSTERS)}
    impact_factors = {i: 0.0 for i in range(NUM_CLUSTERS)}

    data['cluster_name'] = data['cluster_id'].map(cluster_names)
    data['impact_factor'] = data['cluster_id'].map(impact_factors)

    return data


def convert_to_json(data):
    json_result = json.loads(data.to_json(orient='records', force_ascii=False))
    return json_result
