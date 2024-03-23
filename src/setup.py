#
#
#
#
#
#
import subprocess
import platform
import psutil
import os
import help_

print("=============================Prompt=============================")
print("============================Version: 1.0=========================")
print(f"\tOperating System: { platform.system()}\n Verion: {platform.release()}\n Arquiteture: {platform.machine()}")

# print("Name of the operating system:", platform.system())
# print("Version:", platform.release())
# print("Arquiteture:", platform.machine())

# cpu_info = psutil.cpu_times()
# print("CPU Util:")
# print("  - User:", cpu_info.user)
# print("  - System:", cpu_info.system)
# print("  - Idle:", cpu_info.idle)


while(True):
    userInput = input(f'${platform.system()}->{os.getcwd()}>> ')
    if userInput == 'exit':
        break
    elif userInput == 'help':
        help_.Display()
    elif userInput == 'join':
        print("Just copy or click in https://www.github.com/dalton-222/Prompt, good lucky my friend!😊")
    else:
        try:
            #result = subprocess.check_output(userInput, shell=True, text=True)
            result = subprocess.run(userInput, shell=True, text=True)
            #print(result.strip())
            if result.returncode != 0:
                stderr_output = result.stderr.strip() if result.stderr is not None else ""
                if stderr_output:
                    print("Can't execute command. Error:", result.stderr)
            else:
                print(result.stdout)
        except Exception as e:
            print("Error:", e)
            #print("Can't execute command: ", e)
            #print("Can't execute command: ", e.returncode)
            
#
#
#
#
#
#
#
#
#
#
#