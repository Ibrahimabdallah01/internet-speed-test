from tkinter import *
import subprocess
import json


def speedcheck():
    try:
        result = subprocess.run(
            ["speedtest-cli", "--json"], capture_output=True, text=True
        )
        speed_data = result.stdout.strip()
        speed_json = json.loads(speed_data)

        download_speed = speed_json["download"] / 10**6  # in Mbps
        upload_speed = speed_json["upload"] / 10**6  # in Mbps

        down = f"{download_speed:.3f} Mbps"
        upload = f"{upload_speed:.3f} Mbps"

        lab_down.config(text=down)
        lab_upload.config(text=upload)
    except json.decoder.JSONDecodeError as e:
        lab_down.config(text="Error fetching speed")
        lab_upload.config(text="Please try again")


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="Gray")

lab = Label(
    sp,
    text="Internet Speed Test",
    font=("Time New Roman", 30, "bold"),
    bg="Blue",
)
lab.place(x=60, y=40, height=50, width=380)

lab = Label(
    sp,
    text="Download Speed",
    font=("Time New Roman", 30, "bold"),
)
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(
    sp,
    text="00",
    font=("Time New Roman", 30, "bold"),
)
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(
    sp,
    text="Upload speed",
    font=("Time New Roman", 30, "bold"),
)
lab.place(x=60, y=310, height=50, width=380)

lab_upload = Label(
    sp,
    text="00",
    font=("Time New Roman", 30, "bold"),
)
lab_upload.place(x=60, y=380, height=50, width=380)

self = Button(
    sp,
    text="Check Speed",
    font=("Time New Roman", 30, "bold"),
    relief=RAISED,
    bg="Blue",
    command=speedcheck,
)
self.place(x=60, y=490, height=50, width=380)

sp.mainloop()
