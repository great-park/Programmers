def solution(citations):
    citations.sort(reverse=True)
    for id, citation in enumerate(citations):
        if id >= citation:
            return id
    return len(citations)
