import random

# Define word banks by POS tag
determiners = ['The', 'A', 'That', 'This', 'These']
nouns = ['dog', 'cat', 'bird', 'car', 'robot', 'man', 'woman', 'child', 'apple']
verbs = ['runs', 'jumps', 'sleeps', 'barks', 'drives', 'flies', 'eats', 'thinks']
adjectives = ['big', 'small', 'happy', 'angry', 'blue', 'fast', 'quiet']

# POS tag mappings
pos_tags = {
    'determiners': 'DT',
    'nouns': 'NN',
    'verbs': 'VB',
    'adjectives': 'JJ'
}

# Sentence templates (sequence of POS roles)
templates = [
    ['determiners', 'nouns', 'verbs'],
    ['determiners', 'adjectives', 'nouns', 'verbs'],
    ['determiners', 'nouns', 'verbs', 'adverbs'],
    ['determiners', 'nouns', 'verbs', 'determiners', 'nouns']
]

# Optional adverb list
adverbs = ['quickly', 'loudly', 'quietly', 'suddenly']
pos_tags['adverbs'] = 'RB'

# Extend word bank for random selection
word_bank = {
    'determiners': determiners,
    'nouns': nouns,
    'verbs': verbs,
    'adjectives': adjectives,
    'adverbs': adverbs
}

# Function to generate a single sentence
def generate_sentence(template):
    sentence = []
    for part in template:
        word = random.choice(word_bank[part])
        tag = pos_tags[part]
        sentence.append((word, tag))
    return sentence

# Generate synthetic dataset
def generate_dataset(n=100):
    dataset = []
    for _ in range(n):
        template = random.choice(templates)
        sentence = generate_sentence(template)
        dataset.append(sentence)
    return dataset

# Example: Generate 100 synthetic training sentences
synthetic_training_data = generate_dataset(100)
training_data = synthetic_training_data


from collections import defaultdict, Counter
# Filter uniq
def get_initial_tags(data):
    word_tag_freq = defaultdict(Counter)
    for sentence in data:
        for word, tag in sentence:
            word_tag_freq[word][tag] += 1

    # Assign most frequent tag
    most_freq_tag = {}
    for word in word_tag_freq:
        most_freq_tag[word] = word_tag_freq[word].most_common(1)[0][0]
    return most_freq_tag


def baseline_tag(sentence, tag_dict):
    return [(word, tag_dict.get(word, 'NN')) for word, _ in sentence]  # default 'NN'
  
class Rule:
    def __init__(self, from_tag, to_tag, prev_tag):
        self.from_tag = from_tag
        self.to_tag = to_tag
        self.prev_tag = prev_tag

    def apply(self, tagged_sentence):
        new_sentence = tagged_sentence[:]
        for i in range(1, len(tagged_sentence)):
            _, prev_tag = new_sentence[i - 1]
            word, tag = new_sentence[i]
            if tag == self.from_tag and prev_tag == self.prev_tag:
                new_sentence[i] = (word, self.to_tag)
        return new_sentence
      
def evaluate(tagged, gold):
    return sum(1 for (_, t1), (_, t2) in zip(tagged, gold) if t1 == t2)

def learn_rules(training_data, tag_dict):
    rules = []
    for epoch in range(1000):  # number of iterations
        best_rule = None
        best_improvement = 0
        for from_tag in ['NN', 'VB']:
            for to_tag in ['NN', 'VB']:
                if from_tag == to_tag:
                    continue
                for prev_tag in ['DT', 'NN', 'VB']:
                    rule = Rule(from_tag, to_tag, prev_tag)
                    improvement = 0
                    for sent_idx, sentence in enumerate(training_data):
                        gold = sentence
                        pred = baseline_tag(sentence, tag_dict)
                        pred = rule.apply(pred)
                        improvement += evaluate(pred, gold) - evaluate(baseline_tag(sentence, tag_dict), gold)
                    if improvement > best_improvement:
                        best_improvement = improvement
                        best_rule = rule
        if best_rule:
            rules.append(best_rule)
            print(f"Epoch {epoch + 1}: Learned rule - change {best_rule.from_tag} to {best_rule.to_tag} if prev tag is {best_rule.prev_tag}")
        else:
            break
    return rules

def tag_with_rules(sentence, tag_dict, rules):
    tagged = baseline_tag(sentence, tag_dict)
    for rule in rules:
        tagged = rule.apply(tagged)
    return tagged


# Train
tag_dict = get_initial_tags(training_data)
rules = learn_rules(training_data, tag_dict)
print(rules)
# Test on new sentence
test_sentence = [('The', 'DT'), ('cat', 'NN'), ('eat', 'VB'), ('woman', 'NN')]
predicted = tag_with_rules(test_sentence, tag_dict, rules)
print("Tagged:", predicted)
