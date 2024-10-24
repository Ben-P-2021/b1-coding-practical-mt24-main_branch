class PDController:
    def __init__(self, kp, kd):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0

    def control(self, reference, measured_value):
        error = reference - measured_value
        derivative = error - self.previous_error
        output = self.kp * error + self.kd * derivative
        self.previous_error = error
        return output