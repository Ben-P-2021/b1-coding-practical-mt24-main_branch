class PDController:
    def __init__(self, kp, kd):
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain
        self.previous_error = 0

    def compute(self, setpoint, measured_value):
        # Calculate error
        error = setpoint - measured_value
        
        # Calculate derivative of error
        derivative = error - self.previous_error
        
        # Calculate control output
        output = self.kp * error + self.kd * derivative
        
        # Update previous error
        self.previous_error = error
        
        return output

# Example usage
if __name__ == "__main__":
    pd = PDController(kp=1.0, kd=0.1)
    setpoint = 10
    measured_value = 8
    control_output = pd.compute(setpoint, measured_value)
    print(f"Control Output: {control_output}")