
class PDController:
    def __init__(self, kp, kd):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0

    def control(self, setpoint, measured_value):
        error = setpoint - measured_value
        derivative = error - self.previous_error
        output = self.kp * error + self.kd * derivative
        self.previous_error = error
        return output

# Example usage with the Submarine class
if __name__ == "__main__":
    from uuv_mission import Submarine
    # Initialize the submarine and PD controller
    submarine = Submarine()
    pd_controller = PDController(kp=1.0, kd=0.1)

    # Example setpoint and measured value
    setpoint = 10.0
    measured_value = submarine.get_depth()

    # Calculate control output
    control_output = pd_controller.control(setpoint, measured_value)
    print(control_output)
    # Apply control output to the submarine
    #submarine.apply_control(control_output)