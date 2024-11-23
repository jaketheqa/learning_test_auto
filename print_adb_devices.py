import subprocess


def get_aos_device():
    try:
        # Execute "adb devices"
        cmd = 'adb devices'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()

        # Get All of Connected Devices
        output = out.decode().splitlines()

        # Get device info per line
        if len(output) > 0:
            for i in range(len(output)):
                print(output[i])

            # print("********* output[0] : " + output[0])
            # print("********* output[1] : " + output[1])

            print(">>>>> DEVICE SERIAL NUMBER : ", output[1].split()[0])
        else:
            print("No Connected Devices Found...")
    except:
        print("Couldn't Find Any Connected Devices")


if __name__ == '__main__':
    get_aos_device()
