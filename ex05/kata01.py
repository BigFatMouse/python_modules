kata = {
'Python': 'Guido van Rossum',       # Python was created by Guido van Rossum
'Ruby': 'Yukihiro Matsumoto',       # Ruby was created by Yukihiro Matsumoto
'PHP': 'Rasmus Lerdorf',            # PHP was created by Rasmus Lerdorf
}
print('\n'.join(f"{key} was created by {value}" for key, value in kata.items()))