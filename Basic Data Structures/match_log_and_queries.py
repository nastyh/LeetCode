def match_logs_to_queries(logs, queries):
    """
    O(n_q * w_q * n_l * w_l)
    n_q -- num of queries, w_q -- num of words per query
    n_l -- num of logs
    w_l -- av num of words per log

    O(L+Q+M), L, Q -- split versions of logs and queries
    M -- size of all matches
    Matches logs to queries by checking if a query term is a substring of a log entry.
    :param logs: List of log strings.
    :param queries: List of query strings.
    :return: Dictionary mapping each query term to a list of matching logs.
    """
    matches = {}
    # Split logs and queries into words
    split_logs = [log.split() for log in logs]
    split_queries = [query.split() for query in queries]

    # Flatten and create mappings
    for query in split_queries:
        for query_word in query:  # Match each word in the query
            matches[query_word] = [
                log for log in logs if any(query_word in word for word in log.split())
            ]
    
    return matches