import string
import collections

#Uses BFS to find the least steps of transformation


def transform_string(D, s, t):
    StringWithDistance = collections.namedtuple(
        'StringWithDistance', ('candidate_string', 'distance'))
    q = collections.deque([StringWithDistance(s, 0)])
    del D[s]  # Marks s as visited by erasing it in D.

    while q:
        f = q.popleft()
        # Returns if we find a match:
        if f.candidate_string == t:
            return f.distance  # Number of steps reaches t.

        # Tries all possible transformations of f.candidate_string
        for i in range(len(f.candidate_string)):
            for c in string.ascii_lowercase: #iterates through 'a' - 'z'
                cand = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
                if cand in D:
                    del D[cand]
                    q.append(StringWithDistance(cand, f.distance + 1))
    return -1




D = {
    "cat": 1, "car": 2
}
print(transform_string(D, "cat", "car"))