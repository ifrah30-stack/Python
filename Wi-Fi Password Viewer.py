import subprocess

networks = subprocess.check_output("netsh wlan show profiles").decode()
for line in networks.split("\\n"):
    if "All User Profile" in line:
        name = line.split(":")[1].strip()
        try:
            password = subprocess.check_output(f"netsh wlan show profile {name} key=clear").decode()
            key_line = [l for l in password.split('\\n') if 'Key Content' in l]
            print(f"{name}: {key_line[0].split(':')[1].strip()}" if key_line else f"{name}: No Password")
        except:
            pass
