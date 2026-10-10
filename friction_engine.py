class CalibratedFrictionEngine:
    def __init__(self, threshold=0.5):
        self.threshold = threshold
    def evaluate_effort(self, prompt_text, time_spent):
        if "give me answer" in prompt_text.lower():
            return "TRIGGER_SOCRATIC_BRAKE"
        return "ALLOW_ASSISTANCE"
