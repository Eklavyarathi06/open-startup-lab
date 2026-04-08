class Memory:

    def __init__(self):
        self.short_term = []
        self.long_term = []

    def add(self, event):
        self.short_term.append(event)

        if len(self.short_term) > 5:
            self.long_term.append(self.short_term.pop(0))

    def get_context(self):
        return self.long_term[-5:] + self.short_term
    
    def get_penalties(self):
        penalties = 0
        for item in self.long_term:
            if "ignore" in item:
                penalties += 0.05
        return penalties