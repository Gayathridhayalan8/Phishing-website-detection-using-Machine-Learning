
class EducationalComponent:
    def __init__(self, name, topic, duration):
        self.name = name
        self.topic = topic
        self.duration = duration

    def display_info(self):
        print("Name:", self.name)
        print("Topic:", self.topic)
        print("Duration:", self.duration, "minutes")

class Lecture(EducationalComponent):
    def __init__(self, name, topic, duration, speaker):
        super().__init__(name, topic, duration)
        self.speaker = speaker

    def display_info(self):
        super().display_info()
        print("Speaker:", self.speaker)

class Workshop(EducationalComponent):
    def __init__(self, name, topic, duration, facilitator, location):
        super().__init__(name, topic, duration)
        self.facilitator = facilitator
        self.location = location

    def display_info(self):
        super().display_info()
        print("Facilitator:", self.facilitator)
        print("Location:", self.location)

# Example usage:
if __name__ == "__main__":
    lecture = Lecture("Introduction to Python Programming", "Python Basics", 60, "Dr. Smith")
    lecture.display_info()
    print()
    workshop = Workshop("Data Analysis Workshop", "Data Analysis Techniques", 120, "Prof. Johnson", "Room 202")
    workshop.display_info()
