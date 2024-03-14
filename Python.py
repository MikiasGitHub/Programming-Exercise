class MinitermGenerator:
    def __init__(self, predicates):
        self.predicates = predicates

    def generate_horizontal_miniterms(self):
        miniterms = []
        for predicate in self.predicates:
            miniterms.extend(self._generate_miniterms_for_predicate(predicate))
        return miniterms

    def _generate_miniterms_for_predicate(self, predicate):
        miniterms = []
        for key, value in predicate.items():
            miniterm = {key: value}
            miniterms.append(miniterm)
        return miniterms

# Example usage:
predicates = [
    {'A': 'a1', 'B': 'b1', 'C': 'c1'},
    {'A': 'a2', 'B': 'b2', 'C': 'c2'}
]

miniterm_generator = MinitermGenerator(predicates)
horizontal_miniterms = miniterm_generator.generate_horizontal_miniterms()
print(horizontal_miniterms)
