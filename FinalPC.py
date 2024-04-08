import serial
import time

ser = serial.Serial('COM5', 2400) 
time.sleep(2)  

string_to_send = "Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one. In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs,Rajan said in the note.Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently.\n"
send_time = time.time()

for ch in string_to_send:
    ser.write(ch.encode())
    next_time = time.time()
    if next_time != send_time:
        print("Sending speed for ",ch," :", (8.0 / (next_time - send_time)))
    send_time = next_time

ser.write(b"0\n1005\n")

received_data = ''
start_time = time.time()
while True:
    received_byte = ser.read()
    if not received_byte:
        continue
    received_char = received_byte.decode('utf-8', errors='replace')

    end_time = time.time()
    if received_char == '\n':
        break
    received_data += received_char
    speed = 8.0 / (end_time - start_time)
    print("Received data:", received_char)
    print("Receiving speed:", speed)
    start_time = end_time

print("Final received data from MCU:\n", received_data.strip())
ser.close()
