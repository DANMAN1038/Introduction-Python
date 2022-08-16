#Danial Syed
current_state = []
button = []
def launch_rocket(current_state, button):
        if button == "start_btn" and current_state == "IDLE":
            end_state = "READY"
        elif button == "safe_btn" and current_state == "READY":
            end_state = "SAFE"
        elif button == "launch_btn" and current_state == "SAFE":
            end_state = "LAUNCH"
        else:
            end_state = "IDLE"
        return(end_state)
print(launch_rocket("IDLE", "start_btn"))
